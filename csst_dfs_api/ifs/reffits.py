
from ..common.delegate import Delegate

class RefFitsApi(object):
    """
    Reference Fits Operation Class of IFS
    """
    REF_FITS_BIAS = "bias"
    REF_FITS_FLAT = "flat"
    REF_FITS_DARK = "dark"
    REF_FITS_SKY = "sky"
    REF_FITS_ARC = "arc"

    REF_FITS_TYPES = [REF_FITS_BIAS, REF_FITS_FLAT, REF_FITS_DARK, REF_FITS_SKY, REF_FITS_ARC]

    def __init__(self, sub_system="ifs"):
        self.sub_system = sub_system
        self.module = Delegate().load(sub_module = "ifs")
        self.stub = getattr(self.module, "RefFitsApi")()
        self.file_prefix = self.stub.root_dir

    def find(self, **kwargs):
        '''
        parameter kwargs:
            obs_time = [int],
            file_name = [str],
            exp_time = (start, end),
            ccd_num = [int],
            status = [int],
            ref_type = [str]

        return list of reference's files records
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

    def update_status(self, **kwargs):
        ''' update the status of reduction

        parameter kwargs:
            fits_id = [int],
            status = [int]
        '''
        return self.stub.update_status(**kwargs)

    def write(self, **kwargs):
        ''' copy a local file to file storage, then reduce the header of fits file and insert a record into database
 
        parameter kwargs:
            file_path = [str]
        '''        
        return self.stub.write(**kwargs)

