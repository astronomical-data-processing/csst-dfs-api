
from ..common.delegate import Delegate
from astropy.table import Table

class Level2TypeApi(object):
    """
    Level2Type Data Operation Class
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "facility")
        self.stub = getattr(self.pymodule, "Level2TypeApi")()
        
    def find(self, **kwargs):
        ''' retrieve level2Type records from database

        :param kwargs: Parameter dictionary, key items support:
            module_id: [str]
            data_type: [str]
            import_status : [int],
            page: [int]
            limit: limits returns the number of records,default 0:no-limit
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    
    def get(self, **kwargs):
        '''  fetch a record from database

        :param kwargs: Parameter dictionary, key items support:
            data_type: [str]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.get(**kwargs)


    def update_import_status(self, **kwargs):
        ''' update the status of import

        :param kwargs: Parameter dictionary, key items support:
            data_type: [str],
            status = [int]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.update_import_status(**kwargs)

    def write(self, **kwargs):
        ''' insert a level2Type record into database

        :param kwargs: Parameter dictionary, key items support:
            data_type : [str]
            module_id : [str]
            key_column : [str]
            hdu_index : [int]
            demo_filename : [str]
            demo_file_path : [str]    
            ra_column : [str]
            dec_column : [str]
        
        :returns: csst_dfs_common.models.Result
        '''          
        return self.stub.write(**kwargs)
