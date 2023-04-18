FROM python:3.9

COPY . /src

# COPY ./requirements.txt /src/requirements.txt

WORKDIR src

EXPOSE 8000:8000

RUN pip3 install -r requirements.txt

CMD [ "python", "app.py" ]

# docker build -t mlapp . 
# docker run -p 8000:8000 -t -i mlapp