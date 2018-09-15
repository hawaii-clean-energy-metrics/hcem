import re

import inspect
from sys import stderr

import time
import datetime
from calendar import timegm as struct_time_to_timestamp


def emptyhook(f):
    return f

hook = emptyhook
excel_fn_decorator = hook
helper_fn_decorator = hook

ROWCOL = re.compile(r'^(?P<col>[A-Z]+)?(?P<row>[0-9]+)?$')
ERRORVAL = None
DIVIDEBYZERO = None


class ERR_class():
    def __init__(self, rep):
        self.rep = rep
    def __repr__(self):
        return self.rep

ERRDIV0 = ERR_class("#DIV/0!")
ERRNA = ERR_class("#N/A")
ERRREF = ERR_class("#REF!")
ERREF = ERRREF
ERRNAME = None
ERRNULL = None
ERRNUM = None
ERRVALUE2 = ERR_class("#VALUE!")
ERRVALUE = None

eval_fn = staticmethod

SECONDS_PER_DAY = 24 * 60 * 60  # 86400
EXCEL_EPOCH_OFFSET_FROM_UNIX_EPOCH_IN_DAYS = -25569


# DEBUG = True

dontthrow = "dontthrow"
GLOBAL_CACHE = {}

global DEBUG
global DOCACHE
DOCACHE = True
DEBUG = False
TFLOAT = type(1.0)
TINT = type(1)
NUMBER_TYPES = (TINT, TFLOAT)

ERRTYPES = (None, ERRDIV0, ERRNA, ERRREF, ERRVALUE2)

def reset_cache():
    for key in GLOBAL_CACHE.keys():
        del GLOBAL_CACHE[key]


class XLDate(float):

    def to_datetime(self):
        return excel_to_datetime(self)

    def to_string(self):
        return excel_to_datetime_string(self)

    def to_tuple(self):
        return excel_to_time_tuple(self)


@helper_fn_decorator
def py_iserror(val):
    return val == ERRORVAL


@helper_fn_decorator
def py_tofloat(val):
    if val is None:
        return 0

    if type(val) in NUMBER_TYPES or isinstance(val, ERR_class):
        return val

    return 0


@helper_fn_decorator
def py_toint(val):
    if ISERROR(val):
        return val
    try:
        ival = int(val)
    except:
    # if not isinstance(val, int):
        print "<YES_ERR> py_toint fails on '{}', type={}'".format(val, type(val))
        return ERRNUM
    return ival


@helper_fn_decorator
def py_maybeint(val):
    if isinstance(val, float):
        ival = int(val)
        if abs(val - ival) < 0.0000001:
            return ival
    return val


# DATETIME =
# re.compile(r'(?P<YYYY>[0-9][0-9][0-9][0-9])-(?P<MM>[0-1][0-9])-(?P<DD>[0-3][0-9])(00:00:00')

DATETIMESTR = """(?P<YEAR>[0-9][0-9][0-9][0-9])[-\/](?P<MONTH>[0-1][0-9])[-\/](?P<DAY>[0-3][0-9])[ T-]?((?P<HOUR>[012][0-9])[:-](?P<MINUTE>[0-5][0-9])[:-]?(?P<SECOND>[0-5][0-9])?)?"""
DATETIME = re.compile(DATETIMESTR)


def parse_datetime(val):
    if isinstance(val, str):
        match = DATETIME.match(val)
        if match:
            dt = {k: int(v) if v else 0 for k,
                  v in match.groupdict().iteritems()}
            tv = datetime.datetime(dt['YEAR'], dt['MONTH'], dt[
                                   'DAY'], dt['HOUR'], dt['MINUTE'], dt['SECOND'])
            val = tv
    return val


