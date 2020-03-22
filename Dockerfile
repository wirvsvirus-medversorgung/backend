FROM python:buster
WORKDIR /usr/src
RUN mkdir backend
COPY . /usr/src/backend
WORKDIR /usr/src/backend
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "-m", "flask", "run"]