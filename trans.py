from googletrans import Translator
import json, sys

path = input("翻訳元のファイルを選択 >")
with open(path, "r", encoding="utf-8") as f:
    text = f.read()
print("---------------------------")
print("1: lvl1(英語経由)")
print("2: lvl2(2言語経由)")
print("3: lvl3(6言語経由)")
print("4: max(19言語経由)")
print("---------------------------")
kyodo = input("翻訳度を上の数字から選択: ")
if kyodo == "1":
    lvl = "lvl1"
elif kyodo == "2":
    lvl = "lvl1"
elif kyodo == "3":
    lvl = "lvl1"
elif kyodo == "4":
    lvl = "max"
elif kyodo == "5":
    lvl = "master"
with open("./transconf.json", "r", encoding="utf-8") as f:
    l = json.load(f)
    for i in range(len(l[lvl])):
        print(l[lvl][i] + "での翻訳中...")
        translator = Translator()
        trans_en = translator.translate(text, dest=l[lvl][i])
        text = trans_en.text
        print("完了")
    translator = Translator()
    trans_en = translator.translate(text, dest="ja")
with open(path + "_translated.txt", "w") as a:
    a.write(trans_en.text)
    print("保存完了")
    sys.exit()