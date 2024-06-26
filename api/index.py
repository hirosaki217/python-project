from http.server import BaseHTTPRequestHandler
import os
import undetected_chromedriver as uc
from tempfile import mkdtemp
from selenium import webdriver
from selenium.webdriver.common.by import By    

class handler(BaseHTTPRequestHandler):
    driver_path = '/tmp/chromedriver'
    browser_path = '/opt/chrome/chrome'

    os.system(f'cp /opt/chromedriver {driver_path}')
    os.chmod(driver_path, 0o777)

    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280x1696')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-dev-tools')
    options.add_argument('--no-zygote')
    options.add_argument(f'--user-data-dir={mkdtemp()}')
    options.add_argument(f'--data-path={mkdtemp()}')
    options.add_argument(f'--disk-cache-dir={mkdtemp()}')
    options.add_argument('--remote-debugging-port=9222')

    chrome = uc.Chrome(options, driver_executable_path=driver_path, browser_executable_path=browser_path)
    chrome.get('https://google.com/')
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(chrome.find_element(by=By.XPATH, value='//html').text.encode('utf-8'))
        return
