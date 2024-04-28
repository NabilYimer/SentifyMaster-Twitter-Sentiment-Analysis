FROM python:3.11 

WORKDIR usr/app/src

COPY . .

RUN pip install -r requirements.txt 


CMD ["python","app/app.py"]






