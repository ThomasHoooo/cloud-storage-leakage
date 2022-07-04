from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
options = Options()
options.add_argument("--headless")

websites = set()
driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'),options=options)
for i in range(1, 27):
    driver.get("https://www.semrush.com/blog/sp-500/?page=%s" % (i))
    for element in driver.find_elements(by=By.CLASS_NAME, value="___SText_jyp83_gg_"):
        websites.add(element.text)

with open('S&P top 500.txt', 'w') as f: 
    for website in websites:
        f.write(website+"\n")
