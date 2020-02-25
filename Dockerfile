FROM python:3.6

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 6070

ENTRYPOINT ["python", "script.py"]