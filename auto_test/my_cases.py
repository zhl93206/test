# pyhton3.X默认UTF-8编码，无需设置
# 编码设置方式：在文件开头  #coding=utf-8
from auto_test.user_manager import EmpManager
import unittest


class MyCases(unittest.TestCase):
    em = 0

    @classmethod
    def setUpClass(cls):
        print("测试开始了")
        cls.em = EmpManager()

    @classmethod
    def tearDownClass(cls):
        print("测试结束了")
        # #关闭浏览器驱动
        cls.em.driver.close()

    def test01_crm_index(self):
        self.em.goto_index()

    def test01_crm_login(self):
        self.em.login()

    def test01_crm_emInfo(self):
        self.em.emp_info()
