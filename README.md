# 🐍Python Basics
Python学習用の基礎構文トレーニングプロジェクトです。各ステップごとに文法を学び、実行結果を記録していきます。

## STEP 1 概要：Python基礎構文（文法の筋トレ）
Pythonでプログラムを書けるようになるための「文法の型」を習得する。
→ このステップを終えると、**小さなアプリ（計算、条件分岐、入力・出力）**を自作できるようになります。

## 📘 学習進捗

- [x] STEP1-01 出力と入力
- [x] STEP1-02 変数とデータ型
- [x] STEP1-03 条件分岐（if文）
- [x] STEP1-04 ループ（for / while）
- [x] STEP1-05 関数

## 1️⃣ STEP1-01：出力と入力（print / input）
- 入力：input()
- 出力：print()

### 🖥️コード例
```
python
name = input("あなたの名前を教えてください：")
print("こんにちは、”) + name + "さん！")

## 🖨️実行結果
あなたの名前を教えてください：katsuyuki konno
こんにちは、katsuyuki konnoさん
```

## 📁フォルダ構成
```
python-basics/
├── step1_basics/
│   ├── 01_print_input.py
│   ├── 
└── README.md
```

## 2️⃣ STEP1-02：変数とデータ型（Variables & Data Types）
- 変数：値を入れておく入れ物・箱
- 数値（整数）：int、数値（小数）：float、文字列：str、真偽地：bool、リスト：list、辞書：dict

### コード例
```
python
name = input("あなたの名前は？：")
age = int(input("あなたの年齢は？："))
print("こんにちは、"　+ name + "さん。あなたは" + str(age) + "ですね。")
print("来年は", age + 1, "さいになります！")
```

## 実行結果
あなたの名前は？：seisei
あなたの年齢は？:44
こんにちはseiseiさん。来年は45ですね。

## 📁フォルダ構成
```
python_basics/
├── step1_basics/
│   ├── 01_print_input.py
│   ├── 02_variables.py
│   └── 
└── README.md
```

## 4️⃣ STEP1-03：条件分岐（if / elif / else）
- 条件分岐とは？= 『判断力』を与える仕組み。Trueの時に特定の処理を実行する

### 🖥️コード例：年齢による判定
```python
age = int(input("あなたの年齢は？:"))
if age >= 20:
    print("成人です。")
elif age >= 13:
    print("ティーンエイジャーです。")
else :
    print("子どもです。")

コード例②：偶数・奇数の判定
num = int(input("数字を入力してください："))
if num % 2 == 0:
    print("偶数です")
else :
    print("奇数です")
```

## 🖨️実行結果
あなたの年齢を入力してくd歳。：1
子どもです。
数字を入力してください：4828
偶数です

## 📁フォルダ構成
```
python_basics/
├── step1_basics/
│   ├── 01_print_input.py
│   ├── 02_variables.py
│   └── 03_condition.py
└── README.md
```

## 4️⃣STEP1-04：ループ（for / while）
- ループとは？:同じ処理を【繰り返す】ための構文.
- for文：回数で繰り返す
- whoile文：条件がTrueの間、繰り返す

### 🖥️コード例（for文：回数で繰り返す）
```python 
for i in range(5):
    print(i)
```
## 🖨️実行結果
0
1
2
3
4
解説：
・range(5)はは『0から4まで』の数字を順に生成
・i二は毎回その値が代入されてprint()される

### 🖥️コード例（whoile文：条件がTrueの間、繰り返す）
```python 
count = 0 
while count < 3:
    print("こんにちは!")
    count += 1
```
## 🖨️実行結果
こんにちは！
こんにちは！
こんにちは！
解説：
・count += 1 は「count = count + 1」と同じこと
・条件がFalseになる(ccount < 3が成り立たなくなる)までループを続ける

## 📁フォルダ構成
```
python_basics/
├── step1_basics/
│   ├── 01_print_input.py
│   ├── 02_variables.py
│   ├── 03_condition.py
│   └── 04_loops.py
└── README.md
```

## 5️⃣ STEP1-05：関数（Functions）
- 関数とは？：何度も使う処理を“ひとまとめ”にして再利用できるようにする仕組み。
^ 関数を使うと、同じ処理をいちいち書かずに呼び出すだけで使えるようになります。

### 🖥️コード例:あいさつ関数
```python
def greet(name):
    print("こんにちは、 * name *  "さん！")

greet("チャッピー")
greet("Katsuki")
```
### 🖥️コード例 returnで値を返す
```python
def add(a, b):
    return a + b

result = add((5, 3)
print(f"結果：　{result}")
```

## 🖨️実行結果
こんにちは、チャッピーさん！
こんにちは、Katsukiさん！
結果：8

## 📁フォルダ構成
```
python_basics/
├── step1_basics/
│   ├── 01_print_input.py
│   ├── 02_variables.py
│   ├── 03_condition.py
│   ├── 04_loops.py
│   └── 05_functions.py
└── README.md
```

