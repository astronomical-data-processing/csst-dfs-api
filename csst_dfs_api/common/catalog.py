from astropy.table import QTable, Table, Column

from .delegate import Delegate
from csst_dfs_commons.models import Result


class CatalogApi(object):
    def __init__(self):
        self.module = Delegate().load(sub_module = "common")
        self.stub = getattr(self.module, "CatalogApi")()
    
    def catalog_query(self, ra: float, dec: float, radius: float, catalog_name: str, min_mag: float,  max_mag: float,  obstime: int, limit: int):
        ''' retrieval catalog

        :param ra: in deg
        :param dec:  in deg
        :param radius:  in deg
        :param catalog_name: one of ['gaia3','','']
        :param min_mag: minimal magnitude
        :param max_mag: maximal magnitude
        :param obstime: seconds  
        :param limit: limits returns the number of records

        :returns: csst_dfs_common.models.Result
        '''

        if catalog_name == "gaia3":
            return self.gaia3_query(ra, dec, radius, min_mag, max_mag, obstime, limit)
        else:
            return Result.error(message="%s catalog search not yet implemented" %(catalog_name, ))
    def _fields_dtypes(self, rec):
        fields = tuple(rec.__dataclass_fields__.keys())
        dtypes = []
        for _, f in rec.__dataclass_fields__.items():
            if f.type == int:
                dtypes.append('i8')
            if f.type == float:
                dtypes.append('f8')        
            if f.type == str:
                dtypes.append('S2')        
        dtypes = tuple(dtypes)
        return fields, dtypes

    def to_table(self, query_result):
        if not query_result.success or not query_result.data:
            return Table()
        fields, dtypes = self._fields_dtypes(query_result.data[0])
        t = Table(names = fields, dtype = dtypes)
        for rec in query_result.data:
            t.add_row(tuple([rec.__getattribute__(k) for k in fields]))
        return t

    def gaia3_query(self, ra: float, dec: float, radius: float, min_mag: float,  max_mag: float,  obstime: int, limit: int):
        """retrieval GAIA EDR 3
        
        :param ra: in deg
        :param dec:  in deg
        :param radius:  in deg
        :param min_mag: minimal magnitude
        :param max_mag: maximal magnitude
        :param obstime: seconds  
        :param limit: limits returns the number of records

        :returns: csst_dfs_common.models.Result
        """ 
        try:
            return self.stub.gaia3_query(ra, dec, radius, min_mag, max_mag, obstime, limit)
        except Exception as e:
            return Result.error(message=repr(e))
