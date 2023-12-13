from Extracter import Extracter

if __name__ == '__main__':
    url='https://www.zhihu.com/question/316039999'
    # 最多下载图片数量
    maxNum=5
    #文件保存路径
    savePath='图片'
    Extracter.extractImages(url,savePath,maxNum)