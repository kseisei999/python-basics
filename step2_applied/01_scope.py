# STEP2-①：スコープ（Scope）とは？：
"""
変数や関数などが、どこで使えるか（参照できるか）」を決める有効範囲のこと
スコープは「LEGBルール」で管理される
```
LEGBルールとは
| 順番 | スコープ名 | 意味 | 例 |
|------|----------|-----|----|
| L | Local | 関数の中で定義された変数 | 関数内のローカル変数 |
| E | Enclosing | ネスト(入れ子)された関数の外部のスコープ | 関数の中に関数があるとき |
| G | Global | モジュール全体(関数の外)で定義された変数 | ファイルの先頭で定義された変数 |
| B | Built-in | Pythonに最初から用意されている変数 | len, print, sum など |
```
 Pythonは、変数を探す時にこの順番で探す。
 Local → Enclosing → Global → Built-in
 """
# 例１：基本的なスコープ
x = 10 # グローバル関数
def show_value():
    x = 5 # ローカル変数
    print("関数内:", x)
          
show_value()
print("関数外：", x)
# 関数の内と外だと、同じ変数名でも別々のスコープで認識する

# 例2：globalキーワード（関数内でグローバル変数を書き換える）
x = 10
def update_value():
    global x # グローバル変数を使う宣言
    x = 20

update_value()
print(x)
# globalを使うと、関数内で外の変数を置き換え可能（乱用は危険）

# 🔧例3：Enclosing（ネストされた関数）
def outer():
    x = "外側"
    def inner():
        print("内側から参照：", x)
    inner()

outer()

# 例4：nonlocalキーワード（外側のスコープ変数を書き換える）
def outer():
    x = "外側"
    def inner():
        nonlocal x
        x = "内側で変更" 
    inner()
    print(x)

outer()

# 👉 nonlocal を使うと、一つ外側の関数スコープの変数を書き換え可能です。(使い所に注意)

# 練習問題
# 01
x = 1
def func():
    x = 2
    print("関数内：", x)

func()
print("関数外：", x)

# 02
x = 1
def func():
    global x
    x = 2
    print("関数内:", x)

func()
print("関数外：", x)

# 03
def outer():
    x = "Hello"
    def inner():
        x = "world"
        print("outer", x)
    inner()
    print("outer:", x)

outer()

# STEP2-①-2：nonlocalキーワードとは？
"""
定義：
nonlocal は・・・
「関数の外（1つ外側の関数スコープ）にある変数」を書き換えたいときに使うキーワード。
"""
# nonlocal無しの場合
def outer():
    x = "外観"
    def inner():
        x = "内側"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
# 出力　← inner()内の x は新しいローカル変数なので、外側（outer）の x は変化しません。　

# 例2：nonlocalありの場合
def outer():
    x = "外観"
    def inner():
        nonlocal x
        x = "内側で変更"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
# 出力 ← onlocal によって、「1つ外のスコープにある変数x」を直接変更。

# ⚠️globalとの違い
"""
[比較項目]
＜作用範囲＞
nonlocal : 1つ外側の関数スコープ
global : モジュール全体（ファイル全体）

＜よく使う場面＞
nonlocal : 関数が入れ子になっていて、外の関数の値を変更したい時
global : 関数内でグローバル変数を更新したい時

＜例＞
nonlocal : クロージャ（関数を返す関数）など
global : 定数や設定値を共有する処理など
"""

# 例３：クロージャとnonlocal (関数を”返す”関数でもnonlocalはよく使われる。)
def counter():
    count = 0
    def add_one():
        nonlocal count
        count += 1
        return count
    return add_one
c = counter()
print(c()) # 1
print(c()) # 2
print(c()) # 3
"""
👉 countはcounter()の外側スコープにある変数。
nonlocalを使うことで、「関数が呼ばれるたびに前回の値を覚えておける」んです。
これが**クロージャ（closure）**の代表的な使い方。
"""
# 💡まとめ：スコープキーワード早見表
"""
| キーワード | 意味範囲 | 書き換え可能 | よく使う場面 |
|----------|---------|------------|------------|
| (なし) | ローカル変数 | 関数内 | ✅ | 一時的な処理 |
| nonlocal | 一つ外側の関数スコープ | 関数の外 | ✅ | クロージャ・状態保持 |
| global | モジュール全体 | ファイル全体 | ✅ | 設定値の共有・グローバルカウンタ |
"""

# ミニ演習（Try）
# 次のコードの出力を予測して
def outer():
    msg = "Hello"
    def inner():
        nonlocal msg
        msg = "Hi"
        print("inner:", msg)
    inner()
    print("outer:", msg)
outer()

# 補足：nonlocalを使う実用例（関数の実行回数を数えたい場合）
def call_counter():
    count = 0
    def call():
        nonlocal count
        count += 1
        print(f"{count}回目の呼び出し")
    return call

counter = call_counter()
counter()
counter()
counter()

def make_attack_counter(limit=3):
    count = 0
    def attack():
        nonlocal count
        if count < limit:
            count += 1
            print(f"攻撃！({count}/{limit})")
        else:
            print("もう攻撃できません！")
    return attack

# 実行例
attack = make_attack_counter(8)
attack()
attack()
attack()
attack()



