# Build dock image:
#    docker build -t txt-reader:latest -f Dockerfile .
#
# In txt books directory, run dock container:
#    docker run -it --rm -p 5000:8000 -v "$PWD":/reader/books/ txt-reader:latest
# In browser, visit:
#    http://localhost:5000

FROM python:3.11-alpine

LABEL maintainer="Fan Hongtao <fanhongtao@163.com>"

COPY requirements.txt ./

RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY web /reader/web/
COPY books/*.txt /reader/books/

WORKDIR /reader/web
EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "run:app"]
