echo "CSST-DFS-API Installer"
echo "=============================================="

if [ $# != 1 ] ; then
echo "USAGE: $0 [version]"
echo " e.g.: $0 v0.0.1"
exit 1;
fi
version=$1

pip uninstall csst-dfs-api-local -y
pip uninstall csst-dfs-api-cluster -y
pip uninstall csst-dfs-commons -y
pip uninstall csst-dfs-proto -y
pip uninstall csst-dfs-api -y

echo "Installing.....Version:$version"
echo "=============================================="
echo "1/5"
pip install git+https://hub.fastgit.org/astronomical-data-processing/csst-dfs-commons.git@$version
echo "2/5"
pip install git+https://hub.fastgit.org/astronomical-data-processing/csst-dfs-proto-py.git@$version
echo "3/5"
pip install git+https://hub.fastgit.org/astronomical-data-processing/csst-dfs-api-local.git@$version
echo "4/5"
pip install git+https://hub.fastgit.org/astronomical-data-processing/csst-dfs-api-cluster.git@$version
echo "5/5"
pip install git+https://hub.fastgit.org/astronomical-data-processing/csst-dfs-api.git@$version
echo "=============================================="
echo "Done!"