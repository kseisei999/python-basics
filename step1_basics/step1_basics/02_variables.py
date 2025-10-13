STEP 2：変数とデータ型（Variables & Data Types）

# ①変数（Variable）とは？ ＝ 値を入れておく箱
name = "チャッピー"
age = 50


# ❷主なデータ型（Data Types）
# 数値（整数）：int、数値（小数）：float、文字列：str、真偽地：bool、リスト：list、辞書：dict


# ③type() で方を確認
x = 10
y = 3.14
z = "こんにちは"
print(type(x))
print(type(y))
print(type(z))


# ④文字列と数値の違い
a = "10"   # 文字列
b = 10     # 数値
print(a + a)  # "1010"
print(b + b)  # 20
# 🔺文字列（"10"）と数値（10）は別もの！


# ⑤型変換（Casting）
age = input("年齢を入力してください：")
age = int(age)
print("来年は", age + 1, "歳ですね。")


# ⑥Eランク練習問題
# 1️⃣ ユーザーから名前と年齢を入力し、
# 「こんにちは◯◯さん。あなたは◯歳ですね。」と出力する。
# 2️⃣ ユーザーの年齢を1年足して、「来年は◯歳ですね。」と出力する。
# 3️⃣ type() を使って、それぞれのデータ型を表示する。
name = input("あなたの名前は？：")
age = int(input("あなたの年齢は？:"))
print(f"こんにちは{name}さん。来年は{age + 1}ですね。")
print(type(name), type(age))