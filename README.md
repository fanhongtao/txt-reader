# 项目目的

网络上找到的一些 txt 格式的小说，通常我是使用 [Calibre](https://calibre-ebook.com/) 转换成电子书，然后导入到 kindle 再阅读。

但有时候，kindle不在身边，希望能使用 Web 方式阅读，如，在手机上阅读。所以就有了本项目。

本项目实现：

1. 提供一个固定目录（books/）用于存放小说
2. 只支持 UTF-8 格式的 txt 文件
3. 支持按章节阅读（由程序自动实现章节的识别）

# 运行程序

安装依赖库：

* `pip3 install pypinyin`

运行 [Flask](Flask.md)

# docker

为了减少对环境的依赖，提供了 Docker 中的运行方式。

1. 执行命令创建docker镜像：<br/>
   `docker build -t txt-reader:latest -f Dockerfile .`
2. 在存放电子书的目录下，执行以下命令运行 docker 镜像：<br/>
   `docker run -it --rm -p 5000:5000 -v "$PWD":/reader/books/ txt-reader:latest`<br/>
   如果需要反复运行，可以执行如下命令：<br/>
   `docker run -d --name txt-reader -p 5000:5000 -v "$PWD":/reader/books/ txt-reader:latest`
