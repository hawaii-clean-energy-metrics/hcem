from collections import OrderedDict

import xl2py_worksheet_names
from xl2py_excel_runtime import *

import importlib
import traceback
import sys

worksheets = OrderedDict()
names = xl2py_worksheet_names.names


overloads = {}

def rusage(msg=""):
    from resource import getrusage, RUSAGE_SELF
    rusage = getrusage(RUSAGE_SELF)
    print "\\n".join('"rusage","{}",{}'.format(msg,','.join(['"{}"'.format(r) for r in rusage])).split("\n"))

def overload_worksheet(worksheet, csv_filename):
    data = ""
    with open(csv_filename, "r") as f:
        data = f.read()

    lines = data.split("\n")
    register_cell = register_cell_class_to_worksheet(worksheet)
    for row,line in enumerate(lines):
        if not len(line): continue
        assert line[0] == '"'
        assert line[-1] == '"'
        line = line[1:-1]
        cells = line.split('","')
        sys.stderr.write("\n\n")
        for col,cell in enumerate(cells):
            if not len(cell): continue

            try:
                v = float(cell)
            except:
                v = cell

            try:
                v = int(cell)
            except:
                pass

            excel_time = parse_datetime_to_excel_time(v)
            isdatetime = excel_time != v
            value = excel_time if isdatetime else v

            cell_instance = worksheet.icells.get((col + 1, row + 1))
            if cell_instance:
                cid = colrow_to_name(col + 1, row + 1)
                #sys.stderr.write(cid+". ")
                cell_instance.setcache(value, isdatetime)

                # klass = cell_instance.cclass()
                # setattr(klass, "value", value)
                # setattr(klass, "cache_value", value)
                # setattr(klass, "isdatetime", isdatetime)
                # setattr(klass, "cache_generation", 1)
                # if hasattr(klass, "formula"):
                #     delattr(klass, "formula")
            else:
                cid = colrow_to_name(col + 1, row + 1)
                #sys.stderr.write(cid+"+ ")
                klass = type(cid, (object, ), { "value": value, "isdatetime": isdatetime })
                register_cell(klass)


class DelayedModule():
    loaded_modules = {}
    delayed_modules = {}
    loaded_worksheets = {}


    def __init__(self, modname):
        #print "DelayedModule({})".format(modname)
        worksheets[modname] = self
        DelayedModule.delayed_modules[modname] = self
        self.modname = modname

    @staticmethod
    def getmod(modname):
        mod = DelayedModule.loaded_modules.get(modname)
        if mod:
            return getattr(mod, modname)

        mod = importlib.import_module(modname, __name__)

        modclass = getattr(mod, modname)

        if modname in overloads:
            for csv_filename in overloads[modname]:
                rusage("overloading {} with {}".format(modclass.title, csv_filename))
                overload_worksheet(modclass, csv_filename)

        DelayedModule.loaded_modules[modname] = mod
        worksheets[modname] = modclass
        DelayedModule.loaded_worksheets[modname] = modclass


        #
        #for ws1, mod1 in DelayedModule.loaded_modules.iteritems():
        #    for ws2, modclass in worksheets.iteritems():
        #        setattr(mod1, ws2, modclass)

        #return modclass

        for othermodname in worksheets.keys():
            if othermodname != modname:
                othermod = worksheets[othermodname]
                assert othermod is not None
                setattr(mod, othermodname, othermod)
        return modclass


    def __getattr__(self, attr):
        modname = getattr(self, "modname")
        #print "...loading {}".format(modname)
        #print "getattr({}.{}) stack={}".format(modname, attr, "".join(traceback.format_stack()))

        #assert modname not in DelayedModule.loaded_modules
        mod = DelayedModule.getmod(modname)


        #modclass = getattr(mod, modname)
        modclass = mod

        #globals()[modname] = modclass
        setattr(sys.modules[__name__], modname, mod)
        ret = getattr(modclass, attr)
        return ret


def __import_worksheet_module(modname):
    modclass = globals().get(modname)
    if modclass is None:
        #print " >>> {} has {}".format(modname, "")#", ".join(globals().keys()))
        modclass = DelayedModule(modname)
        globals()[modname] = modclass

    return modclass


def __import_worksheet_modules(modnames):
    for modname in modnames:
        __import_worksheet_module(modname)


__import_worksheet_modules(xl2py_worksheet_names.names)
