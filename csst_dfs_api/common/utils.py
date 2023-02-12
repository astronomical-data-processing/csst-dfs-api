from datetime import datetime
from astropy.table import Table
import time

from .delegate import Delegate

def format_datetime(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def format_date(dt):
    return dt.strftime('%Y-%m-%d')

def format_time_ms(float_time):
    local_time = time.localtime(float_time)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (float_time - int(float_time)) * 1000
    return "%s.%03d" % (data_head, data_secs)

def get_parameter(kwargs, key, default=None):
    """ Get a specified named value for this (calling) function

    The parameter is searched for in kwargs

    :param kwargs: Parameter dictionary
    :param key: Key e.g. 'max_workers'
    :param default: Default value
    :return: result
    """

    if kwargs is None:
        return default

    value = default
    if key in kwargs.keys():
        value = kwargs[key]
    return value
    
def to_int(s, default_value = 0):
    try:
        return int(s)
    except:
        return default_value

def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner

def revoke(cmd, desc=''):
    def decorator(func):
        class Wrapper:
            def __init__(self, cmd, desc, func) -> None:
                self.cmd = cmd
                self.func = func
            def __str__(self) -> str:
                return "cmd"
            def __call__(self, *args, **kw):
                return self.func(*args, **kw)
        return Wrapper(cmd, desc, func)
    return decorator

def fields_dtypes(rec):
    fields = tuple(rec.__dataclass_fields__.keys())
    dtypes = []
    for _, f in rec.__dataclass_fields__.items():
        if f.type == int:
            dtypes.append('i8')
        elif f.type == float:
            dtypes.append('f8')        
        elif f.type == str:
            dtypes.append('S2')
        elif f.type == list:
            dtypes.append('(12,)f8')       
        else:
            dtypes.append('S2')                
    dtypes = tuple(dtypes)
    return fields, dtypes

def tuple_fields_dtypes(rec: tuple):
    dtypes = []
    for f in rec:
        if type(f) == int:
            dtypes.append('i8')
        elif type(f) == float:
            dtypes.append('f8')        
        elif type(f) == str:
            dtypes.append('S2')
        elif type(f) == list:
            dtypes.append('(12,)f8')       
        else:
            dtypes.append('S2')                
    dtypes = tuple(dtypes)
    return dtypes

def to_table(query_result):
    if not query_result.success or not query_result.data:
        return Table()
    fields = query_result['columns']
    dtypes = tuple_fields_dtypes(query_result.data[0])
    t = Table(names = fields, dtype = dtypes, rows = query_result.data)
    t.meta['columns'] = fields
    t.meta['total'] = query_result['totalCount']

    return t

def object_list_to_table(query_result):
    if not query_result.success or not query_result.data:
        return Table()
    fields, dtypes = fields_dtypes(query_result.data[0])
    t = Table(names = fields, dtype = dtypes)
    t.meta['comments'] = [str(query_result.data[0].__class__)]
    t.meta['total'] = query_result['totalCount']

    for rec in query_result.data:
        t.add_row(tuple([rec.__getattribute__(k) for k in fields]))
    return t

def get_nextId_by_prefix(prefix):
    pymodule = Delegate().load(sub_module = "common.utils")
    return getattr(pymodule, "get_nextId_by_prefix")(prefix)