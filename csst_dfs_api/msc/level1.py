
from ..common.delegate import Delegate

class Level1DataApi(object):
    """
    Level1 Data Operation Class
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "msc")
        self.stub = getattr(self.pymodule, "Level1DataApi")()
        
    def find(self, **kwargs):
        ''' retrieve level1 records from database

        Args:
            raw_id: [int]
            data_type: [str]
            obs_type: [str]
            create_time : (start, end),
            qc1_status : [int],
            prc_status : [int],
            filename: [str]
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
            id = [int],
            status = [int]
        Returns:
            csst_dfs_common.models.Result
        '''
        return self.stub.update_proc_status(**kwargs)

    def update_qc1_status(self, **kwargs):
        ''' update the status of QC0
        
        Args:
            id = [int],
            status = [int]
        Returns:
            csst_dfs_common.models.Result
        '''        
        return self.stub.update_qc1_status(**kwargs)    

    def write(self, **kwargs):
        ''' insert a level1 record into database
 
        Args:
            raw_id : [int]
            data_type : [str]
            cor_sci_id : [int]
            prc_params : [str]
            flat_id : [int]
            dark_id : [int]
            bias_id : [int]
            filename : [str]
            file_path : [str]            
            prc_status : [int]
            prc_time : [str]
            pipeline_id : [str]
        Returns:
            csst_dfs_common.models.Result
        '''          
        return self.stub.write(**kwargs)

