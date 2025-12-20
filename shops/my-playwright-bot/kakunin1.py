from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def attach_to_existing_chrome():
    options = Options()
    # 既存Chrome(ステップ2)に接続
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # Selenium Managerに任せる（ChromeDriverのパス指定は不要）
    driver = webdriver.Chrome(options=options)

    driver.get("https://jp.mercari.com/mypage/listings")
    time.sleep(300)

if __name__ == "__main__":
    attach_to_existing_chrome()














# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import re


# def run_with_chrome_profile():
#     options = Options()
#     # Chromeのユーザーデータディレクトリを指定
#     #options.add_argument(r"--user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data") 
#     options.add_argument(r"--user-data-dir=C:\Users\user\chrome-profile-selenium\User Data")

#     options.add_argument("--disable-features=DevToolsDebuggingRestrictions")
#     # 追加
#     options.add_argument("--start-maximized")  # ブラウザを最大化して起動


#     # プロファイル名を指定（chrome://version で確認できる）
#     options.add_argument("--profile-directory=Default")
#     #options.add_argument("--profile-directory=Profile 2")

#     driver = webdriver.Chrome(options=options)

#     driver.get("https://jp.mercari.com/mypage/listings")
#     #driver.get("https://www.google.com/")

#     time.sleep(300)  # 必要に応じて変更



# if __name__ == "__main__":
#     run_with_chrome_profile()
