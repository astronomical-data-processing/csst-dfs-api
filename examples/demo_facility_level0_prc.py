from csst_dfs_api.facility.level0prc import Level0PrcApi

api = Level0PrcApi()

#find
recs = api.find(level0_id=134)
print('find:', recs)

#update_proc_status
rec = api.update_proc_status(id = 8, status = 4)
print('update_proc_status:', rec)

#write
rec = api.write(level0_id=134, 
    pipeline_id = "P1",
    prc_module = "QC0",
    params_id = "/opt/dddasd.params",
    prc_status = 3,
    prc_time = '2021-06-04 11:12:13',
    file_path = "/opt/dddasd.header")
print('write:', rec)