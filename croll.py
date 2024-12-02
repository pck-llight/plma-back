
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time
import json

url = 'https://www.tjmedia.com/tjsong/song_search.asp'
want = '어디에도'

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 창을 띄우지 않는 옵션
options.add_argument("--disable-gpu")  # GPU 비활성화 (Windows 환경에서 필요할 수 있음)
options.add_argument("--no-sandbox")  # Linux에서 권한 관련 문제 방지
options.add_argument("--disable-dev-shm-usage")  # /dev/shm 파티션 크기 문제 방지

# 크롬드라이버 실행
driver = webdriver.Chrome(options=options)

#크롬 드라이버에 url 주소 넣고 실행
driver.get(url)
time.sleep(0.5)
search_box = driver.find_element(By.XPATH, '//*[@id="searchSong"]/form/ul[1]/li/input')
print(search_box)
search_box.send_keys(want)
search_box.send_keys(Keys.ENTER)
# time.sleep(0.5)
result_box = driver.find_element(By.XPATH, '/html/body/div/div[3]/div[3]/form/div[2]/table/tbody')
print(result_box.text)
# print(result_box)
# driver.quit()
rows = result_box.find_elements(By.TAG_NAME, "tr")

results = []
for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")  # 각 열 가져오기
        if len(cols) > 0:  # 데이터가 있는 행만 처리
            data = {
                "번호": cols[0].text.strip(),
                "곡명": cols[1].text.strip(),
                "가수": cols[2].text.strip(),
                "작곡": cols[3].text.strip(),
                "작사": cols[4].text.strip(),
            }
            results.append(data)
            # JSON 형태 출력
            json_results = json.dumps(results, ensure_ascii=False, indent=4)
print(json_results)