from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    import undetected_chromedriver as uc
    url = 'https://api.myip.com/'
    my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
  
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument(f"user-agent={my_user_agent}")
  
    # Initialize Chrome WebDriver with the specified options
    driver = uc.Chrome(options=options)
    driver.get(url)
    page_source = driver.page_source
    driver.quit()
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
