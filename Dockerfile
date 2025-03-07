FROM python:3.9.21

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r requirements.txt

COPY demo1.py .

CMD [ "python", "./demo1.py" ]
