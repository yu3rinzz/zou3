from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def attach_to_existing_chrome_Comment():
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)

    driver.get("https://jp.mercari.com/mypage/listings")
    time.sleep(3)  # ページ読み込み待機

    # 商品一覧のコンテナを取得
    items = driver.find_elements(By.XPATH, '//mer-item-thumbnail')

    for item in items:
        try:
            # 商品名だけを取得して表示
            name_p = item.find_element(By.XPATH, './/p[@data-testid="item-label"]')
            print(name_p.text)
        except Exception as e:
            print(f"商品名取得失敗: {e}")

if __name__ == "__main__":
    attach_to_existing_chrome_Comment()