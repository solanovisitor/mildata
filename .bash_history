sudo apt install python3-pip
pip3 install virtualenv
mkdir dbt-project
cd dbt-project/
virutalenv -p python3 .env
virtualenv .env
which virtualenv
virtualenv --version
apt-get install python3-virtualenv
sudo apt-get install python3-virtualenv
virtualenv -p python3 .env
sudo virtualenv -p python3 .env
sudo /usr/bin/easy_install virtualenv
cd dbt-project/
sudo apt-get install python-virtualenv
virtualenv -p python3 .env
source .env/bin/activate
pip install --upgrade setuptools
pip3 install dbt
pip install -U dbt-sqlserver
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get -q -y install msodbcsql17
sudo curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
sudo apt-get install unixodbc-dev
pip install pyodbc
pip install -U dbt-sqlserver
df -h
dbt init
dbt init DataLake
cd dbt-project/
dbt init DataLake/
source .env/bin/activate
dbt init DataLake/
dbt init DataLake
mkdir metabase
virtualenv -p python3 /env
virtualenv -p python3 .env
sudo apt-get update
sudo apt-get install     ca-certificates     curl     gnupg     lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo chmod a+r /etc/apt/keyrings/docker.gpg
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo chmod a+r /etc/apt/keyrings/docker.gpg
sudo apt-get update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce
sudo apt install docker-ce
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce
sudo apt install docker-ce -y
docker pull metabase/metabase:latest
sudo apt update && sudo apt upgrade
sudo apt-get install apt-transport-https ca-certificates curl gnupg software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt install docker-ce
curl -O https://download.docker.com/linux/debian/dists/buster/pool/stable/amd64/containerd.io_1.4.3-1_amd64.deb
sudo apt install docker-ce
sudo apt install ./containerd.io_1.4.3-1_amd64.deb
sudo apt install docker-ce
sudo systemctl status docker
docker pull metabase/metabase:latest
sudo docker pull metabase/metabase:latest
docker run -d -p 3000:3000 --name metabase metabase/metabase
sudo docker run -d -p 3000:3000 --name metabase metabase/metabase
cd ..
git clone https://github.com/airbytehq/airbyte.git
cd airbyte
docker-compose up
sudo apt-get update
docker-compose up
sudo apt-get update
sudo apt-get install docker-compose-plugin
docker-compose up
sudo docker-compose up
docker compose version
Docker Compose version vN.N.N
docker compose up
sudo docker compose up
mkdir mildata
virtualenv -p python3 .env
cd ..
git pull https://github.com/mtchavez/python-package-boilerplate.git
git clone https://github.com/mtchavez/python-package-boilerplate.git
ls
sudo rm -rf mildata/
sudo mv python-package-boilerplate/ mildata/
ls
cd mildata/
virtualenv -p python3 .env
source .env/bin/activate
pip3 install -r requirements.txt 
echo "# mildata" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/solanovisitor/mildata.git
git push -u origin main
git
echo "# mildata" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/solanovisitor/mildata.git
git push -u origin main
git remote add origin https://github.com/solanovisitor/mildata.git
git branch -M main
git push -u origin main
git remote set-url origin https://github.com/solanovisitor/mildata.git
git push -u origin main
git remote add origin https://github.com/solanovisitor/mildata.git
git remote -v
git push
git push origin master
git push origin
git push origin master
git stage
git add .
git commit -m "first commit"
git push
git push origin master
git push
git branch --unset-upstream
git push
git push --set-upstream origin main
git init
git config
git push
git push --set-upstream origin main
git push
git push --set-upstream origin main
git remote -v
git config --global user.name "solanovisitor"
git config --global user.email "solano.todeschini@gmail.com"
git config --l
git config -l
git push --set-upstream origin main
git init
rm -rf .git
echo "# mildata" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/solanovisitor/mildata.git
git push -u origin main
sudo git push -u origin main
git add .
git commit -m "first code"
git push
sudo git push
cd ..
sudo rm -rf mildata/
curl -sSL https://install.python-poetry.org | python3 -
poetry --help
mkdir mildata
cd mildata/
poetry new mildata
