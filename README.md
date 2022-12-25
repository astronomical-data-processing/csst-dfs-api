# CSST DFS APIs library

## Introduction

This package provides APIs to access csst's files and databases.

## Installation

`csst-dfs-api` can be installed with the following command:

```bash
git clone https://csst-tb.bao.ac.cn/code/csst-dfs/csst-dfs-api.git
cd csst-dfs-api
pip install -r requirements.txt
python setup.py install
```

`csst-dfs-api` and relevant packages could be installed by running one of the following commands in your terminal.

```bash
sh -c "$(curl -fsSL https://csst-tb.bao.ac.cn/code/csst-dfs/csst-dfs-api/-/raw/master/tools/csst-dfs-api-install.sh)"
```

## Configuration

enviroment variables

- CSST_DFS_API_MODE = local or cluster               # default: local
- CSST_LOCAL_FILE_ROOT = [a local file directory]    # required if DFS_API_MODE = local,  default: /opt/temp/csst
- CSST_DFS_GATEWAY = [gateway server's address]      # required if DFS_API_MODE = cluster
