## 项目说明

### WEB UI 自动化框架

unittest+ selenium+ beautifulreport

### 项目结构

| 项目结构 | 说明                                               |
| :------- | :------------------------------------------------- |
| case     | 用例层，存放用例文件                               |
| common   | 底层封装，二次封装selenium和其他工具类             |
| config   | 配置层，配置全局变量、路径                         |
| data     | 生成、存放测试数据                                 |
| log      | 生成日志                                           |
| img      | 存放错误截图，用例失败后可在报告中点击详情查看截图 |
| report   | 存放report测试报告                                 |
| run.py   | 执行文件                                           |

### 环境准备

python 3.7

selenium

beautifulreport

### 依赖包安装

使用pip安装依赖包

cd 进入项目根目录

pip install –r requirements.txt

### 执行用例

根目录执行run.py

### 查看测试报告

![image-20200901163012653](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20200901163012653.png)