---

# 📘 STEP1：Python基礎構文まとめ

## 🎯 学習目的
Pythonの「文法の筋トレ」を通して、  
・変数  
・条件分岐  
・繰り返し処理  
・関数  
といった**プログラムの基礎思考**を身につける。

---

## 🧩 STEP1一覧

| ステップ | 学習テーマ | 学習内容 |
|-----------|------------|-----------|
| STEP1-01 | 出力と入力（print / input） | ユーザーから入力を受け取り、出力する |
| STEP1-02 | 変数とデータ型（Variables & Data Types） | 数値・文字列・型変換を理解 |
| STEP1-03 | 条件分岐（if / elif / else） | 条件による分岐処理を学ぶ |
| STEP1-04 | ループ（for / while） | 繰り返し処理の基本構文を習得 |
| STEP1-05 | 関数（Functions） | 処理をまとめて再利用する方法を理解 |

---

## 🧠 学習成果

- Pythonの基本構文を一通り理解  
- コードを「読む → 書く → 動かす → 解釈する」流れを体得  
- GitHubを使ったプロジェクト構成・Push運用も習得  
- 変数のスコープや関数の構造を理解する準備が整った  

---

## 🗂️ フォルダ構成
```
python_basics/
├── step1_basics/
│   ├── 01_print_input.py
│   ├── 02_variables.py
│   ├── 03_condition.py
│   ├── 04_loops.py
│   └── 05_functions.py
└── README.md
```

---

## 🏁 次のステップ：STEP2 応用構文（スコープ・データ構造）

**STEP2では以下を学ぶ：**
```
| テーマ | 内容 |
|--------|------|
| スコープ | 関数内外の変数の扱い方（LEGBルール） |
| リスト・タプル | 複数データの扱い |
| 辞書（dict） | キーと値のペア管理 |
| セット（set） | 重複なしのデータ集合 |
| ループ応用 | リスト内包表記など |
| 関数応用 | ラムダ式・関数の引数活用 |
```

---
🧭 **目標：**  
STEP2を終えるころには、  
「簡単なデータ処理」や「ミニアプリ構築」ができるようになる。
---
---
# STEP2：応用構文（スコープ・データ構造など）
-このステップでは、Pythonを使って「考えながらかける」状態を目指します。
### 学習目標
| No | テーマ | 習得の目安 | ゴール | 
|----|-------|----------|-------|
| 1 | スコープ（変数の有効範囲） | ★★ | 変数がどこで使えるかを理解し、バグを防げる |
| 2 | リスト操作 | ★★★ | append, extend, sliceなどを自在に扱える |
| 3 | タプル・セット・辞書 | ★★★ | データ構造ごとの特徴を理解し使い分けできる |
| 4 | 内包表記（リスト/辞書/集合） | ★★★ | for + if を1行で書ける |
| 5 | 関数の引数と戻り値 | ★★★ | デフォルト引数・可変長引数・キーワード引数を理解する |
| 6 | Lambda式・高階関数（map/filter/sorted） | ★★★ | シンプルな処理を関数化して使い回せる |
| 7 | 例外処理（try/except/finally） | ★★ | エラーに強いコードが書ける | 
| 8 | ファイル操作（open/read/write） | ★★ | テキスト・CSVファイルを安全に読み書きできる |
---
---
## STEP2の全体像

STEP2：応用構文
```
├── スコープ（LEGBルール）
│    ├─ Local / Enclosing / Global / Built-in
│    └─ global, nonlocalキーワード
├── データ構造
│    ├─ リスト（順序あり・変更可）
│    ├─ タプル（順序あり・変更不可）
│    ├─ セット（順序なし・重複なし）
│    └─ 辞書（キーと値のペア）
├── 内包表記
│    ├─ [式 for 変数 in iterable if 条件]
│    └─ {キー: 値 for 変数 in iterable}
├── 関数設計
│    ├─ def / return
│    ├─ デフォルト引数
│    ├─ *args / **kwargs
│    └─ ラムダ式
├── 高階関数
│    ├─ map(), filter(), sorted()
│    └─ key引数とlambdaの組み合わせ
├── 例外処理
│    ├─ try-except-finally
│    ├─ raise
│    └─ 独自例外クラス
└── ファイル操作
     ├─ with open() as f
     ├─ read, readline, readlines
     ├─ write, writelines
     └─ CSV操作（csvモジュール）
```
---
## 📘 学習進捗

- [x] STEP2-01 データ構造（リスト・タプル・セット・辞書）
- [ ] STEP2-02 変数とデータ型
- [ ] STEP2-03 条件分岐（if文）
- [ ] STEP2-04 ループ（for / while）
- [ ] STEP2-05 関数
---
## STEP2-01：スコープ（変数の有効範囲）
-スコープとは？：「変数や関数などが、どこで使える（参照できる）か」を決める有効範囲のこと。

