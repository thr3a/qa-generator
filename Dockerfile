FROM python:3.10

WORKDIR /tmp

ADD requirements.txt ./
ADD download.py ./
RUN pip install --no-cache-dir -r requirements.txt \
  && python -m spacy download ja_core_news_sm \
  && python ./download.py

WORKDIR /app

ADD server.py ./

CMD ["python", "server.py"]
