FROM python:latest

COPY requirements.txt /Citadel/requirements.txt
WORKDIR /Citadel
RUN pip install -r requirements.txt
COPY . /Citadel

ADD ./ Citadel/

ENV PYTHONPATH /Citadel

CMD [ "python", "swd_body.py"]