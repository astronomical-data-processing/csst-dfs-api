
from ..common.delegate import Delegate
from astropy.table import Table

class Level2DataApi(object):
    """
    Level2 Data Operation Class
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "mbi")
        self.stub = getattr(self.pymodule, "Level2DataApi")()
        
    def find(self, **kwargs):
        ''' retrieve level2 records from database

        :param kwargs: Parameter dictionary, key items support:
            level0_id: [str]
            level1_id: [int]
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
        ''' retrieve level2 catalog

        :param kwargs: Parameter dictionary, key items support:
            brick_ids: tuple of int, like (1,2,3)
            obs_id: [str]
            detector_no: [str]
            filter: [str]
            ra:  [float] in deg
            dec: [float] in deg
            radius:  [float] in deg
            obs_time: (start, end)
            columns: tuple of str, like ('ra','dec','sky')
            limit: limits returns the number of records,default 0:no-limit
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.catalog_query(**kwargs)        

    def catalog_query_file(self, **kwargs):
        ''' retrieve level2 catalog, return Level2Record

        :param kwargs: Parameter dictionary, key items support:
            brick_ids: list[int]
            obs_id: [str]
            detector_no: [str]
            filter: [str]
            ra:  [float] in deg
            dec: [float] in deg
            radius:  [float] in deg
            obs_time: (start, end)
            limit: limits returns the number of records,default 0:no-limit
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.catalog_query_file(**kwargs)  
    
    def find_existed_brick_ids(self, **kwargs):
        '''  retrieve existed brick_ids in a single exposure catalog

        :param kwargs: 
        
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
            data_type : [str]
            filename : [str]
            file_path : [str]            
            prc_status : [int]
            prc_time : [str]
            pipeline_id : [str]
        
        :returns: csst_dfs_common.models.Result
        '''          
        return self.stub.write(**kwargs)

