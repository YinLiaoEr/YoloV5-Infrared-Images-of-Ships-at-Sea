import os
from PIL import Image
import xml.etree.cElementTree as ET

# 设置图片文件夹路径
input_folder = "C:\\Users\\Zhaox\\Desktop\\yolov5-ship_detection\\mydata\\data\\images\\train"
output_folder = "C:\\Users\\Zhaox\\Desktop\\yolov5-ship_detection\\mydata\\data\\label\\train"

# 获取文件夹中所有图片文件的列表
image_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg')]

# 遍历每个图片文件
for image_file in image_files:
    # 读取jpg图片
    img = Image.open(os.path.join(input_folder, image_file))

    # 创建xml文件
    annotation = ET.Element("annotation")

    # 添加图片信息
    filename = ET.SubElement(annotation, "filename")
    filename.text = image_file

    size = ET.SubElement(annotation, "size")
    width = ET.SubElement(size, "width")
    width.text = str(img.width)
    height = ET.SubElement(size, "height")
    height.text = str(img.height)

    # 保存xml文件
    tree = ET.ElementTree(annotation)
    output_xml = os.path.join(output_folder, os.path.splitext(image_file)[0] + ".xml")
    tree.write(output_xml)

# 完成所有图片的转换
print("转换完成")