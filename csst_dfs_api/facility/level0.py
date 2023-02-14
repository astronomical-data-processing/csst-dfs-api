
from ..common.delegate import Delegate

class Level0DataApi(object):
    """
    Level 0 Data Operation API
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "facility")
        self.stub = getattr(self.pymodule, "Level0DataApi")()
        
    def find(self, **kwargs):
        ''' retrieve level0 records from database

        :param kwargs: Parameter dictionary, key items support:
            obs_id: [str],
            module_id: [str]
            detector_no: [str],
            obs_type: [str],
            filter: [str],
            obs_time : (start, end),
            qc0_status : [int],
            prc_status : [int],
            file_name: [str],
            ra_obj: [float],
            dec_obj: [float],
            radius: [float],
            object_name: [str],
            version: [str],
            limit: limits returns the number of records,default 0:no-limit
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def find_by_brick_ids(self, **kwargs):
        ''' retrieve level0 records by brick_ids like [1,2,3,4]

        :param kwargs: Parameter dictionary, key items support:
            brick_ids: [list]
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find_by_brick_ids(**kwargs)
        
    def get(self, **kwargs):
        '''  fetch a record from database

        :param kwargs: Parameter dictionary, key items support:
            id : [int],
            level0_id: [str]
            obs_type: [str]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.get(**kwargs)

    def update_proc_status(self, **kwargs):
        ''' update the status of reduction

        :param kwargs: Parameter dictionary, key items support:
            id : [int],
            level0_id: [str],
            obs_type: [str],
            status : [int]
        
        :returns: csst_dfs_common.models.Result            
        '''
        return self.stub.update_proc_status(**kwargs)

    def update_qc0_status(self, **kwargs):
        ''' update the status of QC0
        
        :param kwargs: Parameter dictionary, key items support:
            id : [int],
            level0_id: [str],
            obs_type: [str],
            status : [int]
        
        :returns: csst_dfs_common.models.Result            
        '''        
        return self.stub.update_qc0_status(**kwargs)    

    def write(self, **kwargs):
        ''' insert a level0 data record into database
 
        :param kwargs: Parameter dictionary, key items support:
            obs_id = [str],
            detector_no = [str],
            obs_type = [str],    
            obs_time = [str],
            exp_time = [int],
            detector_status_id = [int],
            filename = [str],
            file_path = [str]
        
        :returns: csst_dfs_common.models.Result
        '''  
        return self.stub.write(**kwargs)

