from ..facility import ObservationApi, Level0DataApi
from csst_dfs_commons.models import Result

def find_observation(
            module_id: str = None,
            obs_type: str = None,
            obs_time : tuple = (None, None),
            qc0_status : int = -1,
            prc_status : int = -1) -> Result:
    kwarg = locals()
    return ObservationApi().find(**kwarg)   

def find_level0(obs_id: str = '',
            module_id: str = '',
            detector_no: str = '',
            obs_type: str = '',
            filter: str = '',
            obs_time : tuple = (None, None),
            qc0_status : int = -1,
            prc_status : int = -1,
            file_name: str = '',
            ra_obj: float = None,
            dec_obj: float = None,
            radius: float = None,
            object_name: str = None,
            version: str = None) -> Result:
    kwarg = locals()
    return Level0DataApi().find(**kwarg)