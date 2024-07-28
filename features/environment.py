from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")
    context.driver = webdriver.Chrome(options=options)
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')

def after_all(context):
    context.driver.quit()