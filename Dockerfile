FROM tensorflow/tensorflow:2.1.0-py3 AS base

ARG HUB_MODEL_URL=https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1

ENV TFHUB_CACHE_DIR=/tfhub_cache \
    HUB_MODEL_URL=${HUB_MODEL_URL}

COPY requirements.txt /
RUN pip install -r requirements.txt

WORKDIR /app

# warming up; to download model parameters
COPY app/detector.py /app/
RUN (echo 'from detector import Detector'; echo 'Detector("'${HUB_MODEL_URL}'").prepare()') | python

COPY app /app

CMD ["uvicorn", "app:app", "--uds=/run/uvicorn/app.sock"]
