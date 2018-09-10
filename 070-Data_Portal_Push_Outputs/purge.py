#!/usr/bin/env python2

import sys
import pprint
import ckan_util
import urllib2

ckan = ckan_util.get_ckan()

headers={'Authorization':ckan.ckan_config['key']}
data='purge-packages=purge'
url="{}ckan-admin/trash".format(ckan.ckan_config['url'])

req = urllib2.Request(url, data, headers)
resp = urllib2.urlopen(req)

sys.exit(0)
