# -*- coding: utf-8 -*-
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DATA_PATH = os.path.join(BASE_PATH, 'data')
CASE_PATH = os.path.join(BASE_PATH, 'case')
REPORT_PATH = os.path.join(BASE_PATH, 'report', '')
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
CONFIG_FILE = os.path.join(CONFIG_PATH, 'config.ini')
LOG_PATH = os.path.join(BASE_PATH, 'log', '')



