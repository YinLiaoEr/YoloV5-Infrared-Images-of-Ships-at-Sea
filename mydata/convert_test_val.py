import os
import random
import shutil

# 设置文件夹路径
test_folder = "C:/Users/Zhaox/Desktop/yolov5-ship_detection/mydata/data/images/test"
val_folder = "C:/Users/Zhaox/Desktop/yolov5-ship_detection/mydata/data/images/val"

# 获取文件夹中所有图片文件的列表
image_files = [f for f in os.listdir(test_folder) if f.endswith('.jpg')]

# 随机打乱图片文件列表
random.shuffle(image_files)

# 计算一半图片数量
split_count = len(image_files) // 2

# 清空val文件夹
for file in os.listdir(val_folder):
    file_path = os.path.join(val_folder, file)
    if os.path.isfile(file_path):
        os.remove(file_path)

# 遍历随机选择的一半图片文件并拷贝到val文件夹中
for i in range(split_count):
    image_file = image_files[i]
    src_path = os.path.join(test_folder, image_file)
    dst_path = os.path.join(val_folder, image_file)
    shutil.copyfile(src_path, dst_path)

# 删除原test文件夹中的图片
for i in range(split_count):
    image_file = image_files[i]
    src_path = os.path.join(test_folder, image_file)
    os.remove(src_path)

print("随机拆分完成")