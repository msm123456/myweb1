FROM python:3.8
ENV PYTHONUNBUFFERD 1
RUN mkdir /code
WORKDIR /code
Add requirements.txt /code/
RUN pip install -r requirements.txt
Add . /code/
ENTRYPOINT ["sh","/code/commands.sh"]