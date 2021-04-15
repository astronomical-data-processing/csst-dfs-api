
from ..common.delegate import Delegate

class FitsApi(object):
    """
    Raw Fits Operation Class of IFS
    """
    def __init__(self, sub_system="ifs"):
        self.sub_system = sub_system
        self.module = Delegate().load(sub_module = "ifs")
        self.stub = getattr(self.module, "FitsApi")()
        
    def find(self, **kwargs):
        '''
        parameter kwargs:
            obs_time = [int],
            file_name = [str],
            exp_time = (start, end),
            ccd_num = [int],
            qc0_status = [int],
            prc_status = [int],
            limit: limits returns the number of records

        return: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def get(self, **kwargs):
        '''  query database, return a record as dict

        parameter kwargs:
            fits_id = [int] 

        return dict or None
        '''
        return self.stub.get(**kwargs)

    def read(self, **kwargs):
        ''' yield bytes of fits file

        parameter kwargs:
            fits_id = [int],
            file_path = [str], 
            chunk_size = [int] default 20480

        yield bytes of fits file
        '''
        return self.stub.read(**kwargs)

    def update_proc_status(self, **kwargs):
        ''' update the status of reduction

        parameter kwargs:
            fits_id = [int],
            status = [int]
        '''
        return self.stub.update_proc_status(**kwargs)

    def update_qc0_status(self, **kwargs):
        ''' update the status of reduction
        
        parameter kwargs:
            fits_id = [int],
            status = [int]
        '''        
        return self.stub.update_qc0_status(**kwargs)    

    def write(self, **kwargs):
        ''' copy a local file to file storage, then reduce the header of fits file and insert a record into database
 
        parameter kwargs:
            file_path = [str]
        '''        
        return self.stub.write(**kwargs)

