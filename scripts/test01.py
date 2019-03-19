import os
import sys
sys.path.append(os.getcwd())
import allure
import pytest

class Test01:
    @allure.step('新增地址方法被执行')
    def test01(self):
        allure.attach('点击新增地址按钮：','')
        allure.attach('点击新增输入收件人：', '')
        allure.attach('点击新增输入手机号：', '')
        allure.attach('点击新增输入收货地址：', '')
        allure.attach('点击新增输入点击新增：', '')
        print('test01被执行')
    @allure.step
    def test02(self):
        print("test02被执行")

    #失败截图并写入报告
    def test03(self):
        print('断言失败，截图并写入报告')
        with open ('./image/faile.png','rb')as f:
            allure.attach('失败原因：',f.read(),allure.attach_type.PNG)
