import os
import urllib.request
import zipfile

def download_and_extract(url, destination):
    filename = url.split('/')[-1]
    file_path = os.path.join(destination, filename)
    
    if not os.path.exists(file_path):
        print(f"正在下载 {filename}...")
        # 使用 urlretrieve 下载，并显示进度（可选）
        urllib.request.urlretrieve(url, file_path)
        print(f"下载完成: {filename}")
    else:
        print(f"{filename} 已存在，跳过下载。")

    print(f"正在解压 {filename}...")
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(destination)
    print(f"解压完成。")
    # 可选：解压后删除压缩包以节省空间
    # os.remove(file_path)

def main():
    # 设定存储目录
    dataset_dir = './coco2017'
    os.makedirs(dataset_dir, exist_ok=True)

    # COCO 2017 官方下载地址
    urls = {
        "train_images": "http://images.cocodataset.org/zips/train2017.zip",      # ~18GB
        "val_images": "http://images.cocodataset.org/zips/val2017.zip",          # ~1GB
        "test_images": "http://images.cocodataset.org/zips/test2017.zip",        # ~6GB
        "annotations": "http://images.cocodataset.org/annotations/annotations_trainval2017.zip" # ~241MB
    }

    for key, url in urls.items():
        try:
            download_and_extract(url, dataset_dir)
        except Exception as e:
            print(f"处理 {key} 时出错: {e}")

    print("\n所有任务已完成！数据集存放在:", os.path.abspath(dataset_dir))

if __name__ == "__main__":
    main()
