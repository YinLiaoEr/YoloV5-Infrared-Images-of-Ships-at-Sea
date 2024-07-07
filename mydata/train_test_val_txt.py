import os

xml_folder_paths = ["C:/Users/Zhaox/Desktop/yolov5-ship_detection/mydata/data/label/test",
                    "C:/Users/Zhaox/Desktop/yolov5-ship_detection/mydata/data/label/train",
                    "C:/Users/Zhaox/Desktop/yolov5-ship_detection/mydata/data/label/val"]

txt_folder_path = "C:/Users/Zhaox/Desktop/yolov5-ship_detection/mydata/data/dataSet/"

# 创建存放txt文件的文件夹
if not os.path.exists(txt_folder_path):
    os.makedirs(txt_folder_path)

for xml_folder_path in xml_folder_paths:
    # 获取当前xml文件夹中所有xml文件的文件名
    xml_files = os.listdir(xml_folder_path)

    # 创建对应的txt文件夹，文件夹名称与xml文件夹名称相同
    txt_subfolder_path = os.path.join(txt_folder_path, os.path.basename(xml_folder_path))
    os.makedirs(txt_subfolder_path, exist_ok=True)

    for xml_file in xml_files:
        with open(os.path.join(txt_subfolder_path, xml_file.replace('.xml', '.txt')), 'w') as txt_file:
            txt_file.write(xml_file)

print("转换完成")