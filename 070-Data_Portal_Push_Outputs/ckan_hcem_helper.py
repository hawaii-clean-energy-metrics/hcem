#!/usr/bin/env python2

import sys
import os
import mimetypes
import pprint
import collections

import ckan_util
import traceback
import json
import Spreadsheet



def get_fieldstorage(data):
    files = None
    if "filename" in data:
        filename = data["filename"]
        del data["filename"]
        files = { "upload": open(filename, "rb") }
        if not data.get("url"):
            data["url"] = os.path.basename(filename)
    return files, data


def set_mimetype(data):
    mimetypes.init()
    _, extension = os.path.splitext(data.get("filename", data.get("url", "")))
    data["mimetype"] = mimetypes.types_map.get(extension, None)
    return data


def resource_create(ckan, data, cmd="resource_create"):
    files, data = get_fieldstorage(data)
    data = set_mimetype(data)
    return ckan.call_action(cmd, data, files=files)


def resource_search_and_remove(ckan, data):
    resources = ckan.call_action("resource_search", data)

    delete_results = []
    if resources['count'] > 0:
        if data.get('name_filter_out'):
            resources['results'] = [res for res in resources['results'] if not data['name_filter_out'] in res['name']]

        for resource in resources['results']:
            data['id'] = resource['id']
            sys.stderr.write("deleting name=\"{}\"\n".format(resource['name']))
            sys.stderr.flush()
            delete_results.append(ckan.call_action("resource_delete", data))

    return {
        u'resources': resources,
        u'delete_results': delete_results
    }


def organization_update(ckan, data, cmd="organization_update"):
    files, data = get_fieldstorage(data)
    return ckan.action.organization_update(id=data['id'], image_upload=files['upload'])


def get_fields_records_from_csv(url):
    csv = Spreadsheet.Spreadsheet(url, None, 0, True)

    fstr = "col_{}"

    col_row = False
    fields = list(csv.header._fields)
    if col_row:
        fields = ["row"] + fields

    fields = [{"id":fstr.format(field), "type":"text"} for field in fields]

    records = [row._asdict() for row in csv.rows]

    records = [collections.OrderedDict([("col_row", "{:03d}".format(i+1))] if col_row else [] +  [(fstr.format(f),v) for f,v in row.iteritems()]) for i, row in enumerate(records)]

    return fields, records



def upload_csv(ckan, data):
    url = data["filename"] if "filename" in data else data.get("url","")

    fields, records = get_fields_records_from_csv(url)

    data['fields'] = fields
    data['records'] = records
    if fields and fields[0].get("id") == "col_row":
        data['primary_key'] = ['col_row']

    print "data={}".format(data)

    return ckan.call_action('datastore_create', data)




def process_config(config):
    ckan = ckan_util.get_ckan(config.get("ckan"))

    for sec,data in config.iteritems():
        cmd = data.get("command")
        del data['command']
        # print 'cmd="{}"'.format(cmd)
        # print 'data={}'.format(data)

        if bool(data.get("debug")):
            pprint.PrettyPrinter(indent=4).pprint(data)


        status = {}
        try:
            if cmd is None:
                continue
            elif cmd == "resource_update":
                status = resource_create(ckan, data, "resource_update")
            elif cmd == "upload_csv":
                status = upload_csv(ckan, data)

            elif cmd == "resource_create":
                status = resource_create(ckan, data)

            elif cmd == "organization_update":
                status = organization_update(ckan, data)

            elif cmd == "resource_search_and_remove":
                status = resource_search_and_remove(ckan, data)
            else:
                status = ckan.call_action(cmd, data)
        except:
            traceback.print_exc()
            sys.exit(1)
            pass
        print json.dumps(status, indent=4)
        #pprint.PrettyPrinter(indent=4).pprint(status)

if __name__ == "__main__":
    config = collections.OrderedDict()
    for arg in sys.argv[1:]:
        if arg.startswith('--'):
            key,val = arg[2:].split('=',1)
            config['commandline'] = config.get('commandline',collections.OrderedDict())
            config['commandline'][key] = val if val else ""
            
        elif arg.lower().endswith('.ini') and os.path.isfile(arg):
            process_config(ckan_util.get_config(arg))
            
    if config.get('commandline'):
        process_config(config)

    sys.exit(0)
