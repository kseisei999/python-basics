# STEP1-05：関数（Functions）
"""
STEP1-05：関数（Functions）
"""
"""
①変数とは？
何度も使う処理を"人まとまり"にして再利用できるようにする仕組み。
"""
"""
②基本構文
def 関数名名(引数):
    実行する処理
    return 戻り値
"""
# #xample:
def greet(name):
    print("こんにちは、" + name + "さん！")

greet("チャッピー")
greet("Katsuyuki")

# 🖨️実行結果

# ③returnで値を返す
def add(a, b):
    return a + b

result = add(5, 3)
print(f"結果：{result}")

# 🖨️実行結果

# ④応用練習（Eランク）
"""
1️⃣ユーザの名前を入力して、関数greet(name)を呼び出し、「こんにちは、〇〇さん！」という出力するプログラムを作ってください。

2️⃣関数calc_square(sum)を定義して、入力された数字の２条を返すようにしてくだい。
→結果をprint()で表示。
"""