def datetime_to_excel_time(dt):
    if isinstance(dt, datetime.datetime):
        return DATE(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    return dt


def parse_datetime_to_excel_time(val):
    return datetime_to_excel_time(parse_datetime(val))


class Unknown():

    @helper_fn_decorator
    def __call__(self, *args):
        ncols = args[2] - args[0] + 1
        nrows = args[3] - args[1] + 1
        result = [[ERRORVAL] * ncols] * nrows
        print "UNKNOWN({}) returns {}".format(args[0:4], result)
        return result

    @helper_fn_decorator
    def __getattr__(self, attr):
        print "UNKNOWN.{} returns None".format(attr)
        return lambda: ERRORVAL

UNKNOWN = Unknown()


class EmptyCell():
    value = None
    formula = None

    @helper_fn_decorator
    def __call__(self):
        return None

EMPTYCELL = EmptyCell()


@helper_fn_decorator
def col_letter(idx):
    letters = ""
    while idx:
        idx, rem = divmod(idx - 1, 26)
        letters = chr(rem + 65) + letters
    return letters


@helper_fn_decorator
def col_letter_val(inletters):
    idx = 0
    letters = inletters.upper()
    while len(letters):
        letter, letters = letters[0], letters[1:]
        idx = idx * 26 + ord(letter) - 64
    return idx


@helper_fn_decorator
def name_to_colrow(name):
    colrow = ROWCOL.match(name).groups()
    col = col_letter_val(colrow[0]) if colrow[0] else 0
    row = int(colrow[1]) if colrow[1] else 0
    return col, row


@helper_fn_decorator
def colrow_to_name(col, row):
    return "{}{}".format(col_letter(col), row)


@helper_fn_decorator
def trim_ranges(ranges, max_only=True):
    MAX = 1000000

    rchop = MAX
    cchop = MAX

    for r in ranges:
        ws = r.worksheet
        c0, r0, c1, r1, nc, nr = r.cbounds()

        if rchop > nr - 1:
            rchop = nr - 1

        if cchop > nc - 1:
            cchop = nc - 1

    for r in ranges:
        ws = r.worksheet
        c0, r0, c1, r1, nc, nr = r.cbounds()

        chop = max(0, r1 - ws.maxrow)
        rchop = min(rchop, chop)

        chop = max(0, c1 - ws.maxcol)
        cchop = min(cchop, chop)

    if rchop == 0 and cchop == 0:
        return

    stderr.write("T")
    # stderr.write("***\nTrim Ranges: ")
    for r in ranges:
        c0, r0, c1, r1, nc, nr = r.cbounds()
        # stderr.write("({}, {}) from {} ->".format(cchop, rchop, r))
        r.push_original_bounds(c0 + 1, r0 + 1, c1 - cchop, r1 - rchop)
        # stderr.write("{}\n".format(r))

    # stderr.write("***\n")


class Range():

    def __str__(self):
        c0, r0, c1, r1, nc, nr = self.cbounds()
        return "'{}'!{}{}:{}{}".format(self.worksheet.title, col_letter(c0 + 1), r0 + 1, col_letter(c1), r1)

    def __repr__(self):
        return "<Range {}>".format(self.__str())

    def __init__(self, worksheet, c0, r0, c1, r1):
        self.cbounds_stack = []
        self.worksheet = worksheet
        self.push_original_bounds(c0, r0, c1, r1)

    def __getitem__(self, key):
        print "Slice: {}".format(key)
        print "Slice start: {} ".format(key.start)
        print "Slice end: {} ".format(key.stop)

    def pop_bounds(self):
        if len(self.cbounds_stack) == 1:
            return
        return self.cbounds_stack.pop()

    def push_original_bounds(self, c0, r0, c1, r1):
        self.obounds = (c0, r0, c1, r1)

        if c0 == 0:
            c0 = self.worksheet.mincol
            c1 = self.worksheet.maxcol

        if r0 == 0:
            r0 = self.worksheet.minrow
            r1 = self.worksheet.maxrow

        # range_id = "'{}'!{}{}:{}{}".format(self.title, col_letter(c0), r0, col_letter(c1), r1)
        # if range_id in GLOBAL_CACHE:
        #    if DEBUG:
        # pass #stderr.write("skipping cached range {}\n".format(range_id))
        #    else:
        #        return GLOBAL_CACHE[range_id]
        assert c0 > 0 and c1 >= c0 and r0 > 0 and r1 >= r0

        # convert from 1 based indexing w/ last index over last value to
        # 0-based w/ last index one past
        c0 -= 1
        r0 -= 1

        nc = c1 - c0
        nr = r1 - r0

        self.cbounds_stack.append((c0, r0, c1, r1, nc, nr))

        return self.cbounds_stack[-1]

    def cbounds(self):
        return self.cbounds_stack[-1]

    def __len__(self):
        _, _, _, _, nc, nr = self.cbounds()
        return nc * nr

    def equal_dimensions(self, other):
        return self.nrow() == other.nrow() and self.ncol() == other.ncol()

    def check_compat(self, other):
        assert self.nrow() == other.nrow()
        assert self.ncol() == other.ncol()
        return True

    def to_rowcol(self):
        ws = self.worksheet
        c0, r0, c1, r1, nc, nr = self.cbounds()
        rowcol = [x[:] for x in [[None] * nc] * nr]
        for ridx in xrange(nr):
            for cidx in xrange(nc):
                rowcol[ridx][cidx] = ws.get_cell(
                    c0 + cidx + 1, r0 + ridx + 1, False)
        return rowcol

    def flatten(self, do_eval=True):
        ncol, nrow = self.cbounds()[-2:]
        n = ncol * nrow
        return [self.get_cell_relative(i % ncol, i / ncol, do_eval) for i in xrange(ncol * nrow)]

    def get_cell1d(self, i, do_eval=True):
        c0, r0, c1, r1, nc, nr = self.cbounds()
        row, col = divmod(i, nc)
        cell = self.worksheet.get_cell(col + c0 + 1, row + r0 + 1, do_eval)
        return cell

    def nrow(self):
        return self.cbounds()[-1]

    def ncol(self):
        return self.cbounds()[-2]

    def get_cell(self, col, row, do_eval=True):
        cell = self.worksheet.get_cell(col, row, do_eval)
        return cell

    def get_cell_relative(self, col, row, do_eval=True):
        c0, r0, c1, r1, nc, nr = self.cbounds()
        cell = self.worksheet.get_cell(col + c0 + 1, row + r0 + 1, do_eval)
        return cell

    def flatten_and_discard(self, do_eval=True):
        c0, r0, c1, r1, ncol, nrow = self.cbounds()
        n = ncol * nrow
        c0 += 1
        r0 += 1
        get_ws_cell = self.worksheet.get_cell
        result = [get_ws_cell(c0 + i % ncol, r0 + i / ncol, do_eval)
                  for i in xrange(ncol * nrow)]
        result = [v for v in result if v is not None]
        return result


def rusage(msg=""):
    from resource import getrusage, RUSAGE_SELF
    rusage = getrusage(RUSAGE_SELF)
    print "\\n".join('"rusage","{}",{}'.format(msg,','.join(['"{}"'.format(r) for r in rusage])).split("\n"))

class Worksheet(object):

    def __init__(self, title, *args):
        print "Worksheet {}".format(title)
        rusage("Worksheet {}".format(title))
        

        self.title = title
        self.minrow = 1000000
        self.maxrow = 1
        self.mincol = 1000000
        self.maxcol = 1
        self.icells = {}

    def __getattr__(self, key):
        col, row = name_to_colrow(key)
        assert col >= 1
        assert row >= 1
        # print "<NOERR> key not found: {}.{}".format(self.title, key)
        return EMPTYCELL

    def __call__(self, c0, r0, c1, r1):

        if DOCACHE:
            range_id = "'{}'!{}{}:{}{}".format(
                self.title, col_letter(c0), r0, col_letter(c1), r1)
            if range_id in GLOBAL_CACHE:
                return GLOBAL_CACHE[range_id]

        rangeo = Range(self, c0, r0, c1, r1)
        val = rangeo  # val = rangeo.to_rowcol()

        if DOCACHE:
            GLOBAL_CACHE[range_id] = val

        return val

    def get_cell(self, col, row, do_eval):
        cell = self.icells.get((col, row))
        if cell is None:
            return None

        if do_eval:
            return cell()
        
        return cell.__call__


def stringrep(val, xlat_double_quotes=False):
    if val is None:
        return ""

    if isinstance(val, str):
        if xlat_double_quotes:
            return val.replace('"', "'")

        return val

    if isinstance(val, bool):
        return "TRUE" if val else "FALSE"

    if isinstance(val, XLDate):
        return val.to_string()

    if isinstance(val, datetime.datetime):
        return datetime_string(val)

    return "{}".format(val)

import sys
def register_cell_class_to_worksheet(worksheet):

    def attach_to_worksheet(cell_class):
        name = cell_class.__name__
        col, row = name_to_colrow(name)
        # key = (col, row, worksheet.title) #"{}_{}".format(worksheet.title,
        # name)

        fn = getattr(cell_class, name, None)
        formula = getattr(cell_class, "formula", None)

        def evaluate(self):
            if not DOCACHE or cell_class.cache_generation:
                if row > 550 and row < 553 and col > 57:
                    sys.stderr.write("CACHED {}={}\n".format(name, cell_class.cache_value))
                return cell_class.cache_value


            if row > 550 and row < 553 and col > 57:
                sys.stderr.write("NOT CACHED {}  cache_gen={}   cache_val={}   formula={}\n".format(name, name, name, name)) # cell_class.cache_generation, cell_class.cache_value, cell_cache.formula))
            cell_class.cache_value = fn()
            if cell_class.cache_value is None:
                cell_class.cache_value = 0
            cell_class.cache_generation += 1

            return cell_class.cache_value

        def fnstr(self):
            # fn = getattr(clazz, "formula", None)
            return "\n".join([s.strip() for s in inspect.getsourcelines(fn)[0]])

        def reprfn(self):
            # fn = getattr(clazz, "formula", None)
            fn = "" if formula is None else " fn={}".format(formula)
            return "<{} v={}{}>".format(name, cell_class.value, fn)

        def evalfn(self, return_formula=True):
            value = self.__call__()
            if return_formula:
                formula = getattr(cell_class, 'formula', None)
                if formula is not None:
                    return formula

            if getattr(self, 'isdatetime', False):
                value = excel_to_datetime(value)

            return value
            
        def setcachefn(self, value, isdatetime):
            cell_class.cache_value = value
            cell_class.value = value
            cell_class.cache_generation += 1
            if hasattr(cell_class, 'formula'):
                # sys.stderr.write("delformula {}".format(name))
                delattr(cell_class, 'formula')
            


        def cclass(self):
            return cell_class

        setattr(cell_class, "formula", formula)
        setattr(cell_class, "fnstr", fnstr)
        setattr(cell_class, "__call__", evaluate)
        setattr(cell_class, "__repr__", reprfn)
        setattr(cell_class, "evaluate", evalfn)
        setattr(cell_class, "cclass", cclass)
        setattr(cell_class, "setcache", setcachefn)
        if fn is None:
            setattr(cell_class, "cache_generation", 1)
            setattr(cell_class, "cache_value", cell_class.value)
        else:
            setattr(cell_class, "cache_generation", 0)

        cell_instance = cell_class()
        worksheet.icells[(col, row)] = cell_instance
        setattr(worksheet, name, cell_instance)

        worksheet.minrow = min(worksheet.minrow, row)
        worksheet.maxrow = max(worksheet.maxrow, row)
        worksheet.mincol = min(worksheet.mincol, col)
        worksheet.maxcol = max(worksheet.maxcol, col)

        return cell_class

    return attach_to_worksheet

register = register_cell_class_to_worksheet


@excel_fn_decorator
def CONCATENATE(*args):
    # token = { "CONCATENATE" : "CONCATENATE" }
    return concat(*args)


@excel_fn_decorator
def ISTEXT(val):
    return isinstance(val, basestring)


# https://support.office.com/en-us/article/INDEX-function-a5dcf0dd-996d-40a4-a822-b56b061328bd
@excel_fn_decorator
def INDEX(val_range, row_num, col_num):
    # token = { "INDEX" : "INDEX" }
    if ISERROR(val_range):
        return val_range
    if ISERROR(row_num):
        return row_num
    if ISERROR(col_num):
        return col_num

    row = py_toint(row_num)
    col = py_toint(col_num)
    if DEBUG:
        print "INDEX {} {} {}".format(val_range, row, col)
    if ISERROR(row) or row < 1:
        return row
    if ISERROR(col) or col < 1:
        return col
    # if row > val_range.nrow(): raise ValueError("ROW>nrow INDEX {} {} {} {}".format(val_range, row, col, val_range.cbounds())) #ERRREF #return ERRREF
    # if col > val_range.ncol(): raise ValueError("COL>ncol INDEX {} {} {}
    # {}".format(val_range, row, col, val_range.cbounds())) #ERRREF #return
    if row > val_range.nrow():
        return ERRREF
    if col > val_range.ncol():
        return ERRREF

    val = val_range.get_cell_relative(col - 1, row - 1)
    return val


@excel_fn_decorator
def SUMIF(eval_range, criteria, sum_range):
    # token = { "SUMIF" : "SUMIF" }
    eval_range.check_compat(sum_range)
    values = [sum_range.get_cell1d(i)
              for i, val in enumerate(eval_range.flatten()) if equal(val, criteria)]
    result = reduce(add, values, 0)
    return result

# https://support.office.com/en-us/article/AVERAGEIF-function-faec8e2e-0dec-4308-af69-f5576d8ac642


@excel_fn_decorator
def AVERAGEIF(eval_range, criteria, average_range=None):
    if average_range is None:
        average_range = eval_range
    eval_range.check_compat(average_range)
    values = [average_range.get_cell1d(i)
              for i, val in enumerate(eval_range.flatten()) if equal(val, criteria)]
    if not values:
        return ERRDIV0
    result = reduce(add, values)
    result = result if ISERROR(result) else result / float(len(values))
    return result


@excel_fn_decorator
def SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2=None, criteria2=None, criteria_range3=None, criteria3=None):
    # token = { "SUMIF" : "SUMIF" }
    sum_range.check_compat(criteria_range1)

    n = len(sum_range)
    assert n == len(criteria_range1), "lensum={}, lencrit={}, n={}".format(
        len(sum_range), len(criteria_range1), n)

    ranges_to_trim = [sum_range, criteria_range1]
    if criteria_range2 is not None:
        ranges_to_trim.append(criteria_range2)

    if criteria_range3 is not None:
        ranges_to_trim.append(criteria_range3)

    trim_ranges(ranges_to_trim)

    crits = [(criteria_range1, criteria1)]
    if criteria2 is not None:
        crits.append((criteria_range2, criteria2))

    if criteria3 is not None:
        crits.append((criteria_range3, criteria3))

    vals = [0] * n
    for i in range(n):
        fail = False
        for crange, rhs in crits:
            lhs = crange.get_cell1d(i)
            if lhs is None or not equal(lhs, rhs):
                fail = True
                break

        if not fail:
            vals[i] = sum_range.get_cell1d(i)

    for r in ranges_to_trim:
        r.pop_bounds()

    # vals = [0 if not flag else sum_range.get_cell1d(i) for i,flag in
    # enumerate(flags)]
    result = reduce(add, vals, 0)
    return result


