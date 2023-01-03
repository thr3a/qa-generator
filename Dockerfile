FROM thr3a/jupyterlab

RUN pip install ginza pytextrank lmqg psutil
RUN python -m spacy download ja_core_news_sm
ADD download.py /download.py
RUN python /download.py
