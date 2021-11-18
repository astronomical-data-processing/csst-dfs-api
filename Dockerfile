from python:3.8.1-slim

RUN apt-get update -y --allow-unauthenticated && apt-get install curl git -y --allow-unauthenticated
RUN curl https://raw.fastgit.org/astronomical-data-processing/csst-dfs-api/master/tools/csst-dfs-api-install.sh >> /csst-dfs-api-install.sh
RUN chmod a+x /csst-dfs-api-install.sh
# RUN /csst-dfs-api-install.sh