@excel_fn_decorator
def MAX(*args):
    # token = { "MAX" : "MAX" }
    vals = flatten_args(*args)
    for v in vals:
        if ISERROR(v):
            return v
    vals = map(float, vals)
    if not vals:
        return 0
    return max(vals)


@excel_fn_decorator
def NA():
    # token = { "NA" : "NA" }
    return ERRNA


@excel_fn_decorator
def IFERROR(value, value_if_error=None):
    assert not isrange(value)
    if ISERROR(value):
        return value_if_error
    return value


# https://support.office.com/en-us/article/VLOOKUP-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1
@excel_fn_decorator
def VLOOKUP(lookup_value, table_range, col_index_num, range_lookup):
    token = {"VLOOKUP": "VLOOKUP"}
    assert range_lookup == "FALSE" or int(range_lookup) == 0, "VLOOKUP({}, {}, {}, {})".format(
        lookup_value, table_range, col_index_num, range_lookup)

    if col_index_num > table_range.ncol():
        return ERRREF

    str_lookup_value = str(lookup_value)
    col_index = int(col_index_num) - 1
    for rowidx in xrange(table_range.nrow()):
        potential_val = table_range.get_cell_relative(0, rowidx)
        potential_val = None if potential_val is None else str(potential_val)
        isequal = equal(potential_val, str_lookup_value)
        if DEBUG:
            print 'searching "{}" for "{}", equal={}'.format(potential_val, str_lookup_value, isequal)

        if isequal:
            val = table_range.get_cell_relative(col_index, rowidx)
            val = 0 if val is None else val
            if DEBUG:
                print "found {}".format(val)
            # raise ValueError("VLOOKUP Found {} in cell {}
            # value={}".format(str_lookup_value, row[0].name, val))
            return val

    return ERRNA


