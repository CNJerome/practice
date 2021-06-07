import sys
# 替换文本
file1 =sys.argv[1]
# 原文本
file2 = sys.argv[2]


with open(file1,'r',encoding='utf-8') as f:
    file_content = f.readlines()
with open(file2,'r',encoding='utf-8') as f:
    file_content2 = f.readlines()

file_dict = dict()
for i in range(0, len(file_content) - 2, 3):
    # 原文本
    raw_text = file_content[i]
    # 标注文本
    label_text = file_content[i + 1]
    # 标签
    label_list = file_content[i + 2]
    id = raw_text.split('\t')[0]
    file_dict[id] = raw_text + '==' + label_text + '==' + label_list
print(file_dict)

file_dict2 = dict()
for i in range(0, len(file_content2) - 2, 3):
    # 原文本
    raw_text = file_content2[i]
    # 标注文本
    label_text = file_content2[i + 1]
    # 标签
    label_list = file_content2[i + 2]
    id = raw_text.split('\t')[0]
    file_dict2[id] = raw_text + '==' + label_text + '==' + label_list

for item in file_dict2:
    if item in file_dict:
        file_dict2[item] = file_dict[item]

with open('new_text.txt','w',encoding='utf-16') as f:
    for item in file_dict2:
        raw_text = file_dict2[item].split('==')[0]
        label_text = file_dict2[item].split('==')[1]
        label_list = file_dict2[item].split('==')[2]
        f.write(raw_text)
        f.write(label_text)
        f.write(label_list)