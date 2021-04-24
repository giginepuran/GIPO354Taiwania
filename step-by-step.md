# Preparation
1. First, download [this](https://drive.google.com/file/d/1XDkycp9DfaUTwRdZWeE8WMffhltzRYry/view?usp=sharing) 
2. In cmd, connect to tawwania, and put it to ~/LumFile 
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
![Preparation1](https://imgur.com/J6e7d9g.jpg)
![Preparation2](https://imgur.com/M5dBhEL.jpg)

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

![login](https://imgur.com/wY4nxV5.jpg)
![BeforeInstall](https://imgur.com/n5LaMHe.jpg)
![Install&check](https://imgur.com/I8EvrWs.jpg)

# That's all
