#coding: UTF-8
import sys

print(u"こんにちわ")

# 標準入力、標準出力、標準エラー出力
print(sys.stdin.encoding)
print(sys.stdout.encoding)
print(sys.stderr.encoding)

# 文字列の標準出力 カンマで区切った場合空白が挿入される
print("Hello!", "Python")

# トリプルクォーテーション
print("""<html>
<head>
<title>Test</title>
</head>
<body>
<p>Test Page</p>
</body>
</html>""")

# raw文字列
print(r"C:\My Document\node\track\test.txt")

# unicord文字列
print(u"こんにちわ\nお元気ですが？")
print(u"Bananaの値段は1000円です")

# 文字列の連結
print("Python" + u"本")

# 文字列の繰り返し
print("*" * 30)

# 文字列の長さ
print(len(u"あいうえお"))

# str([object])組み込み関数
print("Year", str(2000))
print("円周率", str(3.14159))

# 文字列Indexとスライス
str = "ABCDE"
print(str[1], str[2:4])
slice= str[1:-1]
print(slice) # "BCD"

slice = str[1:] # "BCDE"
slice = str[:2] # "AB"

print(u"対象文字列 " + str)

print("[1:3]  " + str[1:3])
print("[1:-1] " + str[1:-1])
print("[1:]   " + str[1:])
print("[:2]   " + str[:2])
print("[:]    " + str[:])



# 数値
1.414
-4.2
.75
2.5e5
3.1e-4
