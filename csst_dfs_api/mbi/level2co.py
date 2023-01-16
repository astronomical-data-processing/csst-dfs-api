
from ..common.delegate import Delegate

class Level2CoApi(object):
    """
    Level2 Merge Catalog Operation Class
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "msc")
        self.stub = getattr(self.pymodule, "Level2CoApi")()
        
    def find(self, **kwargs):
        ''' retrieve level2 Merge Catalog records from database

        :param kwargs: Parameter dictionary, key items support:
            data_type: [str]
            create_time : (start, end),
            qc2_status : [int],
            prc_status : [int],
            filename: [str]
            limit: limits returns the number of records,default 0:no-limit
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def catalog_query(self, **kwargs):
        ''' retrieve level2 Merge catalog

        :param kwargs: Parameter dictionary, key items support:
            obs_id: [str]
            detector_no: [str]
            min_mag: [float]
            max_mag: [float]
            obs_time: (start, end),
            limit: limits returns the number of records,default 0:no-limit
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.catalog_query(**kwargs)        

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

    def update_qc2_status(self, **kwargs):
        ''' update the status of QC2
        
        :param kwargs: Parameter dictionary, key items support:
            id = [int],
            status = [int]
        
        :returns: csst_dfs_common.models.Result
        '''        
        return self.stub.update_qc2_status(**kwargs)    

    def write(self, **kwargs):
        ''' insert a level2 record after merge into database
 
        :param kwargs: Parameter dictionary, key items support:
            data_type : [str]
            filename : [str]
            file_path : [str]            
            prc_status : [int]
            prc_time : [str]
            pipeline_id : [str]
        
        :returns: csst_dfs_common.models.Result
        '''          
        return self.stub.write(**kwargs)

