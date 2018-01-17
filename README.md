# visual web crawler
Repo for capstone project 

### installation
- make sure you have python3 and virtualenv installed (pip install virtualenv)
- clone this repo
__create new virtualenv__
```
# use -p if you want to use special python interpreter i'm using miniconda bc it is awesome
cas@ubuntu:~/working_dir/visual_web_crawler$ virtualenv -p /home/cas/miniconda/bin/python crawler
```
__activate crawler virtual env__
```
cas@ubuntu:~/working_dir/visual_web_crawler$ source crawler/bin/activate
(crawler) cas@ubuntu:~/working_dir/visual_web_crawler$ ls
crawler web_crawler_POC.ipynb README.md requirements.txt
```
__install requirements__
```
cas@ubuntu:~/working_dir/visual_web_crawler$ pip install -r requirements.txt
```
__get geckodriver for selenium__
```
# download latest
(crawler) cas@ubuntu:~/working_dir/visual_web_crawler$ curl -LO https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
# untar/unzip
(crawler) cas@ubuntu:~/working_dir/visual_web_crawler$ gunzip geckodriver-v0.19.1-linux64.tar.gz
(crawler) cas@ubuntu:~/working_dir/visual_web_crawler$ tar -xvf geckodriver-v0.19.1-linux64.tar
# remove tarball
(crawler) cas@ubuntu:~/working_dir/visual_web_crawler$ rm geckodriver-v0.19.1-linux64.tar  
# point it to virtualenv bin
(crawler) cas@ubuntu:~/working_dir/visual_web_crawler$ mv geckodriver crawler/bin/
```
__look at jupyter notebook__
```
(crawler) cas@ubuntu:~/working_dir/visual_web_crawler$ jupyter notebook
```
