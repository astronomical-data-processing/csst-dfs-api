
from ..common.delegate import Delegate

class Level0PrcApi(object):
    """
    Level 0 Data Operation API
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "facility")
        self.stub = getattr(self.pymodule, "Level0PrcApi")()
        
    def find(self, **kwargs):
        ''' retrieve level0 procedure records from database

        parameter kwargs:
            level0_id: [int]
            pipeline_id: [str]
            prc_module: [str]
            prc_status : [int]

        return: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def update_proc_status(self, **kwargs):
        ''' update the status of reduction

        parameter kwargs:
            id : [int],
            status : [int]

        return csst_dfs_common.models.Result
        '''
        return self.stub.update_proc_status(**kwargs)

    def write(self, **kwargs):
        ''' insert a level0 procedure record into database
 
        parameter kwargs:
            level0_id : [int]
            pipeline_id : [str]
            prc_module : [str]
            params_id : [str]
            prc_status : [int]
            prc_time : [str]
            file_path : [str]
        return csst_dfs_common.models.Result
        '''  
        return self.stub.write(**kwargs)