# https://support.office.com/en-us/article/HLOOKUP-function-a3034eec-b719-4ba3-bb65-e1ad662ed95f
@excel_fn_decorator
def HLOOKUP(lookup_value, table_range, row_index_num, range_lookup):
    token = {"VLOOKUP": "VLOOKUP"}
    assert range_lookup == "FALSE" or int(range_lookup) == 0, "VLOOKUP({}, {}, {}, {})".format(
        lookup_value, table_range, col_index_num, range_lookup)
    str_lookup_value = str(lookup_value)
    row_index = int(row_index_num) - 1
    for idx in xrange(table_range.ncol()):
        potential_val = table_range.get_cell_relative(idx, 0)
        potential_val = None if potential_val is None else str(potential_val)
        isequal = equal(potential_val, str_lookup_value)
        if DEBUG:
            print 'searching "{}" for "{}", equal={}'.format(potential_val, str_lookup_value, isequal)

        if isequal:
            val = table_range.get_cell_relative(idx, row_index)
            val = 0 if val is None else val
            if DEBUG:
                print "found {}".format(val)
            # raise ValueError("VLOOKUP Found {} in cell {}
            # value={}".format(str_lookup_value, row[0].name, val))
            return val

    return ERRNA

# https://support.office.com/en-US/article/COUNT-function-A59CD7FC-B623-4D93-87A4-D23BF411294C


