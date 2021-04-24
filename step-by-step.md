# Preparation
1. First, download [this](https://drive.google.com/file/d/1XDkycp9DfaUTwRdZWeE8WMffhltzRYry/view?usp=sharing) \
2. In cmd, connect to tawwania, and put it to ~/LumFile \
```
sftp user@140.110.148.22
Password:
Changing MOTP:

Auth MOTP: PASS
Auth Password: PASS
sftp> mkdir LumFile; cd LumFile
sftp> put .../LUM354.tar 
sftp> bye
```

# Login & install Lumerical
```
ssh user@140.110.148.11
Password:
Changing MOTP:

Auth MOTP: PASS
Auth Password: PASS
```
1. Before installing - modify your userdata
```
cd LumFile
vi testjob.sh
```
2. Install Lumerical & test
```
sh LumericalInstaller.sh
6003571 blocks
Initialized empty Git repository in /home/u5/u6097335/tools/.git/
129699.srvc1
qstat 129699 -H
```
3. Check E-mail / ~/LumFile/.log file

# That's all
