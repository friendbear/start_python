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

# 演算
17 /5 # 3
-17 / 5 # -4
17 // 5 # 3
17.0 // 5 # 3.0
5 %3 # 2
5 ** 2 # 25

# 型変換
int("14") # 14
int("3F", 16) # 63
int(16.8) # 16
int(-7.2) # -7

# 変数名の命名ルール
# 1) 1文字目は英文字かアンダーバー(_)
# 2) 2文字目以降は英数文字、アンダーバー
# 3) 予約語は使用できない
# 4) 大文字と小文字は区別される


# list
list1 = [1, 2]
list2 = list1
list1.append(3)
print(list2)


variable()
def variable():
	num = 10
	name = u"加藤"
	msg = "Hello"
	print(msg)
	

if 10 % 3:
	print(u"割り切れません")

x = 0
y = 1
if x == 0:
	print("x is zero")
	if y == 0:
		print("y is zero")

# 真偽値
# 数値型の場合は0(0、0.0、0jなど)は偽(false)、0以外は真(true)
# 文字列型の場合は空文字列("")は偽(false)、""以外は真(true)
# 空のタプル()、空のリスト[]、空のディクショナリ{}は偽(false)
# BooleanType型の「True」は真(true)
# BooleanType型の「False」は偽(false)
# NoneType型の「None」は偽(false)
if True:
	print("Always True")

num = 20
if num < 20:
	print("num is lt 20")
pref = "Tokyo"

if pref > "Osaka":
	print("pref is over Tokyo")
