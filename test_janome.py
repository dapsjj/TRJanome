from janome.tokenizer import Tokenizer
import csv

title = [['キーワード','原形','品詞','品詞細分類']]
top_list=[]
t = Tokenizer()
every_row= t.tokenize('私はメールを送った。')
for item in every_row:
    array1=str(item).split("\t")
    array2=array1[1].split(",")
    top_list.append([array1[0],array2[6],array2[0],array2[1]])
with open(r'D:/janome.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(title)
    writer.writerows(top_list)
