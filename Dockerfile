# Build dock image:
#    docker build -t txt-reader:latest -f Dockerfile .
#
# In txt books directory, run dock container:
#    docker run -it --rm -p 5000:5000 -v "$PWD":/reader/books/ txt-reader:latest

FROM python:3.9-alpine

LABEL maintainer="Fan Hongtao <fanhongtao@gmail.com>"

COPY requirements.txt ./

RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY web /reader/web/
COPY books/*.txt /reader/books/

WORKDIR /reader/web
EXPOSE 5000

CMD ["gunicorn", "run:app"]
