#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class DriverManager:
    __driver = 0

    def __init__(self,type):
        if "ie"==type:
            self.driver = webdriver.Ie();
        elif "chrome"==type:
            self.driver = webdriver.Chrome();
        elif "firefox"==type:
            self.driver = webdriver.Firefox();
        else:
            print ("没有指定打开任何浏览器");

    def get_driver(self):
        return self.driver;

    def into_index(self,url=""):
        self.driver.get(url)

    #通过id,xpath,name查找元素
    def find_element(self,id="",name="",xpath=""):
        if id:
            element = self.driver.find_element_by_id(id);
        elif name:
            element = self.driver.find_element_by_name(name);
        else:
            element = self.driver.find_element_by_xpath(xpath);
        return element;

    #向指定id或者name或者xpath的元素内输入内容
    def send_value(self,id="",name="",xpath="",value=""):
        element = self.find_element(id,name,xpath)
        element.send_keys(value)

    #点击指定的元素
    def click_element(self,id="",name="",xpath=""):
        element = self.find_element(id,name,xpath);
        element.click();

    #向有日期标签的元素框内输入内容
    def input_date(self,id="",name="",xpath="",value=""):
        js = "document.getElementById('"+id+"').removeAttribute('readonly')";
        self.driver.execute_script(js);
        self.send_value(id,name,xpath,value);

    #跳转到指定的frame
    def switch_frame(self,id="",name="",xpath=""):
        self.driver.switch_to.default_content()
        element = self.find_element(id,name,xpath)
        self.driver.switch_to.frame(element)


    #通过index,value,text选择下拉框对应的元素
    def switch_option(self,id="",name="",xpath="",index=-1,value="",text=""):
        elment = self.find_element(id,name,xpath);
        select = Select(elment);
        if index>-1:
            select.select_by_index(index);
        elif value:
            select.select_by_value(value);
        elif text:
            select.select_by_visible_text(text);
        else:
            print ("没有输入选择条件");

    # 指定等待某一个元素
    def wait_ele(self,driver, second, xpath=""):
        while second > 0:
            try:
                driver.find_element_by_xpath(xpath);
                return;
            except:
                print("元素不存在,再等待" + str(second) + "秒");
                time.sleep(1);
                second -= 1;
        driver.find_element_by_xpath(xpath);



