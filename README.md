# 🐍Python Basics
Python学習用の基礎構文トレーニングプロジェクトです。各ステップごとに文法を学び、実行結果を記録していきます。

## STEP 1 概要：Python基礎構文（文法の筋トレ）
Pythonでプログラムを書けるようになるための「文法の型」を習得する。
→ このステップを終えると、**小さなアプリ（計算、条件分岐、入力・出力）**を自作できるようになります。

## 📘 学習進捗

- [x] STEP1-01 出力と入力
- [x] STEP1-02 変数とデータ型
- [x] STEP1-03 条件分岐（if文）
- [ ] STEP1-04 ループ（for / while）
- [ ] STEP1-05 関数

## 1️⃣ STEP1-01：出力と入力（print / input）
### 🖥️コード例
```python
name = input("あなたの名前を教えてください：")
print("こんにちは、”) + name + "さん！")

## 🖨️実行結果
あなたの名前を教えてください：katsuyuki konno
こんにちは、katsuyuki konnoさん

## 📁フォルダ構成
python-basics/
├── step1_basics/
│   ├── 01_print_input.py
│   ├── 
└── README.md

## 2️⃣ STEP1-02：変数とデータ型（Variables & Data Types）
### コード例
```python
name = input("あなたの名前は？：")
age = int(input("あなたの年齢は？："))
print("こんにちは、"　+ name + "さん。あなたは" + str(age) + "ですね。")
print("来年は", age + 1, "さいになります！")

## 実行結果
あなたの名前は？：seisei
あなたの年齢は？:44
こんにちはseiseiさん。来年は45ですね。

## 📁フォルダ構成
python_basics/
├── step1_basics/
│   ├── 01_print_input.py
│   ├── 02_variables.py
│   └── 
└── README.md

## 🧩 STEP1-03：条件分岐（if / elif / else）
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

## 🖨️実行結果
あなたの年齢を入力してくd歳。：1
子どもです。
数字を入力してください：4828
偶数です

## 📁フォルダ構成
python_basics/
├── step1_basics/
│   ├── 01_print_input.py
│   ├── 02_variables.py
│   └── 03_condition.py
└── README.md

### 🖥️コード例
## 🖨️実行結果
## 📁フォルダ構成