@excel_fn_decorator
def COUNT(*args):
    vals = flatten_args(*args)
    vals = [val for val in vals if not(isinstance(val, str) and val == "")]
    return len(vals)

# https://support.office.com/en-us/article/AVERAGE-function-047bac88-d466-426c-a32b-8f33eb960cf6


@excel_fn_decorator
def AVERAGE(*args):
    # token = { "AVERAGE" : "AVERAGE" }
    vals = flatten_args(*args)
    vals = [val for val in vals if type(val) in NUMBER_TYPES]

    if not vals:
        return ERRDIV0
    result = reduce(add, vals, 0) / float(len(vals))
    return result


@excel_fn_decorator
def ISERROR(val):
    return val in ERRTYPES


@excel_fn_decorator
def ISERR(val):
    return val in (ERRDIV0, ERRNAME, ERRNULL, ERRNUM, ERRREF, ERRVALUE) or isinstance(val, ERR_class)


@excel_fn_decorator
def ISNA(val):
    return val == ERRNA


@excel_fn_decorator
def ABS(v):
    v = py_tofloat(v)
    if ISERROR(v):
        return v
    v = abs(v)
    return v


def excel_to_time_tuple(value):
    if ISERROR(value):
        return [value] * 9

    if not isinstance(value, int) and not isinstance(value, float):
        return None

    if value < 0:
        return [ERRNUM] * 9

    leapyearbug = 60 <= value < 61
    day0 = 0 <= value < 1

    if value < 61:
        value += 1

    value = value + \
        EXCEL_EPOCH_OFFSET_FROM_UNIX_EPOCH_IN_DAYS  # Shift date from XL to Unix epoch
    value = value * SECONDS_PER_DAY
    time_tuple = list(time.gmtime(value))

    if leapyearbug:
        time_tuple[1] = 2
        time_tuple[2] = 29
    if day0:
        time_tuple[0] = 1900
        time_tuple[1] = 1
        time_tuple[2] = 0

    return time_tuple


