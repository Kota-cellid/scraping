import sys
from urllib.request import urlopen

f = urlopen('https://gihyo.jp/dp')
# HTTPヘッダーからエンコーディングを取得する
encoding = f.info().get_content_charset(failobj='utf-8')
print('encoding:', encoding, file=sys.stderr) #エンコーディングを標準エラーに出力する
text = f.read().decode(encoding) #得られたエンコーディングを指定して文字列にデコードする
print(text)
