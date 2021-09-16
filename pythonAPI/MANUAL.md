# Using lumerical python api to optimize/simulate waveguid design in DBS-bending on taiwania (140.110.148.17)

## 1. Set conda to run lumerical api with python3
因為此DBS腳本是用py3語法 

而且taiwania預設的python2缺package 

所以這步驟為必須

[ref] https://iservice.nchc.org.tw/nchc_service/nchc_service_qa.php

### 1-1 : 登入taiwania後，使用terminal，在個人目錄下(~/)，輸入以下指令

```shell
module load anaconda3/5.1.10
conda create --prefix ~/condapy3 python=3 anaconda
```

### 1-2 : 等他跑完(可能會很久)，中間會要你確認是否要繼續進行，輸入 y

```
proceed ([y]/n)? y
```

### 範例 : 因為真的要等很久，所以我就不跑了
![setConda](https://imgur.com/gRlfgCm.jpg)

## 2. Introduction of Sample Script
最佳化過程會使用到的Script主要有三種

### 2-1 : DBS_lsf中一些檔案

#### setBase.lsf - 建立還沒蝕刻的元件原型

#### setHole.lsf - 挖洞

#### delHole.lsf - 刪洞

#### setSimu.lsf - 設定 monitor, source 等

#### getData.lsf - 可以寫你自己的FOM

#### DBS20by20_ini.txt - 初始值, 範例是全部都填洞

#### main.lsf - 在最佳化過程中用不到，但可以拿來確認你的其他lsf有沒有寫錯

### 範例結構
![DBS_ini](https://imgur.com/AnbpgLb.jpg)

![DBS__399_93%](https://imgur.com/FlGpLLH.jpg)

### 2-2 : .sh file
提交模擬job用, 可以自己設定資源 

### 2-3 : 演算法跟資料處理 放在pyScript中，另外還有一個main.py
#### buildOptPath.py - 會在workPath下建立一個optPath, 再在其中建立 ./Gen_n/p_m/ 等等..., 很多資料夾

#### buildInitialPattern.py - 會用到lumapi, 配合txt建立元件結構初始值(.fsp)

#### simuFDTD.py - 專門用來qsub並確認是否完成, 需在進入此sciprt前, 將變數fspPath設為你要做FDTD的那個fsp檔

#### DBSflow.py - opt流程, 要自己寫alg就改這個檔案

#### main.py - 會依序呼叫上面的.py
跑自動最佳化模擬就直接跑main.py就好

## 3. Example
![workPath](https://imgur.com/j2502N2.jpg)

![workExp](https://imgur.com/V2STS2D.jpg)

## 4. Complement
### A. 預設是每模擬10次, 會寄一次模擬結果信, 可以自己改寄信頻率, 在simuFDTD.py中
![mail](https://imgur.com/E6B8yVV.jpg)
### B. lumerical的python api有時候會秀抖, 不能打開fsp, 或他自己關掉, 所以DBSflow.py包了幾個迴圈, 防止程式中止, 如果要自己寫script可以參考一下
![robusten](https://imgur.com/gEmcpP4.jpg)
### C. 台灣杉好像有判定你為idle後踢掉連線的設定... 待解決, 目前是在本地電腦用ahk自動點ThinLinc= =
