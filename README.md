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



