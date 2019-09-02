#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main_pytest.py.py
# @Author: LILIANG
# @Date  : 2019/8/30
# @Desc  :  test
import pytest

# pytest.main(["-s","-v","-m","smoke","--alluredir=/Outputs/allure_reports"])
# 添加重运行机制
pytest.main(["-s","-v","-m","smoke","--reruns","2","--reruns-delay","5","--alluredir=Outputs//allure_reports"])
