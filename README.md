# CSST DFS APIs library

## Introduction

This package provides APIs to access csst's files and databases.

## Installation

This library can be installed with the following command: 

```bash
python setup.py install
```

## Configuration

enviroment variables
CSST_DFS_API_MODE = local or cluster         # defaulrt: cluster
CSST_LOCAL_FILE_ROOT = [a local file directory] # required if DFS_API_MODE = local,  default: /opt/temp/csst
CSST_DFS_CONFIG_SERVER = [config server's address] # required if DFS_API_MODE = cluster, 
