
from ..common.delegate import Delegate

class OtherDataApi(object):
    """
    Other Data Operation Class
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "facility")
        self.stub = getattr(self.pymodule, "OtherDataApi")()
        
    def find(self, **kwargs):
        ''' retrieve other data records from database

        :param kwargs: Parameter dictionary, key items support:
            obs_id: [str]
            detector_no: [str]
            module_id: [str]
            data_type: [str]
            create_time : (start, end)
            filename: [str]
            pipeline_id: [str]
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
        ''' insert a other data record into database

        :param kwargs: Parameter dictionary, key items support:
            obs_id: [str]
            detector_no : [str]
            module_id : [str]
            file_type : [str]
            filename : [str]
            file_path : [str]            
            pipeline_id : [str]
        
        :returns: csst_dfs_common.models.Result
        '''          
        return self.stub.write(**kwargs)

