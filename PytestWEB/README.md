## 项目说明

### 接口自动化框架

pytest + selenium+ allure 

### 项目结构

| 项目结构 | 说明                                           |
| :------- | :--------------------------------------------- |
| case     | 用例层，存放用例文件                           |
| common   | 公共层，封装selenium、shell、工具类等          |
| config   | 配置层，定义全局参数                           |
| log      | 存放日志                                       |
| report   | 存放allure报告                                 |
| page     | 存放页面元素，把页面元素定位和页面元素操作分开 |
| run.py   | 执行文件                                       |

### 环境准备

python 3.7

pytest==4.5.0

allure-pytest==2.8.6

selenium

nb_log

### 执行用例

根目录执行run.py

### 查看allure报告

allure serve ./result