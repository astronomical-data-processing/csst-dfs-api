
from ..common.delegate import Delegate

class Level0PrcApi(object):
    """
    Level 0 Data Operation API
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "cpic")
        self.stub = getattr(self.pymodule, "Level0PrcApi")()
        
    def find(self, **kwargs):
        ''' retrieve level0 procedure records from database

        :param kwargs: Parameter dictionary, key items support:
            level0_id: [str]
            pipeline_id: [str]
            prc_module: [str]
            prc_status : [int]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def update_proc_status(self, **kwargs):
        ''' update the status of reduction

        :param kwargs: Parameter dictionary, key items support:
            id : [int],
            status : [int]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.update_proc_status(**kwargs)

    def write(self, **kwargs):
        ''' insert a level0 procedure record into database
 
        :param kwargs: Parameter dictionary, key items support:
            level0_id : [str]
            pipeline_id : [str]
            prc_module : [str]
            params_file_path : [str]
            prc_status : [int]
            prc_time : [str]
            result_file_path : [str]
        
        :returns: csst_dfs_common.models.Result
        '''  
        return self.stub.write(**kwargs)

