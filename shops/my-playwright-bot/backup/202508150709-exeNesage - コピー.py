import datetime
import csv
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 変更前の価格を取得する関数
def before_price(driver):
    try:
        # <input name="price"> 要素を取得
        price_input = driver.find_element(By.NAME, "price")

        # value属性から価格を取得
        price_value = price_input.get_attribute("value")

        #print(f"before-price: {price_value}")
        return price_value
    except Exception as e:
        print(f"before価格取得失敗: {e}")
        return None



# 値下げ実行部分を関数化
def price_down(item_code):
    """商品番号を指定して値下げ処理を実行"""
    options = Options()
    options.add_argument(r"--user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data")
    options.add_argument("--disable-features=DevToolsDebuggingRestrictions")
    options.add_argument("--start-maximized")
    options.add_argument("--profile-directory=Default")

    driver = webdriver.Chrome(options=options)
    try:
        url = f"https://jp.mercari.com/sell/edit/{item_code}"
        driver.get(url)
        print(f"値下げページを開きました: {url}")

        # ページを読み込み終わるまで待機（ランダムで）
        time.sleep(random.uniform(5,6))

        # 変更前の価格を数値として取得（関数から取得）
        current_price = before_price(driver)
        #print(current_price)
        print(f"現在の価格: {current_price}")

        #########
        # 100円値下げ
        if current_price is not None:
            after_price = int(current_price) - 100
            print(f"変更後の価格: {after_price}")

            # <input name="price"> 要素を再取得して値をクリア＆入力
            price_input = driver.find_element(By.NAME, "price")
            time.sleep(0.5)  # 0.5秒待機
            
            #price_input.clear()
            # すべて選択してDelete
            price_input.send_keys(Keys.CONTROL, 'a')  # 全選択
            time.sleep(0.3)
            price_input.send_keys(Keys.DELETE)        # 削除
            
            time.sleep(0.3)  # 0.5秒待機
            price_input.send_keys(str(after_price))

            #print("新しい価格を入力しました。")
            time.sleep(random.uniform(1,2))  # 確認のため待機

            # 「変更する」ボタンをクリック
            try:
                # data-testid="edit-button" を持つ「変更する」ボタンを取得してクリック
                save_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="edit-button"]')
                # 変更するボタンのクリック
                save_button.click()
                print("保存ボタン（変更する）をクリックしました。")
            except Exception as e:
                print(f"保存ボタンのクリックに失敗: {e}")

            time.sleep(random.uniform(2,3))  # 確認のため待機
        else:
            print("価格取得に失敗したため値下げできませんでした。")



        # # 変更後の価格（ここでは100円値下げ）
        # after_price = int(current_price) - 100
        # print(f"変更後の価格: {after_price}")

        # time.sleep(random.uniform(2,3))     # 確認のため待機

        print("=================================")

    except Exception as e:
        print(f"⚠ 値下げ処理でエラー: {e}")
    finally:
        driver.quit()


# item-list.txt をCSVとして読み込み、3列目の商品番号を抜き出して表示
with open("item-list.txt", "r", encoding="utf-8") as f:
    reader = list(csv.reader(f))
    # ランダムに並び替え
    random.shuffle(reader)


    # 除外する時間帯（カンマ区切りで指定、例："1,2,3,4"） 2025.08.14追加
    EXCLUDE_HOURS = [int(h) for h in "2,3,4,5,10,14,15,16".split(",")]


    # 4列目の商品番号を表示
    for row in reader:
        if len(row) >= 4:
            print(row[0],row[3])


            # 現在時刻のhourを取得 2025.08.14追加
            now_hour = datetime.datetime.now().hour
            if now_hour in EXCLUDE_HOURS:
                print(f"{now_hour}時台なので値下げ処理をスキップします。")
                continue  # 次の商品へ


            # 値下げの処理
            print("待機開始:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            #time.sleep(random.uniform(1,4))  # ランダムな待機時間
            #time.sleep(random.uniform(300,900))  # ランダムな待機時間 10分間隔
            #time.sleep(random.uniform(360,1080))  # ランダムな待機時間 12分間隔
            #time.sleep(random.uniform(720,1080))  # ランダムな待機時間 15分間隔 ゴールデンタイム
            #time.sleep(random.uniform(900,1700))  # ランダムな待機時間 21.6分間隔
            time.sleep(random.uniform(1100,1800))  # ランダムな待機時間 24分間隔
            #time.sleep(random.uniform(1400,2200))  # ランダムな待機時間 30分間隔
            print("待機終了:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            item_code = row[3]  # 商品番号を取得
            print(f"商品番号: {item_code} の値下げ処理を実行中...")
            print("https://jp.mercari.com/sell/edit/" + item_code)



            try:
                # 値下げ実行
                price_down(item_code)
            except Exception as e:
                print(f"この商品の値下げ処理でエラーが発生しました（スキップします）: {e}")
                continue  # 次の商品へ
