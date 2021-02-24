
from ..common.delegate import Delegate

class FitsApi(object):
    def __init__(self, sub_system="ifs"):
        self.sub_system = sub_system
        self.module = Delegate().load(sub_module = "ifs")
        self.stub = getattr(self.module, "FitsApi")()

    def find(self, **kwargs):
        '''
        parameter kwargs:
        obs_time = [str] 

        return list of fits_id
        '''
        return self.stub.find(**kwargs)

    def read(self, **kwargs):
        '''
        parameter kwargs:
        fits_id = [str] 
        
        yield bytes of fits file
        '''
        yield self.stub.read(**kwargs)

    def update_status(self, **kwargs):
        return self.stub.update_status(**kwargs)    

    def upload(self,**kwargs): 
        yield self.stub.upload(**kwargs)

