from .delegate import Delegate
from csst_dfs_commons.models import Result
from csst_dfs_api.common.utils import to_table as to_fits_table

class CatalogApi(object):
    def __init__(self):
        self.module = Delegate().load(sub_module = "common")
        self.stub = getattr(self.module, "CatalogApi")()
    
    def catalog_query(self, ra: float, dec: float, radius: float, catalog_name: str, columns: tuple, min_mag: float,  max_mag: float,  obstime: int, limit: int):
        ''' retrieval catalog

        :param ra: in deg
        :param dec:  in deg
        :param radius:  in deg
        :param catalog_name: one of ['gaia3','','']
        :param columns: tuple of str, like ('ra','dec','phot_g_mean_mag')
        :param min_mag: minimal magnitude
        :param max_mag: maximal magnitude
        :param obstime: seconds  
        :param limit: limits returns the number of records

        :returns: csst_dfs_common.models.Result
        '''

        if catalog_name == "gaia3":
            return self.gaia3_query(ra, dec, radius, columns, min_mag, max_mag, obstime, limit)
        else:
            return Result.error(message="%s catalog search not yet implemented" %(catalog_name, ))

    def to_table(self, query_result):
        return to_fits_table(query_result)

    def gaia3_query(self, ra: float, dec: float, radius: float, columns: tuple,min_mag: float,  max_mag: float,  obstime: int, limit: int):
        """retrieval GAIA DR 3, all column name must be lowercase. columns specification at https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html

        :param ra: in deg
        :param dec:  in deg
        :param radius:  in deg
        :param columns: tuple of str, like ('ra','dec','phot_g_mean_mag')
        :param min_mag: minimal magnitude
        :param max_mag: maximal magnitude
        :param obstime: seconds  
        :param limit: limits returns the number of records

        :returns: csst_dfs_common.models.Result
        """ 
        try:
            if not columns:
                raise Exception("columns is empty")
            return self.stub.gaia3_query(ra, dec, radius, columns, min_mag, max_mag, obstime, limit)
        except Exception as e:
            return Result.error(message=repr(e))
