
import sys
import os
import mimetypes
import pprint
import collections

import ckanapi
import os
import collections

import json


def maybe_to_bool(v):
    if v == "False":
        return False
    if v == "True":
        return True
    return v


def maybe_to_json(v):
    try:
        nv = json.loads(v)
        v = nv
    except:
        pass
    return v

def env_substiutions(v):
    for env_key, env_val in os.environ.iteritems():
        v = v.replace("${}{}{}".format("{", env_key, "}"), env_val)
    return v

def get_config(inifilename=None, section=None):
    import ConfigParser
    config = ConfigParser.SafeConfigParser()

    if inifilename is None:
        inifilename = os.environ.get("CONFIG")

    config.read(inifilename)

    result = collections.OrderedDict()
    for section_name in config.sections():
        section_dict = collections.OrderedDict()
        for key,val in config.items(section_name):
            val = env_substiutions(val)
            val = maybe_to_bool(val)
            val = maybe_to_json(val)
            section_dict[key] = val
        result[section_name] = section_dict

    if section:
        result = result.get(section)

    return result


def get_ckan(ckan_config=None):
    if not ckan_config:
        ckan_config = get_config(None, "ckan")

    assert ckan_config
    ua = 'ckanhepf/1.0 (+https://hepf.hawaiiopendata.org/data)'
    ckan = ckanapi.RemoteCKAN(ckan_config["url"], apikey=ckan_config["key"]) #user_agent=ua
    setattr(ckan,'ckan_config', ckan_config)
    return ckan
