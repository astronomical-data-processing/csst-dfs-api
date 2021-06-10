
from ..common.delegate import Delegate

class CalMergeApi(object):
    """
    Level 0 Data Operation API
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "facility")
        self.stub = getattr(self.pymodule, "CalMergeApi")()
        
    def find(self, **kwargs):
        ''' retrieve calibration merge records from database

        Args:
            detector_no: [str]
            ref_type: [str]
            obs_time: (start,end)
            qc1_status : [int]
            prc_status : [int]
            file_name: [str]
            limit: limits returns the number of records,default 0:no-limit
        Returns:
            csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def get(self, **kwargs):
        '''  fetch a record from database

        Args:
            id : [int] 
        Returns:
            csst_dfs_common.models.Result
        '''
        return self.stub.get(**kwargs)

    def update_proc_status(self, **kwargs):
        ''' update the status of reduction

        Args:
            id : [int],
            status : [int]
        Returns:
            csst_dfs_common.models.Result
        '''
        return self.stub.update_proc_status(**kwargs)

    def update_qc1_status(self, **kwargs):
        ''' update the status of reduction

        AArgs:
            id : [int],
            status : [int]
        Returns:
            csst_dfs_common.models.Result
        '''        
        return self.stub.update_qc1_status(**kwargs)    

    def write(self, **kwargs):
        ''' insert a calibration merge record into database
        Args:
            detector_no : [str]
            ref_type : [str]
            obs_time : [str]
            exp_time : [float]
            prc_status : [int]
            prc_time : [str]
            filename : [str]
            file_path : [str]
            level0_ids : [list]
        Returns:
            csst_dfs_common.models.Result
        '''  
        return self.stub.write(**kwargs)

