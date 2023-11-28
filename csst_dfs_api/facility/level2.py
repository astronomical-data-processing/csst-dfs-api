
from ..common.delegate import Delegate
from astropy.table import Table

class Level2DataApi(object):
    """
    Level2 Data Operation Class
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "facility")
        self.stub = getattr(self.pymodule, "Level2DataApi")()
        
    def find(self, **kwargs):
        ''' retrieve level2 records from database

        :param kwargs: Parameter dictionary, key items support:
            level0_id: [str]
            level1_id: [int]
            module_id: [str]
            brick_id: [int]
            data_type: [str]
            create_time : (start, end),
            qc2_status : [int],
            prc_status : [int],
            import_status : [int],
            filename: [str]
            limit: limits returns the number of records,default 0:no-limit
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def catalog_query(self, **kwargs):
        ''' retrieve level2 catalog

        :param kwargs: Parameter dictionary, key items support:
            sql: [str]
            limit: limits returns the number of records,default 0:no-limit
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.catalog_query(**kwargs)

    def find_existed_brick_ids(self, **kwargs):
        '''  retrieve existed brick_ids in the catalog with data_type
        :param kwargs: 
            data_type: [str]
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find_existed_brick_ids(**kwargs)    
    
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
        ''' insert a level2 record into database

        :param kwargs: Parameter dictionary, key items support:
            level1_id: [int]
            brick_id: [int]
            module_id : [str]
            object_name: [str]
            data_type : [str]
            filename : [str]
            file_path : [str]            
            prc_status : [int]
            prc_time : [str]
            pipeline_id : [str]
        
        :returns: csst_dfs_common.models.Result
        '''          
        return self.stub.write(**kwargs)
