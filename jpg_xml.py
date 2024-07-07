import os
import xml.etree.ElementTree as ET
import glob
import shutil
import random

# 类别映射
classes = ["person", "vehicle", "NonMotorVehicle"]

# 数据路径
data_dir = 'data'
images_dir = os.path.join(data_dir, 'Images')
labels_dir = os.path.join(data_dir, 'Labels')

# 目标路径
train_images_dir = os.path.join(images_dir, 'train')
val_images_dir = os.path.join(images_dir, 'val')
train_labels_dir = os.path.join(labels_dir, 'train')
val_labels_dir = os.path.join(labels_dir, 'val')

# 创建目标目录
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# 获取所有XML文件
xml_files = glob.glob(os.path.join(labels_dir, '*.xml'))

# 分割数据集
random.seed(0)
random.shuffle(xml_files)
split_idx = int(len(xml_files) * 0.8)
train_files = xml_files[:split_idx]
val_files = xml_files[split_idx:]

def convert_annotation(xml_file, output_txt_path):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)

    with open(output_txt_path, 'w') as f:
        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes or int(difficult) == 1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text),
                 float(xmlbox.find('xmax').text), float(xmlbox.find('ymax').text))
            bb = (b[0] + b[2]) / 2.0 / width, (b[1] + b[3]) / 2.0 / height, (b[2] - b[0]) / width, (b[3] - b[1]) / height
            f.write(f"{cls_id} {' '.join([str(a) for a in bb])}\n")

# 处理训练集和验证集
for xml_file in train_files:
    img_file = os.path.join(images_dir, os.path.basename(xml_file).replace('.xml', '.jpg'))
    if not os.path.exists(img_file):
        continue
    output_txt_path = os.path.join(train_labels_dir, os.path.basename(xml_file).replace('.xml', '.txt'))
    convert_annotation(xml_file, output_txt_path)
    shutil.copy(img_file, train_images_dir)

for xml_file in val_files:
    img_file = os.path.join(images_dir, os.path.basename(xml_file).replace('.xml', '.jpg'))
    if not os.path.exists(img_file):
        continue
    output_txt_path = os.path.join(val_labels_dir, os.path.basename(xml_file).replace('.xml', '.txt'))
    convert_annotation(xml_file, output_txt_path)
    shutil.copy(img_file, val_images_dir)
