from ..common.delegate import Delegate

class DetectorApi(object):
    """
    Detector Operation Class
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "facility")
        self.stub = getattr(self.pymodule, "DetectorApi")()
        
    def find(self, **kwargs):
        ''' retrieve detector records from database

        parameter kwargs:
            module_id: [str]
            key: [str]

        return: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def get(self, **kwargs):
        '''  fetch a record from database

        parameter kwargs:
            no : [str] 

        return csst_dfs_common.models.Result
        '''
        return self.stub.get(**kwargs)

    def update(self, **kwargs):
        ''' update a detector by no

        parameter kwargs:
            no : [str],
            detector_name : [str],
            module_id : [str],
            filter_id : [str]

        return csst_dfs_common.models.Result
        '''
        return self.stub.update(**kwargs)

    def delete(self, **kwargs):
        ''' delete a detector by no

        parameter kwargs:
            no : [str]

        return csst_dfs_common.models.Result
        '''
        return self.stub.delete(**kwargs)

    def write(self, **kwargs):
        ''' insert a detector record into database
 
        parameter kwargs:
            no : [str],
            detector_name : [str],
            module_id : [str],
            filter_id : [str]
        return csst_dfs_common.models.Result
        '''        
        return self.stub.write(**kwargs)

    def find_status(self, **kwargs):
        ''' retrieve a detector status's from database

        parameter kwargs:
            detector_no: [str]
            status_occur_time: (begin,end)
            limit: limits returns the number of records,default 0:no-limit

        return: csst_dfs_common.models.Result
        '''
        return self.stub.find_status(**kwargs)

    def get_status(self, **kwargs):
        '''  fetch a record from database

        parameter kwargs:
            id : [int] 

        return csst_dfs_common.models.Result
        '''
        return self.stub.get_status(**kwargs)

    def write_status(self, **kwargs):
        ''' insert a detector status into database
 
        parameter kwargs:
            detector_no : [str],
            status : [str],
            status_time : [str]
        return csst_dfs_common.models.Result
        '''
        return self.stub.write_status(**kwargs)  