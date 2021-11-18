FROM python:3.8.1-slim
LABEL author="weishoulin@astrolab.cn"

RUN apt-get update -y && apt-get install curl git -y --allow-unauthenticated
RUN sh -c "$(curl -fsSL https://raw.fastgit.org/astronomical-data-processing/csst-dfs-api/master/tools/csst-dfs-api-install.sh)"