# 作成中プログラム 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re



def attach_to_existing_chrome_Comment():
    options = Options()
    # 既存Chrome(ステップ2)に接続
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # Selenium Managerに任せる（ChromeDriverのパス指定は不要）
    driver = webdriver.Chrome(options=options)

    driver.get("https://jp.mercari.com/mypage/listings")
    time.sleep(20)


    # try:
    #     # 「もっと見る(20)」ボタンが表示されるのを最大15秒待つ
    #     wait = WebDriverWait(driver, 25)
    #     more_button = wait.until(
    #         EC.element_to_be_clickable((By.ID, "auto-more-loader"))
    #     )

    #     # ボタンが見つかったらクリック
    #     more_button.click()
    #     print("「もっと見る(20)」ボタンをクリックしました")


    #     # ② xx秒間待機（データロード時間）
    #     time.sleep(60)  # 必要に応じて変更

    #     # ③ Enterキーを送信してダイアログを閉じる（アクティブ要素に対して送信）
    #     webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    #     print("✅ Enterキーを送信しました（ダイアログ閉じる）")

    # except Exception as e:
    #     print("⚠ エラー発生（もっと見る or Enter処理）:", e)




if __name__ == "__main__":
    attach_to_existing_chrome_Comment()