#!/usr/bin/env python
# encoding: utf-8
#author: Jim Yin

#!/usr/bin/env python
#coding=utf-8

import sys
import os
import pytest
import subprocess
import logging
import allure


#为什么我们要设置这个路径到pythonPATH
sys.path.append(os.path.dirname(sys.modules[__name__].__file__))

fileHandler = logging.FileHandler(filename="../log/uiauto.log",encoding="utf-8")
logging.getLogger().setLevel(0)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
fileHandler.setFormatter(formatter)

logging.getLogger().addHandler(fileHandler)


if __name__ == '__main__':


    #pytest.main(['-sq', '--alluredir', '../log/testreport', 'testcases/myselector/test_all_stocks.py'])
    pytest.main(['-sq', '--alluredir', '../log/testreport', 'testcases/login','testcases/myselector'])
    #pytest.main(['-sq', '--alluredir', '../log/testreport','--allure_severities=blocker', 'testcases/'])
    print(subprocess.getstatusoutput('allure generate --clean ../log/testreport/ -o ../log/testreport/html'))
    #print(subprocess.getstatusoutput('allure generate  ../log/testreport/ -o ../log/testreport/html'))