# Install Lumerical on Taiwania

## 0. Taiwania Manual 
安裝範例是在圖形化介面下進行

請參考[taiwania使用者操作手冊 2.4.2](https://drive.google.com/file/d/1Dfvzk2XCij7xsMjAPPVNzH4izbnAWXy5/view?usp=sharing), 使用ThinLinc登入互動式節點後安裝

## 1. LumFile
### 1-1 : 打開瀏覽器下載[這個壓縮檔](https://reurl.cc/mq1aQV)
![shorten](https://imgur.com/sVCf2ur.jpg)

### 1-2 : 把它放在你的home底下, 如下圖
![putFileToHome](https://imgur.com/YXWuH8z.jpg) 

### 1-3 : 將它解壓縮, 如下圖
![extract](https://imgur.com/cOlaay0.jpg)

### 1-4 : 進入LumFile的資料夾, 打開testjob.sh, 把使用者信箱改成你自己的, 如下圖
![edit job template](https://imgur.com/JJEg7B0.jpg)

## 2. Install
### 2-1 : 在LumFile資料夾下點右鍵, 選擇 Open in Terminal, 如下圖
![openInTerminal](https://imgur.com/tVzxOIW.jpg)

### 2-2 : 建議先調整terminal的主題, 不然字很不清楚, 如下圖
![terminal theme](https://imgur.com/ZzLj9kz.jpg)

### 2-3 : 在打開的terminal中, 輸入指令便會自動安裝Lumerical, 如下圖
```
sh LumericalInstaller.sh
```
![lum installer](https://imgur.com/0AOKROA.jpg)

### 2-4 : 打開lumerical, 如下圖
![launcher path](https://imgur.com/I8ghKcM.jpg)

### 2-5 : 用lumerical打開LumFile資料夾中的grating_coupler_2D.fsp, 確認模擬是否成功, 如下圖
![result](https://imgur.com/Qpp0Yp9.jpg)


## 3. Complement
### 3-1 : 若確認fsp已有包含模擬結果了, 代表lumerical已安裝成功, 同步驟 2-1 打開terminal
![openInTerminal](https://imgur.com/tVzxOIW.jpg)

### 3-2 : 使用指令清除安裝過程中的檔案, 如下圖
```
sh afterInstall.sh
```
![clean](https://imgur.com/Lihh2fg.jpg)

### 3-3 : Home底下會保留原本的壓縮檔, 另外會複製一份用來提交模擬運算的jobTemplate.sh於Home底下, 可以參考裡面的寫法來做其他fsp的模擬
