import datetime
from selenium import webdriver
from selenium.webdriver.support.select import Select
import chromedriver_binary
import time
import re
import json

# 取得するシラバスの年度
year = datetime.datetime.now().strftime("%Y")

# Seleniumオプション設定
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument("--headless")

# Chromeドライバ起動
driver = webdriver.Chrome()

# 東洋大学のシラバスデータベースシステムへアクセス
driver.get("https://g-sys.toyo.ac.jp/syllabus/")

# 読み込み待機
time.sleep(3)

# 開講年度を設定
Select(driver.find_element_by_xpath(
    "/html/body/div[3]/div/div/div/div/div/div/div[3]/form/table/tbody/tr[1]/td/select")).select_by_value(year)

# 学部を情報連携学部に設定
Select(driver.find_element_by_xpath(
    "/html/body/div[3]/div/div/div/div/div/div/div[3]/form/table/tbody/tr[3]/td/select")).select_by_value("1F000-2017")

# 検索結果の表示件数を1000件に強制設定
driver.execute_script(
    "document.getElementById('perPage').options[0].value = '1000';")
Select(driver.find_element_by_xpath(
    "/html/body/div[3]/div/div/div/div/div/div/div[3]/form/table/tbody/tr[14]/td/select")).select_by_value("1000")

# 検索実行
driver.find_element_by_xpath(
    "/html/body/div[3]/div/div/div/div/div/div/div[3]/form/div[2]/input[1]").click()

# 読み込み待機
time.sleep(3)

# 検索結果の該当件数
total = int(re.findall(r"\d+", driver.find_element_by_xpath(
    "/html/body/div[3]/div/div/div/div[1]").get_attribute("innerText"))[1])

# 追加していくためのJSON
result = []

# 一つずつJSONにして追加
for i in range(total):
    xpath = "/html/body/div[3]/div/div/div/table[2]/tbody/tr[" + str(i + 1) + "]"

    # 雛形
    obj = {
        "@type": "terachan:INIADSyllabus",
        "dc:date": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S+09:00"),
        "owl:sameAs": "terachan.INIADSyllabus:" + year + "." + str(i + 1),
        "dc:title": None,
        "terachan:courseTitle": {
            "ja": None,
            "en": None
        },
        "terachan:courseYear": int(year),
        "terachan:courseNo": i + 1,
        "terachan:courseSemester": None,
        "terachan:courseWeek": None,
        "terachan:coursePeriod": None,
        "terachan:courseLanguage": None,
        "terachan:courseStudyYear": None,
        "terachan:instructorName": [],
        "terachan:instructorType": None,
        "terachan:syllabusNo": {
            "ja": None,
            "en": None
        }
    }

    # 科目名
    courseTitle = driver.find_element_by_xpath(
        xpath + "/td[3]").get_attribute("innerText").splitlines()
    if len(courseTitle) == 2:
        obj["dc:title"] = courseTitle[0]
        obj["terachan:courseTitle"]["ja"] = courseTitle[0]
        obj["terachan:courseTitle"]["en"] = courseTitle[1]

    # 開講学期
    courseSemester = driver.find_element_by_xpath(
        xpath + "/td[2]").get_attribute("innerText").splitlines()
    if len(courseSemester) == 2:
        obj["terachan:courseSemester"] = courseSemester[1]

    # 曜日・時限
    courseTime = driver.find_element_by_xpath(
        xpath + "/td[5]").get_attribute("innerText").splitlines()
    if len(courseTime) == 2:
        if courseTime[1].split(",")[0] != "None" and courseTime[1].split(",")[1] != "Intensive":
            obj["terachan:courseWeek"] = courseTime[1].split(",")[0]
        if courseTime[1].split(",")[1] != "None" and courseTime[1].split(",")[1] != "Intensive":
            obj["terachan:coursePeriod"] = int(courseTime[1].split(",")[1][0])

    # 主たる使用言語
    courseLanguage = driver.find_element_by_xpath(
        xpath + "/td[7]").get_attribute("innerText").split(" / ")
    if len(courseLanguage) == 2:
        obj["terachan:courseLanguage"] = courseLanguage[1]

    # 対象年次
    courseStudyYear = driver.find_element_by_xpath(
        xpath + "/td[6]").get_attribute("innerText")
    studyYear = []
    for y in range(int(courseStudyYear[0]), int(courseStudyYear[-1])+1):
        studyYear.append(y)
    obj["terachan:courseStudyYear"] = studyYear

    # 教員名
    instructorName = driver.find_element_by_xpath(
        xpath + "/td[4]").get_attribute("innerText").splitlines()
    if len(instructorName) > 0:
        name = []
        for n in range(len(instructorName)):
            if len(instructorName[n].split(" / ")) == 2:
                name.append({
                    "ja": instructorName[n].split(" / ")[0].replace('　', ' '),
                    "en": instructorName[n].split(" / ")[1].replace('　', ' ')
                })
        obj["terachan:instructorName"] = name

    instructorType = driver.find_element_by_xpath(
        xpath + "/td[8]").get_attribute("innerText").split("/")
    if len(instructorType) == 2:
        obj["terachan:instructorType"] = instructorType[1][5]

    # シラバス番号(ja)
    syllabusNoJa = driver.find_element_by_xpath(
        xpath + "/td[9]/div").find_elements_by_class_name("btn_syllabus_jp")
    if len(syllabusNoJa) != 0:
        q = re.findall(r'\d+', syllabusNoJa[0].get_attribute("onclick"))
        obj["terachan:syllabusNo"]["ja"] = int(q[1])

    # シラバス番号(en)
    syllabusNoEn = driver.find_element_by_xpath(
        xpath + "/td[9]/div").find_elements_by_class_name("btn_syllabus_en")
    if len(syllabusNoEn) != 0:
        q = re.findall(r'\d+', syllabusNoEn[0].get_attribute("onclick"))
        obj["terachan:syllabusNo"]["en"] = int(q[1])

    # JSONに追加
    result.append(obj)

# ファイルに保存
df = open("./data/"+year+"/syllabus.json", "w",  encoding="utf-8")
json.dump(result, df, ensure_ascii=False)

# Chromeドライバ終了
driver.quit()
