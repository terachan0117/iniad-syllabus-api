# INIAD Syllabus API
東洋大学情報連携学部(INIAD)のシラバスをスクレイピングしてJSONにします。

データは data/{year}/syllabus.json に保存されています。

# Requirement
* Selenium
* Chromedriver

# Installation
## pip
```bash
>> pip install selenium
>> pip install chromedriver-binary
```
## conda
```bash
>> conda install selenium
>> conda install python-chromedriver-binary
```

# Usage
```bash
>> git clone https://github.com/Terachan0117/iniad-syllabus-api.git
>> cd iniad-syllabus-api
>> python main.py
```

## Response example
```json
[
    {
        "@type": "terachan:INIADSyllabus",
        "dc:date": "2020-05-06T17:08:02+09:00",
        "owl:sameAs": "terachan.INIADSyllabus:2020.304",
        "dc:title": "情報連携学概論",
        "terachan:courseTitle": {
            "ja": "情報連携学概論",
            "en": "Introduction to INIAD"
        },
        "terachan:courseYear": 2020,
        "terachan:courseNo": 304,
        "terachan:courseSemester": "Spring",
        "terachan:courseWeek": "Wed",
        "terachan:coursePeriod": 2,
        "terachan:courseLanguage": "Japanese",
        "terachan:courseStudyYear": [
            1,
            2,
            3,
            4
        ],
        "terachan:instructorName": [
            {
                "ja": "坂村 健",
                "en": "Sakamura Ken"
            }
        ],
        "terachan:instructorType": "B",
        "terachan:syllabusNo": {
            "ja": 123189,
            "en": 123189
        }
    }
]
```

## Definition
* それぞれのデータは、`Object`形式で表現されます。
* 値がない場合、`null`が入ります。

| Name | Description | Schema
| ---- | ---- | ---- |
|`@type`|クラス名|`string`
|`dc:date`|データ生成日時（ISO8601 日付時刻形式）|`string (xsd:dateTime)`
|`owl:sameAs`|固有識別子。命名ルールは、terachan.INIADSyllabus:開講年度.科目番号|`string`
|`dc:title`|科目名（日本語）|`string`
|`terachan:courseTitle`|科目名（多言語対応）|`object`
|`terachan:courseYear`|開講年度|`integer`
|`terachan:courseNo`|科目番号|`integer`
|`terachan:courseSemester`|開講学期|`string`
|`terachan:courseWeek`|開講曜日|`string`
|`terachan:coursePeriod`|開講時限|`array`
|`terachan:courseLanguage`|主たる使用言語。"Japanese"：日本語, "English"：英語, "Other Languages"：ドイツ語、フランス語、中国語、韓国語（ハングル）, "Foreign Language Course"：言語の習得を目的とした科目|`string`
|`terachan:courseStudyYear`|対象年次|`object`
|`terachan:instructorName`|教員名（多言語対応）。担当者未決定の場合は空のarray|`array`
|`terachan:instructorType`|教員実務経験種別。"A"：担当教員の実務経験を活かした、実践的教育を行っている科目, "B"：企業等の外部講師を招いてオムニバスなどで実施している科目, "C"：学外のインターンシップ、実習などを授業の中心に位置づけている科目|`string`
|`terachan:syllabusNo`|シラバス番号|`object`


シラバスには以下のURLでアクセスできます。
* 日本語 `https://g-sys.toyo.ac.jp/syllabus/html/gakugai/{terachan:courseYear}/{terachan:courseYear}_{terachan:syllabusNo}.html`
* 英語 `https://g-sys.toyo.ac.jp/syllabus/html/gakugai/{terachan:courseYear}/{terachan:courseYear}_{terachan:syllabusNo}_en.html`

# Note
本APIは、東洋大学及び東洋大学情報連携学部が公式に提供しているものではありません。

本APIにて提供する情報の正確性・妥当性につきましては細心の注意を払っておりますが、当作者はその保証をするものではありません。本APIの利用によって利用者や第三者等にネットワーク障害等による損害、データの損失その他あらゆる不具合、不都合が生じた場合について、裁判所またはそれに準ずる機関で当作者の重過失が認められた場合を除き、当作者では一切の責任を負いません。

本APIは、東洋大学シラバスデータベースシステム(URL:[https://g-sys.toyo.ac.jp/syllabus/](https://g-sys.toyo.ac.jp/syllabus/))にて公開されているデータをスクレイピングしています。本APIを利用される際は、システムへの負荷の観点からアクセス頻度を常識的な範囲内に調整するようにして下さい。

# Author
* Terachan

# Contact
お問合わせは、[こちら](https://tera-chan.com/contact.html)からお願いいたします。

# License
本ソフトウェアは、[MITライセンス](./LICENSE)の下提供されています。



