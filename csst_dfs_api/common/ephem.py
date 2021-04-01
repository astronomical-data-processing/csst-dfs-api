from .delegate import Delegate
class EphemSearchApi(object):
    def __init__(self):
        self.module = Delegate().load(sub_module = "common")
        self.stub = getattr(self.module, "EphemSearchApi")()
    
    def gaia_query(self, ra: float, dec: float, radius: float, mag: float, limit: int = 1000):
        ''' retivial GAIA DR 2
            args:
                ra:  in deg
                dec:  in deg
                radius:  in deg
                mag:  
                limit: limits on the number of returns
            return: a dict as {success: true, totalCount: 100, records:[.....]}
        ''' 
        return self.stub.gaia_query(ra, dec, radius, mag, limit)    

