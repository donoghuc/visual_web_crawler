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
- note make sure you are using bash shell if you want to use kill -kill
```
flip1 ~ 151% top -U donoghuc

top - 08:33:11 up 30 days, 13:30, 61 users,  load average: 4.22, 9.92, 18.98
Tasks: 1310 total,   5 running, 1293 sleeping,  10 stopped,   2 zombie
%Cpu(s): 16.6 us,  0.2 sy,  0.0 ni, 83.1 id,  0.0 wa,  0.0 hi,  0.1 si,  0.0 st
KiB Mem : 98821584 total, 32793244 free, 47274048 used, 18754296 buff/cache
KiB Swap:  4194300 total,   189032 free,  4005268 used. 49525268 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND     
29413 donoghuc  20   0  169224   4568   2636 R   1.3  0.0   0:00.17 top         
26349 donoghuc  20   0  531492  31360   5180 S   0.0  0.0   0:01.84 pserve      
29316 donoghuc  20   0  166188   2408   1120 S   0.0  0.0   0:00.01 sshd        
29317 donoghuc  20   0  136132   2096   1360 S   0.0  0.0   0:00.06 tcsh  

bash-4.2$ kill -kill 26349
bash-4.2$ top -U donoghuc

top - 08:34:25 up 30 days, 13:32, 61 users,  load average: 4.43, 8.71, 17.86
Tasks: 1316 total,   5 running, 1299 sleeping,  10 stopped,   2 zombie
%Cpu(s): 16.8 us,  1.7 sy,  0.0 ni, 81.5 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem : 98821584 total, 32834456 free, 47235764 used, 18751368 buff/cache
KiB Swap:  4194300 total,   189032 free,  4005268 used. 49563088 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND     
30617 donoghuc  20   0  169264   4444   2580 R   8.7  0.0   0:00.09 top         
29316 donoghuc  20   0  166188   2408   1120 S   0.0  0.0   0:00.02 sshd        
29317 donoghuc  20   0  136132   2144   1404 S   0.0  0.0   0:00.06 tcsh     
```