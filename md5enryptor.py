from selenium import webdriver
from bs4 import BeautifulSoup
import hashlib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

url = "http://167.172.58.213:31289/"
driver = webdriver.Firefox()
driver.get(url)
source = driver.page_source
soup = BeautifulSoup(source, "html.parser")
md5 = computeMD5hash(soup.find_all("h3")[0].getText())
driver.find_element(By.NAME,"hash").send_keys(md5)
driver.find_element(By.XPATH, "/html/body/center/form/input[2]").click()
source = driver.page_source
print(source)
driver.quit()
