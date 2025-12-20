from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re


def run_with_chrome_profile():
    options = Options()
    # Chromeのユーザーデータディレクトリを指定
    options.add_argument(r"--user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data") 

    options.add_argument("--disable-features=DevToolsDebuggingRestrictions")
    # 追加
    options.add_argument("--start-maximized")  # ブラウザを最大化して起動


    # プロファイル名を指定（chrome://version で確認できる）
    #options.add_argument("--profile-directory=Profile 2")
    options.add_argument("--profile-directory=Default")

    driver = webdriver.Chrome(options=options)

    driver.get("https://jp.mercari.com/mypage/listings")

    ### 追加
    try:
        # 「もっと見る(20)」ボタンが表示されるのを最大15秒待つ
        #wait = WebDriverWait(driver, 15)
        wait = WebDriverWait(driver, 3)
        more_button = wait.until(
            EC.element_to_be_clickable((By.ID, "auto-more-loader"))
        )

        # ボタンが見つかったらクリック
        #more_button.click()
        #print("「もっと見る(20)」ボタンをクリックしました")


        # ② 40秒間待機（データロード時間）
        #time.sleep(60)  # 必要に応じて変更
        time.sleep(5)  # 必要に応じて変更

        # ③ Enterキーを送信してダイアログを閉じる（アクティブ要素に対して送信）
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
        print("✅ Enterキーを送信しました（ダイアログ閉じ）")

    except Exception as e:
        print("⚠ エラー発生（もっと見る or Enter処理）:", e)


####################

    # ④ 「2日前」の要素をすべて取得して、価格も表示
    try:
        #spans = driver.find_elements(By.XPATH, '//span[text()="2日前"]')
        # テキストに '日前' を含み、かつ '1日前' でない」span要素をすべて取得する
        #spans = driver.find_elements(By.XPATH, '//span[contains(text(),"日前") and not(text()="1日前")]')
        #spans = driver.find_elements(By.XPATH, '//span[contains(text(),"日前に更新") and not(text()="1日前に更新")]')
        # 

        #price_down_obj = spans

        #print(f"\n✅ 「〇日前（1日前を除く）」の要素が {len(price_down_obj)} 件 見つかりました:")
        for idx, elem in enumerate(price_down_obj, start=1):
            try:
                # 祖先の <a data-testid="listed-item"> を起点に検索
                # 商品全体の<a data-testid="listed-item"> を取得
                container = elem.find_element(By.XPATH, "./ancestor::a[@data-testid='listed-item']")

                ### 追加 ### 商品番号
                # href属性から item-code を取得（例: m19646357504）
                href = container.get_attribute("href")
                match = re.search(r'/item/(m\d{11})', href)
                item_code = match.group(1) if match else "ID取得失敗"


                # 金額部分だけを含む <span class="jdmOYL kpXXdK hGHvhs"> のうち2番目（¥の次）を取得
                price_spans = container.find_elements(By.XPATH, './/span[@class="jdmOYL kpXXdK hGHvhs"]')
                if len(price_spans) >= 2:
                    current_price = price_spans[1].text.replace(",", "").replace("¥", "").strip()
                else:
                    current_price = "価格取得失敗"

            except Exception as e:
                current_price = f"取得エラー: {e}"

            # 抽出結果を出力
            # CSVに書き出し 全ての出力の場合
            #print(f"{idx},{elem.text},{current_price},{item_code}")

            # current_price が数値かつ3000円以上の場合のみ item-list.txt に書き出し
            try:
                if current_price.isdigit() and int(current_price) >= 3000:
                    print(f"{idx},{elem.text},{current_price},{item_code}")
            except Exception:
                pass


    except Exception as e:
        print("⚠ エラー発生（〇日前（1日前を除く）要素の抽出）:", e)




    # # 終了前に待機（任意）
    time.sleep(60)
    driver.quit()

if __name__ == "__main__":
    run_with_chrome_profile()
