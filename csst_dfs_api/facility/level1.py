
from ..common.delegate import Delegate

class Level1DataApi(object):
    """
    Level1 Data Operation Class
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "facility")
        self.stub = getattr(self.pymodule, "Level1DataApi")()
        
    def find(self, **kwargs):
        ''' retrieve level1 records from database

        :param kwargs: Parameter dictionary, key items support:
            obs_id: [str]
            level0_id: [str]
            module_id: [str]
            data_type: [str]
            create_time : (start, end)
            qc1_status : [int]
            prc_status : [int]
            filename: [str]
            ra_cen: float = None
            dec_cen: float = None,
            radius_cen: float = None
            pipeline_id: [str]
            detector_no: [str]
            filter: [str]
            object_name: [str]
            limit: limits returns the number of records,default 0:no-limit
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def find_by_brick_ids(self, **kwargs):
        ''' retrieve level1 records by brick_ids like [1,2,3,4]

        :param kwargs: Parameter dictionary, key items support:
            brick_ids: [list]
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find_by_brick_ids(**kwargs)

    def find_by_ids(self, **kwargs):
        ''' retrieve level1 records by internal level1 ids like [1,2,3,4]

        :param kwargs: Parameter dictionary, key items support:
            ids: [list]
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find_by_ids(**kwargs)
    
    def sls_find_by_qc1_status(self, **kwargs):
        ''' retrieve level1 records from database

        :param kwargs: Parameter dictionary, key items support:
            qc1_status : [int],
            limit: limits returns the number of records,default 1
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.sls_find_by_qc1_status(**kwargs)

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
            data_type : [str]
            cor_sci_id : [int]
            prc_params : [str]
            filename : [str]
            file_path : [str]            
            prc_status : [int]
            prc_time : [str]
            pipeline_id : [str]
            refs: [dict]
        
        :returns: csst_dfs_common.models.Result
        '''          
        return self.stub.write(**kwargs)

