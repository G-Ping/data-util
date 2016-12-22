#!/usr/bin/python
# -*- coding: gb2312 -*-
'''从bug.xlsx中获取bug编号，将禅道上对应bug导出'''

import os
import time
import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import key
import xlrd

class zentao():
    def __init__(self):
        
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/zentao/bug-browse.html"
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_id("submit").click()
       

    def bug_search1(self,a,b,c,d,e,f):
        driver = self.driver
        driver.maximize_window()
        driver.find_element_by_xpath("//li[@id='bysearchTab']/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@id='searchmore']/i").click()
        Select(driver.find_element_by_id("field1")).select_by_visible_text(u"Bug编号")
        driver.find_element_by_id("value1").clear()
        driver.find_element_by_id("value1").send_keys(a)
        Select(driver.find_element_by_id("andOr2")).select_by_visible_text(u"或者")
        driver.find_element_by_id("value2").clear()
        driver.find_element_by_id("value2").send_keys(b)
        Select(driver.find_element_by_id("andOr3")).select_by_visible_text(u"或者")
        Select(driver.find_element_by_id("field3")).select_by_visible_text(u"Bug编号")
        driver.find_element_by_id("value3").clear()
        driver.find_element_by_id("value3").send_keys(c)
        Select(driver.find_element_by_id("groupAndOr")).select_by_visible_text(u"或者")
        Select(driver.find_element_by_id("field4")).select_by_visible_text(u"Bug编号")
        driver.find_element_by_id("value4").clear()
        driver.find_element_by_id("value4").send_keys(d)
        Select(driver.find_element_by_id("andOr5")).select_by_visible_text(u"或者")
        Select(driver.find_element_by_id("field5")).select_by_visible_text(u"Bug编号")
        driver.find_element_by_id("value5").clear()
        driver.find_element_by_id("value5").send_keys(e)
        Select(driver.find_element_by_id("andOr6")).select_by_visible_text(u"或者")
        Select(driver.find_element_by_id("field6")).select_by_visible_text(u"Bug编号")
        driver.find_element_by_id("value6").clear()
        driver.find_element_by_id("value6").send_keys(f)
        driver.find_element_by_id("submit").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@id='searchlite']/i").click()
        driver.find_element_by_xpath("//li[@id='bysearchTab']/a").click()
        driver.find_element_by_xpath("//li[@id='bysearchTab']/a").click()

    def dao(self):
        driver = self.driver
        driver.find_element_by_id("reversechecker").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_link_text(u"导出数据").click()
        time.sleep(1)
        driver.switch_to.frame("modalIframe")
        driver.find_element_by_id("fileName").clear()
        driver.find_element_by_id("fileName").send_keys("1")
        Select(driver.find_element_by_id("encode")).select_by_visible_text("GBK")
        Select(driver.find_element_by_id("exportType")).select_by_visible_text(u"选中记录")
        ele = driver.find_element_by_id("submit")
        ele.click()
        ActionChains(driver).click(ele).perform()
        time.sleep(1)
        key.key_down( 'alt' )
        key.key_input1( 's' )
        key.key_up( 'alt' )
        key.key_input1( 'enter' )
        driver.switch_to.default_content()

        
def OnlyCharNum(s,oth=''):
    fomart = '0123456789'  #fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for c in s:
        if not c in fomart:
            s = s.replace(c,'')
    return s[0:4]

def get_bugId():
    data = xlrd.open_workbook('bug.xlsx')
    table = data.sheets()[0]
    nrows = table.nrows
    bugId = {}
    j=0
    for i in range(nrows):
        str0=table.row_values( i )
        str2 =','.join(str0)
        s= OnlyCharNum(str2)
        if len(s)>3:
            bugId[j]=s
            #print bugId[j]
            j=j+1
            
    return bugId

if __name__ == "__main__":         
    bugid = get_bugId()    
    '''6个一组'''
    j = len(bugid)/6 + 1
    k = j * 6
    b = [9999]*k
    for i in range(len(bugid)):
        b[i]=bugid[i]

    z = zentao()
    for n in range(j):
        p = n * 6
        z.bug_search1(b[p],b[p + 1],b[p + 2],b[p + 3],b[p + 4],b[p + 5])
        z.dao()
 




