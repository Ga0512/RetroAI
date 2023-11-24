FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN cd DeOldify

RUN pip install opencv-python==4.4.0.42
RUN pip install numpy==1.24.3

RUN pip install -r requirements.txt

EXPOSE 5000

RUN cd ..
CMD python ./DeOldify/app.py