def excel_to_datetime(value):
    t = excel_to_time_tuple(value)
    return datetime.datetime(t[0], t[1], t[2], t[3], t[4], t[5])


def excel_to_datetime_string(value):
    time_tuple = excel_to_time_tuple(value)
    return timetuple_string(time_tuple)


def datetime_string(value):
    return timetuple_string(value.timetuple())


def timetuple_string(time_tuple, full_iso8601=True):
    ftime = "%Y-%m-%d"
    if full_iso8601 or any(time_tuple[3:6]):
        ftime += " %H:%M:%S"
    return time.strftime(ftime, time_tuple)


@excel_fn_decorator
def YEAR(value):
    ttuple = excel_to_time_tuple(value)
    if ttuple:
        return ttuple[0]

    tmp = str(value)[:4]
    val = py_toint(tmp)
    return val


@excel_fn_decorator
def MONTH(value):
    ttuple = excel_to_time_tuple(value)
    if ttuple:
        return ttuple[1]

    tmp = str(value)[5:7]
    val = py_toint(tmp)
    return val


@excel_fn_decorator
def DAY(value):
    ttuple = excel_to_time_tuple(value)
    if ttuple:
        return ttuple[2]

    tmp = str(value)[8:10]
    val = py_toint(tmp)
    return val


@excel_fn_decorator
def DATE(year, month, day, hour=0, minute=0, second=0):
    struct_time = time.struct_time(
        (int(year), int(month), int(day), int(hour), int(minute), int(second), 0, 0, 0))
    timestamp = struct_time_to_timestamp(struct_time)
    timestamp = timestamp / SECONDS_PER_DAY
    timestamp = timestamp - EXCEL_EPOCH_OFFSET_FROM_UNIX_EPOCH_IN_DAYS
    return timestamp


