from xl2py_util import *
from xl2py_worksheet import *
from xl2py_dependencies import *
from time import time as time_get_timestamp
from os import rename

class Workbook(object):
    def __init__(self, workbook, output_path, workbook_data=None):
        # Patch up the worksheet names
        for i, worksheet in enumerate(workbook.worksheets):
            worksheet.title = xlat_worksheet(worksheet.title)

        make_path(output_path)

        self.dependencies = Dependencies()

        self.copy_framework_files(output_path)
        self.write_all_worksheets_in_workbook(workbook, output_path, workbook_data)
        self.write_sheetnames_file(workbook, output_path)
        self.dependencies.write_dependencies(output_path)

    def write_all_worksheets_in_workbook(self, workbook, output_path, workbook_data):
        for i, worksheet in enumerate(workbook.worksheets):
            t0 = time_get_timestamp()
            sys.stdout.write("{} ({} of {})".format(worksheet.title, i + 1, len(workbook.worksheets)))
            self.write_worksheet_file(worksheet, output_path, workbook_data.worksheets[i] if workbook_data else None)
            dt = time_get_timestamp() - t0
            sys.stdout.write(" time={:>6.4f}s\n".format(dt))

    def copy_framework_files(self, output_path):
        srcdir = os.path.dirname(os.path.abspath(__file__))
        shutil.copy(srcdir + "/xl2py_workbook_runtime.py", output_path)
        shutil.copy(srcdir + "/xl2py", output_path)
        shutil.copy(srcdir + "/xl2py_excel_runtime.py", output_path)

    def write_sheetnames_file(self, workbook, output_path):
        print "Sheet names: {}".format("\n".join(workbook.sheetnames))
        outpy = "{}xl2py_worksheet_names.py".format(output_path)
        with open(outpy, "w") as f:
            f.write("names = {}".format(workbook.sheetnames))

    def write_worksheet_file(self, worksheet, output_path, worksheet_data):
        outpy = "{}{}.py".format(output_path, worksheet.title)
        sys.stdout.write(" => {}".format(outpy))
        outtmp = outpy+".tmp"
        with open(outtmp, "w") as f:
            add_dependency_fn = self.dependencies.get_add_dependency_fn(worksheet.title)
            text = Worksheet(worksheet, add_dependency_fn, worksheet_data).text
            f.write(text)
        os.rename(outtmp, outpy)
