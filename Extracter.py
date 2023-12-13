import re
import requests
import requests
import os
import time

class Extracter:
    header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        }
    @staticmethod
    def getImagesURL(url):
        response = requests.get(url, headers=Extracter.header)
        if response.status_code == 200:
            htmlContent = response.text
            # 匹配以<img src开头的URL
            img_urls = re.findall(r'<img src="(https://picx\.zhimg\.com/[^"]+)"', htmlContent)
            return img_urls
    @staticmethod
    def downloadImage(imageURLs, savePath, imageName):
        # 确保保存路径存在，如果不存在则创建
        if not os.path.exists(savePath):
            os.makedirs(savePath)
        response = requests.get(imageURLs, stream=True)
        if response.status_code == 200:
            with open(os.path.join(savePath, imageName), 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
    @staticmethod
    def extractImages(url,savePath,maxNum=20):
        imageURLs = Extracter.getImagesURL(url)
        for i, url in enumerate(imageURLs):
            imageName = f'image_{i}.jpg'  
            Extracter.downloadImage(url, savePath, imageName)
            print(f"成功下载{i+1}张图片")
            time.sleep(0.5)  # 在下载下一张图片前暂停0.5秒
            if i+1 >= maxNum:
                break
        