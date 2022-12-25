
from ..common.delegate import Delegate

class Level1PrcApi(object):
    """
    Level 0 Data Operation API
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "mci")
        self.stub = getattr(self.pymodule, "Level1PrcApi")()
        
    def find(self, **kwargs):
        ''' retrieve level1 procedure records from database

        :param kwargs: Parameter dictionary, key items support:
            level1_id: [int]
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
        ''' insert a level1 procedure record into database
 
        :param kwargs: Parameter dictionary, key items support:
            level1_id : [int]
            pipeline_id : [str]
            prc_module : [str]
            params_file_path : [str]
            prc_status : [int]
            prc_time : [str]
            result_file_path : [str]
        
        :returns: csst_dfs_common.models.Result
        '''  
        return self.stub.write(**kwargs)

