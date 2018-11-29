from auto_test.driver_manager import DriverManager
import time

class EmpManager:
    driver = 0
    dm = 0

    def __init__(self,type="chrome"):
        self.dm = DriverManager(type)
        self.driver = self.dm.get_driver()

    def goto_index(self):
        self.dm.into_index("localhost:8081/crm")

    def login(self):
        self.dm.send_value(name="userNum",value="admin")
        self.dm.send_value(name="userPw",value="123456")
        self.dm.find_element(id="in1").click()
        time.sleep(3)

    def emp_info(self):
        ele = self.driver.find_element_by_xpath(xpath="/html/frameset/frameset")
        self.driver.switch_to.frame(ele)
        self.driver.switch_to.frame(1)
        ele1 = self.driver.find_element_by_link_text("员工信息")
        ele1.click()
