from .delegate import Delegate
class CatalogApi(object):
    def __init__(self):
        self.module = Delegate().load(sub_module = "common")
        self.stub = getattr(self.module, "CatalogApi")()
    
    def catalog_query(self, ra: float, dec: float, radius: float, catalog_name: str, min_mag: float,  max_mag: float,  obstime: int, limit: int):
        ''' retrieval catalot
            args:
                ra:  in deg
                dec:  in deg
                radius:  in deg
                catalog_name: one of ['gaia3','','']
                min_mag: minimal magnitude
                max_mag: maximal magnitude
                obstime: seconds  
                limit: limits returns the number of records
            return: a dict as {success: true, totalCount: 100, records:[.....]}   
        '''

        if catalog_name == "gaia3":
            return self.gaia3_query(ra, dec, radius, min_mag, max_mag, obstime, limit)
        else:
            raise Exception("%s catalog search not yet implemented" %(catalog_name, ))

    def gaia3_query(self, ra: float, dec: float, radius: float, min_mag: float,  max_mag: float,  obstime: int, limit: int):
        ''' retrieval GAIA DR 3
            args:
                ra:  in deg
                dec:  in deg
                radius:  in deg
                min_mag: minimal magnitude
                max_mag: maximal magnitude
                obstime: seconds  
                limit: limits returns the number of records
            return: a dict as {success: true, totalCount: 100, records:[.....]}
        ''' 
        return self.stub.gaia3_query(ra, dec, radius, min_mag, max_mag, obstime, limit)    

