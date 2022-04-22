echo "CSST-DFS-API Installer"
echo "=============================================="

version=""
user=""

pip uninstall csst-dfs-api-local -y
pip uninstall csst-dfs-api-cluster -y
pip uninstall csst-dfs-commons -y
pip uninstall csst-dfs-proto -y
pip uninstall csst-dfs-api -y

echo "Installing CSST DFS API with Version:$version"
echo "➡==============================================="
echo " 🛰  1️⃣/5️⃣"
pip install$user git+https://hub.fastgit.xyz/astronomical-data-processing/csst-dfs-commons.git$version
echo " 🛰  2️⃣/5️⃣"
pip install$user git+https://hub.fastgit.xyz/astronomical-data-processing/csst-dfs-proto-py.git$version
echo " 🛰  3️⃣/5️⃣"
pip install$user git+https://hub.fastgit.xyz/astronomical-data-processing/csst-dfs-api-local.git$version
echo " 🛰  4️⃣/5️⃣"
pip install$user git+https://hub.fastgit.xyz/astronomical-data-processing/csst-dfs-api-cluster.git$version
echo " 🛰  5️⃣/5️⃣"
pip install$user git+https://hub.fastgit.xyz/astronomical-data-processing/csst-dfs-api.git$version
echo "➡==============================================="
echo "🇨🇳🇨🇳🇨🇳🚀🚀🚀Done!"