### 🖥️コード例1：基本的なスコープ
```python
x = 10  # グローバル変数

def show_value():
    x = 5  # ローカル変数
    print("関数内:", x)

show_value()
print("関数外:", x)
```
## 🖨️実行結果
-関数内: 5
-関数外: 10
-関数の中と外で同じ名前の変数xを使っても、別々のスコープで管理されます

### 🖥️コード例2：globalキーワード（関数内でグローバル変数を書き換える）
```python
x = 10

def update_value():
    global x  # グローバル変数を使う宣言
    x = 20

update_value()
print(x)
```

## 🖨️実行結果
20
- global を使うと、関数内でも外の変数を書き換え可能になります。
  ※乱用は危険。バグの温床になりかねない。

### 🖥️コード例3：Enclosing（ネストされた関数）
```python
def outer():
    x = "外側"

    def inner():
        print("内側から参照:", x)

    inner()

outer()
```
## 🖨️実行結果
内側から参照: 外側
-内側の関数でも、外側の関数スコープの変数を参照できます。(Enclosingスコープ)

### 🖥️コード例4：nonlocalキーワード（外側のスコープ変数を書き換える）
```python
def outer():
    x = "外側"

    def inner():
        nonlocal x
        x = "内側で変更"

    inner()
    print(x)

outer()
```
## 🖨️実行結果
内側で変更
-一つ外側の関数スコープの変数を書き換え可能です。(nonlocalスコープ)
　※globalと同様、使い所は慎重に

## まとめ：スコープの使い分け
---
| 種類 | 範囲 | 書き換え可 |よく使う場面 |
|-----|-----|-----------|-----------|
| Local | 関数の中 | ✅ | 関数内で値を保持 |
| Enclosing | 関数の外（ネスト構造） | ✅（nonlocal）| 関数ネスト時のクロージャ処理 |
| Global | モジュール全体 | ✅（global） | 定数・設定値など |
| Built-in | Python内部 | ❌ | 組み込み関数（変更不可）|
---

## STEP2-01-2：nonlocalキーワードとは？
-「関数の外（1つ外側の関数スコープ）にある変数」を書き換えたいときに使うキーワード
---

## 🖥️コード例1：nonlocalなしの場合
```python
def outer():
    x = "外側"
    def inner():
        x = "内側"
        print("inner:", x)
    inner()
    print("outer:", x)

outer()
```
## 🖨️実行結果
-inner: 内側
-outer: 外側
-👉 inner()内の x は新しいローカル変数なので、外側（outer）の x は変化しない。

## 🖥️コード例2：nonlocalありの場合
```python
def outer():
    x = "外側"
    def inner():
        nonlocal x   # 外側のxを使う宣言
        x = "内側で変更"
        print("inner:", x)
    inner()
    print("outer:", x)

outer()
```
S
## 🖨️実行結果
-inner: 内側で変更
-outer: 内側で変更
-👉 nonlocal によって、「1つ外のスコープにある変数x」を直接変更している。
　　グローバル変数ではないけれど、関数をまたいで値を共有できる仕組みです。

## nonlocalとglobalの違い
---
| 比較対象 | nonlocal | global |
|---------|----------|--------|
| 作用範囲 | １つ外側の関数スコープ | モジュール全体（ファイル全体）|
| よく使う場面 | 関数が入れ子になっていて、外の関数の値を変更したい時 | 関数内でグローバル関数を更新したい時 |
| 例 | クロージャ（関数を返す関数）など | 定数や設定値を共有する処理など |
---

## 🖥️コード例3：クロージャとnonlocal
```python
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
```
## 🖨️実行結果
-１
-２
-３
-👉 countはcounter()の外側スコープにある変数。
-nonlocalを使うことで、「関数が呼ばれるたびに前回の値を覚えておける」んです。
-これが**クロージャ（closure）**の代表的な使い方。

# 💡まとめ：スコープキーワード早見表
---
| キーワード | 意味範囲 | 書き換え可能 | よく使う場面 |
|----------|---------|------------|------------|
| (なし) | ローカル変数 | 関数内 | ✅ | 一時的な処理 |
| nonlocal | 一つ外側の関数スコープ | 関数の外 | ✅ | クロージャ・状態保持 |
| global | モジュール全体 | ファイル全体 | ✅ | 設定値の共有・グローバルカウンタ |
---

## 🖥️コード例：関数の実行関数を数えたい婆愛
```python
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
```
## 🖨️実行結果
-1回目の呼び出し
-2回目の呼び出し
-3回目の呼び出し
-👉 関数が呼ばれるたびに、countが保持されて更新される。
-これが クロージャ（Closure）

## 🖥️コード例
## 🖨️実行結果
## 📁フォルダ構成

## 🖥️コード例
## 🖨️実行結果
## 📁フォルダ構成

