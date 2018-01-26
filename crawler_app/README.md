# Install and Run on OSU server
- SSH (over VPN in you want) in to the OSU server (ssh donoghuc@access.engr.oregonstate.edu)
- I typcially switch from defaut xterm shell to bash
- install python 3.6 
```
curl -LO https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -p ~/miniconda -b
rm Miniconda3-latest-Linux-x86_64.sh 
echo "export PATH=~/miniconda/bin:\$PATH" >> ~/.bashrc
source ~/.bashrc
```
- test python install (see below)
```
bash-4.2$ python --version
Python 3.6.3 :: Anaconda, Inc.
```
- install virtualenv
```
bash-4.2$ pip install virtualenv
```
- clone our repo
```
bash-4.2$ git clone https://github.com/donoghuc/visual_web_crawler.git
```
- set up virutalenv inside repo (dont VCS virtualenv stuff!!!)
- get your path to the python in the miniconda bin (my onid is donoghuc so you can I installed mine in home ~/)
- activate new environment

```
bash-4.2$ cd ~/visual_web_crawler
bash-4.2$ virtualenv -p /nfs/stak/users/donoghuc/miniconda/bin/python --no-site-packages env_crawler_app
bash-4.2$ source env_crawler_app/bin/activate
(env_crawler_app) bash-4.2$ 
```
- go to crawler app directory
- install project and dependencies
```
(env_crawler_app) bash-4.2$ cd crawler_app/
(env_crawler_app) bash-4.2$ ls
CHANGES.txt  development.ini  production.ini  README.txt
crawler_app  MANIFEST.in      pytest.ini      setup.py
(env_crawler_app) bash-4.2$ pip install -e .
```
- run in production mode on server with pserve
- NOTE if port is taken change it in production.ini
```
(env_crawler_app) bash-4.2$ ls
CHANGES.txt  crawler_app.egg-info  MANIFEST.in	   pytest.ini  setup.py
crawler_app  development.ini	   production.ini  README.txt
(env_crawler_app) bash-4.2$ pserve production.ini 
Running in prod mode.
Starting server in PID 23659.
Serving on http://0.0.0.0:6543
Serving on http://[::]:6543
```
- for local development run development.ini
```
(env_crawler_app) cas@ubuntu:~/working_dir/visual_web_crawler/crawler_app$ ls
CHANGES.txt  crawler_app.egg-info  MANIFEST.in     pytest.ini  setup.py
crawler_app  development.ini       production.ini  README.txt
(env_crawler_app) cas@ubuntu:~/working_dir/visual_web_crawler/crawler_app$ pserve development.ini 
Running in prod mode.
Starting server in PID 3790.
Serving on http://localhost:6543

```
- "persisting" on osu server
- i started on flip1 and set process to run in background 
```
(env_crawler_app) bash-4.2$ pserve production.ini &
```
- i can safely close that terminal and when I log back in i can look up the process using top -U
- This will show me all my processes, in this case i have pserve running at PID 26349, so i could kill that from new session. 
```
flip1 ~ 153% top -U donoghuc
```