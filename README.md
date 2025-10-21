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

**STEP2では以下を学びます：**

| テーマ | 内容 |
|--------|------|
| スコープ | 関数内外の変数の扱い方（LEGBルール） |
| リスト・タプル | 複数データの扱い |
| 辞書（dict） | キーと値のペア管理 |
| セット（set） | 重複なしのデータ集合 |
| ループ応用 | リスト内包表記など |
| 関数応用 | ラムダ式・関数の引数活用 |

---

🧭 **目標：**  
STEP2を終えるころには、  
「簡単なデータ処理」や「ミニアプリ構築」ができるようになる。

---

### 🖥️コード例
## 🖨️実行結果
## 📁フォルダ構成
