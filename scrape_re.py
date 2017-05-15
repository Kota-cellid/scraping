import re
from html import unescape

#中身を変数htmlに格納する
with open('dp.html') as f :
    html = f.read()


# re.html()を使って、書籍1冊に相当する部分のHTMLを取得する
for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):
    # 書籍のURLはitemprop="url"という属性をもつa要素のhre属性から取得する
    url = re.search(r'<a itemprop="url" href="(.*?)"', partial_html).group(1)
    url = 'https://gihyo.jp' + url #/で始まっているのでドメイン名などを追加する

    title = re.search(r'<p itemprop="name".*?</p>',partial_html).group(0)
    title = title.replace('<br/>', '') #<br/>タグをスペースに置き換える
    title = re.sub(r'<.*?>', '',title) #タグを取り除く
    title = unescape(title)

    print(url, title)

