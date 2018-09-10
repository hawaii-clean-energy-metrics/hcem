from xl2py_util import *
from xl2py_cell_info import CellInfo
import xl2py_tokenizer as tokenizer

logger = setup_logger()

EXCEL_TOKEN_MAPPING = OrderedDict([
    ('&', 'concat'),
    ('+', 'add'),
    ('*', 'mult'),
    ('-', 'sub'),
    ('/', 'divide'),
    ('=', 'equal'),
    ('^', 'POW'),
    ('<', 'lessthan'),
    ('>', 'greaterthan'),
    ('CONCATENATE', 'CONCATENATE'),
    ('VLOOKUP', 'VLOOKUP'),
    ('SUM', 'SUM'),
    ('SUMIFS', 'SUMIFS'),
    ('IF', 'IF'),
    ('ABS', 'ABS'),
    ('ISERROR', 'ISERROR'),
    ('ISNA', 'ISNA'),
    ('NA', 'NA'),
    ('SUMIF', 'SUMIF'),
    ('ISERR', 'ISERR'),
    ('IFERROR', 'IFERROR'),
    ('MATCH', 'MATCH'),
    ('INDEX', 'INDEX'),
    ('YEAR', 'YEAR'),
    ('DATE', 'DATE'),
    ('MAX', 'MAX'),
    ('AVERAGE', 'AVERAGE'),
    ('COUNT', 'COUNT'),
    ('CORREL', 'CORREL'),
    ('SUMPRODUCT', 'SUMPRODUCT'),
    ('MONTH', 'MONTH'),
    ('COLUMN', 'COLUMN'),
    ('ROW', 'ROW'),
    ('OR', 'OR'),
    ('HLOOKUP', 'HLOOKUP'),
    ('AVERAGEIF', 'AVERAGEIF'),
    ('ISTEXT', 'ISTEXT'),
    ('SQRT', 'SQRT'),
    ('COUNTIF', 'COUNTIF'),
    ('MID', 'MID'),
    ('_xlfn.FORMULATEXT', 'FORMULATEXT'),
    ('FIND', 'FIND')
])


def get_excel_token_str(tokenstr):
    token = EXCEL_TOKEN_MAPPING.get(tokenstr)
    if token is None:
        logger.error("{} not in EXCEL_TOKEN_MAPPING table".format(tokenstr))
        token = EXCEL_TOKEN_MAPPING[tokenstr] = tokenstr
    return token




class Cell2Py(object):
    def __init__(self, cell, add_dependency_fn, dcell):
        super(Cell2Py, self).__init__()
        self.cell = CellInfo(cell, dcell)
        self.add_dependency = add_dependency_fn

    def emit_class(self, emitter):
        emitter.emit = "@register({})".format(self.cell.worksheet_name)
        emitter.emit = "class {}():".format(self.cell.coordinate)
        emitter.indent += 1
        emitter.emit = "# {}".format(self.cell.name)

    def emit_property(self, emitter, name, val):
        emitter.emit = "{} = {}".format(name, val)

    def emit_property_def(self, emitter, name, val):
        emitter.emit = ""
        emitter.emit = "@property"
        emitter.emit = "def {}(self):".format(name)
        emitter.indent += 1
        emitter.emit = "return {}".format(val)
        emitter.indent -= 1

    def emit(self, emitter):

        if self.cell.formula is None and self.cell.value in [None, ""]:
            return None

        indent = emitter.indent
        try:
            emitter.emit = ""
            self.emit_class(emitter)
            self.emit_property(emitter, "value", python_rep(self.cell.value))
            if not self.cell.is_formula and isinstance(self.cell.value, datetime.datetime):
                self.emit_property(emitter, "isdatetime", "True")
            self.emit_def_eval_formula(emitter)
        except:
           print "Unexpected error:", sys.exc_info()[0]
           print "self={}".format(str(self))
           print "cell.value=".format(str(self.cell.value))
           print "cell.tokens=".format(str(self.cell.tokens))
           raise

        emitter.indent = indent

    def __str__(self):
        return str(self.cell)

    def vname(self, prefix="var"):
        n = 0
        varname = ''
        while not n or self.taken[varname]:
            n += 1
            varname = "{}_{}".format(prefix, n).lower()
        self.taken[varname] += 1
        return varname


    def eval_token(self, tstack, frame):
        token = tstack.pop(0)
        tokenstr = str(token)

        if isinstance(token, tokenizer.OperatorNode) or isinstance(token, tokenizer.FunctionNode):
            return (self.vname(), get_excel_token_str(tokenstr), token.num_args)


        if isinstance(token, tokenizer.RangeNode):
            token_worksheet, token_bounds = compute_range_tuple(tokenstr, self.cell.worksheet_name)

            if token_bounds == (0, 0, 0, 0):
                print "cell: {} failed to parse range {}".format(self.cell.name, tokenstr)

            token_worksheet = xlat_worksheet(token_worksheet)
            if self.add_dependency:
                self.add_dependency(token_worksheet, token_bounds)

            if token_bounds == (0, 0, 0, 0):
                return (self.vname("range"), "ERRREF #", 0)

            if (token_bounds[0] > 0 and token_bounds[0] == token_bounds[2] and
                token_bounds[1] > 0 and token_bounds[1] == token_bounds[3]):
                cellname = cell_name("", token_bounds[:2])
                call = "{}.{}".format(token_worksheet, cellname)
                if len(tstack) and str(tstack[0]) == "_xlfn.FORMULATEXT":
                    call = call + ".formula #"
                return (self.vname(cellname), call, 0)

            frame += map(str, token_bounds)
            return (self.vname("range"), token_worksheet, 4)

        if isinstance(token, tokenizer.ASTNode):
            if token.token.tsubtype == tokenizer.ExcelParserTokens.TOK_SUBTYPE_NUMBER:
                tokenstr = float(tokenstr)
            frame.append(python_rep(tokenstr))

        return None


    def emit_def_eval_formula(self, emitter):
        if not self.cell.is_formula:
            return

        self.emit_property(emitter, "formula", python_rep(self.cell.formula))

        emitter.emit = "@eval_fn"
        emitter.emit = "def {}():".format(self.cell.coordinate)
        emitter.indent += 1

        self.taken = Counter()
        frame = []
        tstack = self.cell.tokens
        while len(tstack):
            function = self.eval_token(tstack, frame)

            if function:
                varname, fname, num_args = function
                args = []
                # if there are arguments, pop them of the frame
                if num_args:
                    frame, args = frame[:-num_args], frame[-num_args:]
                emitter.emit = "{} = {}({})".format(varname, fname, ", ".join(args))
                frame.append(varname)

        emitter.emit = "return {}".format(frame[-1])
        emitter.indent -= 1
