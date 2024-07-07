# coding:utf-8

import os

# 获取当前工作目录
current_dir = os.getcwd()
print(current_dir)
# 定义相对路径，相对于当前工作目录
# 例如，如果xml和jpg文件夹在当前工作目录的同级目录下
# 你可以使用'..'来表示上一级目录，或者直接使用文件夹名称
relative_xml_path = os.path.join(current_dir, 'data/xml/val')  # 替换为实际的相对路径
relative_jpg_path = os.path.join(current_dir, 'data/images/val')  # 替换为实际的相对路径
relative_txt_path = os.path.join(current_dir, 'data/dataSet')  # 替换为实际的相对路径
# 确保txt_path文件夹存在
if not os.path.exists(relative_txt_path):
    os.makedirs(relative_txt_path)

# 获取XML目录下的所有文件
total_xml = [f for f in os.listdir(relative_xml_path) if f.endswith('.xml')]

# 定义输出文本文件的路径
output_txt_path = os.path.join(relative_txt_path, 'val.txt')

# 打开文件准备写入
with open(output_txt_path, 'w') as output_file:
    # 遍历XML文件
    for xml_file in total_xml:
        # 去除.xml后缀，获取基础文件名
        base_name = os.path.splitext(xml_file)[0]
        # 构建JPG文件的完整路径
        jpg_file = os.path.join(relative_jpg_path, base_name + '.jpg')

        # 检查JPG文件是否存在
        if os.path.isfile(jpg_file):
            # 如果存在，写入到文本文件
            output_file.write(jpg_file + '\n')
