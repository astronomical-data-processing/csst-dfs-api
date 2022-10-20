
from ..common.delegate import Delegate

class Level0DataApi(object):
    """
    Level 0 Data Operation API
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "mci")
        self.stub = getattr(self.pymodule, "Level0DataApi")()
        
    def find(self, **kwargs):
        ''' retrieve level0 records from database

        :param kwargs: Parameter dictionary, key items support:
            obs_id: [str],
            detector_no: [str],
            obs_type: [str],
            object_name: [str],
            obs_time : (start, end),
            qc0_status : [int],
            prc_status : [int],
            file_name: [str],
            version: [str],
            ra_obj: [float],
            dec_obj: [float],
            radius: [float],            
            limit: limits returns the number of records,default 0:no-limit
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def get(self, **kwargs):
        '''  fetch a record from database

        :param kwargs: Parameter dictionary, key items support:
            id : [int],
            level0_id: [str]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.get(**kwargs)

    def update_proc_status(self, **kwargs):
        ''' update the status of reduction

        :param kwargs: Parameter dictionary, key items support:
            id : [int],
            level0_id: [str],
            status : [int]
        
        :returns: csst_dfs_common.models.Result            
        '''
        return self.stub.update_proc_status(**kwargs)

    def update_qc0_status(self, **kwargs):
        ''' update the status of QC0
        
        :param kwargs: Parameter dictionary, key items support:
            id : [int],
            level0_id: [str],
            status : [int]
        
        :returns: csst_dfs_common.models.Result            
        '''        
        return self.stub.update_qc0_status(**kwargs)    

    def write(self, **kwargs):
        ''' insert a level0 data record into database
 
        :param kwargs: Parameter dictionary, key items support:

            file_path = [str],
            copyfiles = [boolean]
        
        :returns: csst_dfs_common.models.Result
        '''  
        return self.stub.write(**kwargs)

