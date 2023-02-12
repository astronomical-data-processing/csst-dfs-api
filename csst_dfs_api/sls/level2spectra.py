
from ..common.delegate import Delegate

class Level2SpectraApi(object):
    """
    Level1 Data Operation Class
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "sls")
        self.stub = getattr(self.pymodule, "Level2SpectraApi")()
        
    def find(self, **kwargs):
        ''' retrieve level2 spectra records from database

        :param kwargs: Parameter dictionary, key items support:
            level0_id: [str]
            level1_id: [int]
            spectra_id: [str]
            create_time : (start, end),
            qc1_status : [int],
            prc_status : [int],
            filename: [str]
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
            id = [int],
            status = [int]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.update_proc_status(**kwargs)

    def update_qc1_status(self, **kwargs):
        ''' update the status of QC1
        
        :param kwargs: Parameter dictionary, key items support:
            id = [int],
            status = [int]
        
        :returns: csst_dfs_common.models.Result
        '''        
        return self.stub.update_qc1_status(**kwargs)    

    def write(self, **kwargs):
        ''' insert a level1 record into database

        :param kwargs: Parameter dictionary, key items support:
            level0_id: [str]
            level1_id: [int]
            spectra_id : [str]
            region : [str]
            filename : [str]
            file_path : [str]            
            prc_status : [int]
            prc_time : [str]
            pipeline_id : [str]
        
        :returns: csst_dfs_common.models.Result
        '''          
        return self.stub.write(**kwargs)

