
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

        Args:
            obs_id: [int]
            detector_no: [str]
            obs_type: [str]
            obs_time : (start, end),
            qc0_status : [int],
            prc_status : [int],
            file_name: [str]
            limit: limits returns the number of records,default 0:no-limit
        Returns:
            csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def get(self, **kwargs):
        '''  fetch a record from database

        Args:
            fits_id : [int] 
        Returns:
            csst_dfs_common.models.Result
        '''
        return self.stub.get(**kwargs)

    def update_proc_status(self, **kwargs):
        ''' update the status of reduction

        Args:
            fits_id : [int],
            status : [int]
        Returns:
            csst_dfs_common.models.Result            
        '''
        return self.stub.update_proc_status(**kwargs)

    def update_qc0_status(self, **kwargs):
        ''' update the status of QC0
        
        Args:
            fits_id : [int],
            status : [int]
        Returns:
            csst_dfs_common.models.Result            
        '''        
        return self.stub.update_qc0_status(**kwargs)    

    def write(self, **kwargs):
        ''' insert a level0 data record into database
 
        Args:
            obs_id = [int]
            detector_no = [str]
            obs_type = [str]        
            obs_time = [str]
            exp_time = [int]
            detector_status_id = [int]
            filename = [str]
            file_path = [str]
        Returns:
            csst_dfs_common.models.Result
        '''  
        return self.stub.write(**kwargs)

