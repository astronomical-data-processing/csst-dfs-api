
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
        
        :param kwargs: Parameter dictionary, key items support:
            detector_no: [str],
            ref_type: [str],
            obs_time: (start,end),
            qc1_status : [int],
            prc_status : [int],
            file_name: [str],
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

    def update_proc_status(self, **kwargs):
        ''' update the status of reduction

        :param kwargs: Parameter dictionary, key items support:
            id : [int],
            status : [int]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.update_proc_status(**kwargs)

    def update_qc1_status(self, **kwargs):
        ''' update the status of reduction

        :param kwargs: Parameter dictionary, key items support:
            id : [int],
            status : [int]
        
        :returns: csst_dfs_common.models.Result
        '''        
        return self.stub.update_qc1_status(**kwargs)    

    def write(self, **kwargs):
        ''' insert a calibration merge record into database

        :param kwargs: Parameter dictionary, key items support:
            detector_no : [str]
            ref_type : [str]
            obs_time : [str]
            exp_time : [float]
            prc_status : [int]
            prc_time : [str]
            filename : [str]
            file_path : [str]
            level0_ids : [list]
        
        :returns: csst_dfs_common.models.Result
        '''  
        return self.stub.write(**kwargs)

