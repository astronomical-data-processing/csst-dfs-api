
from ..common.delegate import Delegate

class ObservationApi(object):
    """
    Observation Operation Class
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "facility")
        self.stub = getattr(self.pymodule, "ObservationApi")()
        
    def find(self, **kwargs):
        ''' retrieve exposure records from database

        parameter kwargs:
            obs_id = [int]
            module_id: [str]
            obs_type: [str]
            obs_time : (start, end),
            qc0_status : [int],
            prc_status : [int],
            limit: limits returns the number of records,default 0:no-limit

        return: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def get(self, **kwargs):
        '''  fetch a record from database

        parameter kwargs:
            obs_id = [int] 

        return: csst_dfs_common.models.Result
        '''
        return self.stub.get(**kwargs)


    def update_proc_status(self, **kwargs):
        ''' update the status of reduction

        parameter kwargs:
            obs_id = [int],
            status = [int]
        
        return: csst_dfs_common.models.Result
        '''
        return self.stub.update_proc_status(**kwargs)

    def update_qc0_status(self, **kwargs):
        ''' update the status of QC0
        
        parameter kwargs:
            obs_id = [int],
            status = [int]

        return: csst_dfs_common.models.Result
        '''        
        return self.stub.update_qc0_status(**kwargs)    

    def write(self, **kwargs):
        ''' insert a observational record into database
 
        parameter kwargs:
            obs_time = [str]
            exp_time = [float]
            module_id = [str]
            obs_type = [str]
            facility_status_id = [int]
            module_status_id = [int]
        
        return: csst_dfs_common.models.Result
        '''        
        return self.stub.write(**kwargs)

