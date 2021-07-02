from csst_dfs_api.facility.level0 import Level0DataApi

api = Level0DataApi()

# find
recs = api.find(obs_id = 17, obs_type = 'sci', limit = 0, prc_status = -1)
print('find:', recs)

# get
rec = api.get(fits_id = 100)
print('get:', rec)

# update_proc_status
rec = api.update_proc_status(fits_id = 100, status = 6)
print('update_proc_status:', rec)

# update_qc0_status
rec = api.update_qc0_status(fits_id = 100, status = 7)
print('update_qc0_status:', rec)
