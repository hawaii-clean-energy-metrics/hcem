#!/usr/bin/env python
import xl2py_tokenizer as tokenizer
from xl2py_util import *


class CellInfo(object):
    def __init__(self, cell, dcell):
        super(CellInfo, self).__init__()
        self.cell = cell
        self.dcell = dcell

    @property
    def safe_str_val(self):
        return safe_str(self.cell.value)

    def __str__(self):
        return self.safe_str_val

    @property
    def is_formula(self):
        return self.safe_str_val.startswith('=')

    @property
    def value(self):
        return self.dcell.value

    @property
    def formula(self):
        if self.is_formula:
            return self.cell.value
        else:
            return None

    @property
    def worksheet(self):
        return self.cell.parent

    @property
    def coordinate(self):
        return self.cell.coordinate

    @property
    def worksheet_name(self):
        return self.cell.parent.title

    @property
    def workbook(self):
        return self.worksheet.parent

    @property
    def name(self):
        return "'{}'!{}".format(self.worksheet.title, self.coordinate)


    def patch_token_stack(self, tstack):
        for i, token in enumerate(tstack):
            tokenstr = str(token).upper()
            if (isinstance(token, tokenizer.FunctionNode) and tokenstr in ["COLUMN", "ROW"]):
                assert token.num_args <= 1
                if token.num_args == 1:
                    assert i > 0, "Nothing on stack for COLUMN or ROW"
                    ptoken = tstack[i - 1]
                elif token.num_args == 0:
                    ptoken = self.coordinate
                range_tuple = compute_range_tuple(str(ptoken), self.worksheet_name)
                if range_tuple[1] == (0, 0, 0, 0):
                    print "cell: {} failed to parse range {}".format(self.name, str(ptoken))
                rep = range_tuple[1][1] if tokenstr == "ROW" else col_letter(range_tuple[1][0])
                ntokenstr = "'{}'!{}:{}".format(range_tuple[0], rep, rep)
                ntoken = tokenizer.f_token(ntokenstr, "operand", "range")
                tstack[i - 1] = tokenizer.RangeNode(ntoken)
        return tstack

    @property
    def tokens(self):
        if not self.is_formula:
            return []

        formula_str = self.safe_str_val
        formula_str = formula_str.replace("#REF!", "UNKNOWN")
        tokens = tokenizer.shunting_yard(formula_str)
        tokens = self.patch_token_stack(list(tokens))
        return tokens
