# Ansible Deploy

We are hosting our web app on Digital Ocean. This directory (deploy) has the ansible playbooks for provisioning a new server and for doing routine code pushes to the server. 

## Init Config
- When a new Digital Ocean Droplet (Ubuntu 16.04 LTS) is rented run this playbook
- install failtoban, disable root ssh, make non root user, change authentication to RSA key pair only
- General intent is to do some basic security for hosting public website

## Init Miniconda
- This recipe based on [andrew rothstien's ansible galaxy recipe](https://github.com/andrewrothstein/ansible-miniconda)
- it uses the miniconda distribution to get python 3.6 (the ubuntu server has an older version)
- typically run only once per server provision 

## Prod Deploy (common)
- this is run every time new code is ready to go to production
- this is the most "complex" playbook, it ensures dependencies are satisfied, that new code is pulled from github master branch,  that the nginx and waitress servers are restarted and stay up. 
