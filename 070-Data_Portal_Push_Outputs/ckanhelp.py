#!/usr/bin/env python2

import ckanapi
import sys
import re
import pprint
import ckan_util
from collections import OrderedDict

try:
    ckan = ckan_util.get_ckan()
except:
    print "Invalid CKAN url and key in .ini file specified by CONFIG"
    sys.exit(1)

cmds = sys.argv[1:]
if not cmds:
    cmds.append("help_show")

for name in cmds:
    text = ckan.call_action("help_show", { "name": name })
    m = re.split(':(param|type|rtype) ([^:]*): ', text)
    i = 0
    obj = OrderedDict()
    while i < len(m):
        txt = m[i]
        if m[i] == 'param':
            assert m[i+3] == 'type'
            key = m[i+1]
            typ = m[i+5].strip(" \n")
            txt = m[i+2]
            txt = "[{}] {}".format(typ, txt)
            txt = txt.replace("\n", " ")
            txt = re.sub(" +", " ", txt)

            obj[key] = txt
            i += 6
        else:
            i += 1
            print txt
        #txt = txt.replace("\n", " ")
        #txt = re.sub(" +", " ", txt)

    print "{} =\n{}".format(name,"{")
    for k,v in obj.iteritems():
        print "    \"{}\": \"{}\"".format(k,v)
    print "}"

sys.exit(0)