@excel_fn_decorator
def SUMPRODUCT(*args):
    # token = { "SUMPRODUCT" : "SUMPRODUCT" }

    ranges = [arg.flatten() for arg in args]
    if DEBUG:
        print ranges

    products = [reduce(mult, vals) for vals in zip(*ranges)]
    if DEBUG:
        print products

    result = reduce(add, products, 0)
    if DEBUG:
        print result

    return result


@excel_fn_decorator
def SUM(*args):
    # token = { "SUM" : "SUM" }
    vals = flatten_args(*args)
    result = reduce(add, vals, 0)
    return result

# https://support.office.com/en-US/article/MATCH-function-E8DFFD45-C762-47D6-BF89-533F4A37673A
# TODO: Default match_type should be 1, not implemented


@excel_fn_decorator
def MATCH(lookup_value, lookup_range, match_type=0):
    # token = { "MATCH" : "MATCH" }
    assert match_type == 0
    # assert isrange(lookup_range)

    if DEBUG:
        print "MATCH {} {}".format(lookup_range, lookup_value)
    n = len(lookup_range)
    for i in xrange(n):
        if equal(lookup_range.get_cell1d(i), lookup_value):
            return i + 1

    return ERRNA


@excel_fn_decorator
def COLUMN(column_range):
    return column_range.obounds[0]


@excel_fn_decorator
def ROW(row_range):
    return row_range.obounds[1]


def py_predicate(val):
    if isinstance(val, int):
        return val != 0
    elif isinstance(val, float):
        return val != 0.0
    return ERRVALUE


def OR(v1, v2):
    v1 = py_predicate(v1)
    if v1:
        return True

    v2 = py_predicate(v2)
    if v2:
        return True

    if ISERROR(v1):
        return v1
    if ISERROR(v2):
        return v2
    return False


@excel_fn_decorator
def IF(val, trueval, falseval):
    if ISERROR(val):
        return val
    if isinstance(val, int):
        predicate = val != 0
    elif isinstance(val, float):
        predicate = val != 0.0
    elif isinstance(val, str):
        predicate = val != '0' and val != 'FALSE'

    if predicate is not None:
        return trueval if predicate else falseval

    assert False, "IF({}) unhandled".format(val)
    return falseval


mapping = {
    "CONCATENATE": CONCATENATE,
    "INDEX": INDEX,
    "SUMIFS": SUMIFS,
    "MAX": MAX,
    "NA": NA,
    "IFERROR": IFERROR,
    "VLOOKUP": VLOOKUP,
    "COUNT": COUNT,
    "AVERAGE": AVERAGE,
    "ISERROR": ISERROR,
    "ABS": ABS,
    "SUMIF": SUMIF,
    "YEAR": YEAR,
    "ISERR": ISERR,
    "SUMPRODUCT": SUMPRODUCT,
    "SUM": SUM,
    "MATCH": MATCH,
    "IF": IF,
}


def isrange(val):
    return isinstance(val, list) and len(val) > 0 and isinstance(val[0], list) and len(val[0]) > 0


def flatten_args(*args):
    result = []
    for arg in args:
        if isinstance(arg, Range):
            result += arg.flatten_and_discard()
        elif arg is not None:
            result.append(arg)

    return result


def excel_fn_op_decorator(fn_op):
    def setup_args(lhs, rhs):
        lhs = py_tofloat(lhs)
        # lhs = 0 if lhs is None else lhs
        if lhs is None or isinstance(lhs, ERR_class): # ISERROR(lhs):
            return lhs

        rhs = py_tofloat(rhs)
        # rhs = 0 if rhs is None else rhs
        if rhs is None or isinstance(rhs, ERR_class): # ISERROR(lhs):
            return rhs

        return fn_op(lhs, rhs)

    return setup_args


# generated by: print_template(, "Counter({'=': 51216, '*': 40814, '/':
# 14521, '+': 8504, '-': 935, '<': 136, '&': 63})", "")
@excel_fn_decorator
def concat(*args):
    strs = flatten_args(*args)
    for arg in strs:
        if ISERROR(arg):
            return arg
    strs = [str(py_maybeint(arg)) for arg in strs]
    result = "".join(strs)
    return result


@excel_fn_decorator
def equal(lhs, rhs):
    if lhs is None or rhs is None:
        return False

    if isinstance(lhs, str) and isinstance(rhs, str):
        return lhs.lower() == rhs.lower()

    return lhs == rhs


@excel_fn_op_decorator
@excel_fn_decorator
def add(lhs, rhs):
    # token = { "+" : "add" }
    result = lhs + rhs
    return result


