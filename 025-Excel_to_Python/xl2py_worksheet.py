from xl2py_util import Emitter
from xl2py_cell import Cell2Py


class Worksheet(object):
    def __init__(self, worksheet, add_dependency_fn = None, worksheet_data=None):
        super(Worksheet, self).__init__()
        self.worksheet = worksheet
        self.add_dependency_fn = add_dependency_fn
        self.worksheet_data = worksheet_data

    @property
    def text(self):
        emitter = Emitter()
        self.emit_header(emitter)
        self.emit_cells(emitter)
        return emitter.emit

    def emit_header(self, emitter):
        emitter.emit = "# -*- coding: utf-8 -*-"
        emitter.emit = "from xl2py_excel_runtime import *"
        emitter.emit = "{} = Worksheet('{}', {}, {})".format(self.worksheet.title, self.worksheet.title, 10, 10)
        emitter.emit = ""
        emitter.emit = ""

    def emit_cells(self, emitter):
        for row,drow in zip(self.worksheet, self.worksheet_data):
            for cell,dcell in zip(row,drow):
                c2p = Cell2Py(cell, self.add_dependency_fn, dcell)
                c2p.emit(emitter)


