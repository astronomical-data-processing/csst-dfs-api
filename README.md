# CSST DFS APIs library

## Introduction

This package provides APIs to access csst's files and databases.

## Installation

This library can be installed with the following command: 

```bash
git clone https://github.com/astronomical-data-processing/csst-dfs-api.git
cd csst-dfs-api
pip install -r requirements.txt
python setup.py install
```

## Configuration

enviroment variables
- CSST_DFS_API_MODE = local or cluster               # default: local
- CSST_LOCAL_FILE_ROOT = [a local file directory]    # required if DFS_API_MODE = local,  default: /opt/temp/csst
- CSST_DFS_GATEWAY = [gateway server's address]       # required if DFS_API_MODE = cluster, 