@excel_fn_op_decorator
@excel_fn_decorator
def mult(lhs, rhs):
    # token = { "*" : "mult" }
    result = lhs * rhs
    return result


@excel_fn_op_decorator
@excel_fn_decorator
def sub(lhs, rhs):
    # token = { "-" : "sub" }
    result = lhs - rhs
    return result


@excel_fn_op_decorator
@excel_fn_decorator
def lessthan(lhs, rhs):
    # token = { "<" : "lessthan" }
    result = 1 if lhs < rhs else 0
    return result


@excel_fn_op_decorator
@excel_fn_decorator
def greaterthan(lhs, rhs):
    # token = { ">" : "lessthan" }
    result = 1 if lhs > rhs else 0
    return result


@excel_fn_op_decorator
@excel_fn_decorator
def divide(lhs, rhs):
    # token = { "/" : "divide" }
    if rhs == 0:
        return ERRDIV0

    if ISERROR(lhs) or ISERROR(rhs):
        return ERRNUM

    result = float(lhs) / float(rhs)
    return result


@excel_fn_decorator
def SQRT(val):
    val = py_tofloat(val)
    # rhs = 0 if rhs is None else rhs
    if ISERROR(val):
        return val

    return pow(val, 0.5)


@excel_fn_decorator
def POW(val, exp):
    val = py_tofloat(val)
    if ISERROR(val):
        return val

    exp = py_tofloat(exp)
    if ISERROR(exp):
        return exp

    return pow(val, exp)


# https://support.office.com/en-us/article/CORREL-function-995dcef7-0c0a-4bed-a3fb-239d7b68ca92
@excel_fn_decorator
def CORREL(array1, array2):
    if not array1.equal_dimensions(array2):
        return ERRNA

    xy = zip(array1.flatten(), array2.flatten())

    for x, y in xy:
        if x is not None and ISERROR(x):
            return x
        if y is not None and ISERROR(y):
            return y

    xy = [(x, y)
          for (x, y) in xy if type(x) in NUMBER_TYPES and type(y) in NUMBER_TYPES]

    n = len(xy)
    if not n:
        return ERRDIV0

    xbar = sum([x for x, y in xy]) / n
    ybar = sum([y for x, y in xy]) / n

    deviations = [(x - xbar, y - ybar) for x, y in xy]

    sumxy = sum([x * y for x, y in deviations])
    sumxx = sum([x * x for x, y in deviations])
    sumyy = sum([y * y for x, y in deviations])

    denom = pow(sumxx * sumyy, 0.5)

    if denom == 0.0:
        return ERRDIV0

    result = sumxy / denom

    return result


@excel_fn_decorator
def FIND(find_text, within_text, start_num=1):
    within_text = str(within_text).lower()
    find_text = str(find_text).lower()
    pos = within_text.find(find_text) + 1
    return pos if pos else ERRVALUE


@excel_fn_decorator
def COUNTIF(count_range, criteria):
    count = 0
    criteria = str(criteria).lower()
    for i in xrange(len(count_range)):
        val = count_range.get_cell1d(i)
        if ISERROR(val):
            return val
        if str(val).lower() == criteria:
            count += 1
    return count

# https://support.office.com/en-us/article/mid-midb-functions-d5f9e25c-d7d6-472e-b568-4ecb12433028
@excel_fn_decorator
def MID(text, start_num, num_chars):
    return text[start_num-1:start_num-1+num_chars]

# https://support.office.com/en-us/article/formulatext-function-0a786771-54fd-4ae2-96ee-09cda35439c8
@excel_fn_decorator
def FORMULATEXT(text):
    return '' if text is None else str(text)

# https://support.office.com/en-us/article/AVERAGEIFS-function-48910c45-1fc0-4389-a028-f7c5c3001690
'''
@excel_fn_decorator
def AVERAGEIFS(average_range, criteria_range1, criteria1):
    average_range.check_compat(criteria_range)

    criterias = criteria_range1.flatten()
    values = [average_range.get_cell1d(i) for i,val in enumerate(eval_range.flatten()) if equal(val, criteria)]
    if not values:
        return ERRDIV0
    result = reduce(add, values) / float(len(values))



    values = [average_range.get_cell1d(i) for i,val in enumerate(eval_range.flatten()) if equal(val, criteria)]
    if not values:
        return ERRDIV0
    result = reduce(add, values) / float(len(values))
    return result
'''
