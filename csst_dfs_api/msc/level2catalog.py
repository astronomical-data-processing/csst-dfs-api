import os
import logging
import numpy as np
from astropy.io import fits

from ..common.delegate import Delegate
from ..common.utils import *
from csst_dfs_commons.models import Result

log = logging.getLogger('csst_api')

class Level2CatalogApi(object):
    """
    Level1 Data Operation Class
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "msc")
        self.stub = getattr(self.pymodule, "Level2CatalogApi")()
        
    def find(self, **kwargs):
        ''' retrieve level2catalog records from database

        :param kwargs: Parameter dictionary, key items support:
            obs_id: [str]
            detector_no: [str]
            min_mag: [float]
            max_mag: [float]
            obs_time: (start, end),
            limit: limits returns the number of records,default 0:no-limit
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def write(self, **kwargs):
        ''' insert a level2 catalog file into database
 
        :param kwargs: Parameter dictionary, key items support:
            file_path: str

        :returns: csst_dfs_common.models.Result
        '''          

        try:
            file_path = get_parameter(kwargs, "file_path", '')
            if not file_path:
                return Result.error(message="file_path is blank")
            if not os.path.exists(file_path):
                return Result.error(message="the file [%s] not existed" % (file_path, )) 
            records = []
            success_num, fail_num = 0, 0

            hdul = fits.open(file_path)
            header = hdul[0].header
            binTable = hdul[1]

            obs_id = header["OBSID"]
            detector_no = header["DETECTOR"][3:5]
            obs_time = f"{header['DATE-OBS']} {header['TIME-OBS']}"
            batch_size = 500
            for tr in binTable.data:
                v_list = [f"'{obs_id}'",f"'{detector_no}'"]
                for td in tr:
                    if type(td) == np.ndarray:
                        v_list.extend(td)
                    else:
                        v_list.append(td)
                v_list.append(f"'{obs_time}'")
                records.append(",".join(['null' if type(v) != str and np.isnan(v) else str(v) for v in v_list]))
            
                if len(records) == batch_size:
                    resp = self.stub.write(records)
                    if resp.success:
                        success_num += len(records)
                    else:
                        log.error(f"{resp.message}")
                        fail_num  += len(records)
                    records.clear()
                    records = []
            if records:
                resp = self.stub.write(records)
                if resp.success:
                    success_num += len(records)
                else:
                    log.error(f"{resp.message}")
                    fail_num  += len(records)                
            return Result.ok_data({"success_num":success_num, "fail_num": fail_num})
        except Exception as e:
            return Result.error(str(e))        


