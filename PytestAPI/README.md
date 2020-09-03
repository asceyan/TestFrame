## 项目说明

### 接口自动化框架

pytest + requests + allure 

### 项目结构

| 项目结构         | 说明              |
| :--------------- | :---------------- |
| case             | 用例层            |
| common           | 底层封装          |
| config           | 配置层            |
| log              | 存放日志          |
| report           | 存放allure报告    |
| conftest         | 项目的全局变量    |
| nb_log_config.py | nb_log 的配置文件 |
| pytest.ini       | pytest 的配置文件 |
| run.py           | 执行文件          |

### 环境准备

python 3.7

pytest==4.5.0

requests==2.23.0

allure-pytest==2.8.6

nb_log

### 依赖包安装

使用pip安装依赖包

cd 进入项目根目录

pip install –r requirements.txt

### 执行用例

根目录执行run.py

### 查看allure报告

cd 进入report/report-0901100159

allure serve ./result