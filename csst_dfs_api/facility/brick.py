
from ..common.delegate import Delegate

class BrickApi(object):
    """
    Brick Data Operation API
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "facility")
        self.stub = getattr(self.pymodule, "BrickApi")()
        
    def find(self, **kwargs):
        ''' retrieve brick records from database

        :param kwargs: Parameter dictionary, support:
            limit: limits returns the number of records,default 0:no-limit

        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def get(self, **kwargs):
        '''  fetch a record from database

        :param kwargs: Parameter dictionary, key items support:
            id : [int]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.get(**kwargs)

    def write(self, **kwargs):
        ''' insert a brick data record into database
 
        :param kwargs: Parameter dictionary, key items support:
            ra = [float]\n
            dec = [float]\n
            boundingbox = [str]
        
        :returns: csst_dfs_common.models.Result
        '''  
        return self.stub.write(**kwargs)

    def find_obs_status(self, **kwargs):
        ''' find observation status of bricks

        :param kwargs: Parameter dictionary, support:
            brick_id = [int]\n
            band = [string]

        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find_obs_status(**kwargs)

    def find_level1_data(self, **kwargs):
        ''' find level1 data

        :param kwargs: Parameter dictionary, support:
            brick_id = [int]\n
            level1_id = [int]\n
            module = [str]       

        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find_level1_data(**kwargs)        