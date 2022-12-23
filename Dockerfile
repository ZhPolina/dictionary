FROM python:3.8.10
COPY . /server
WORKDIR /server
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
RUN pip install -r requirements.txt
#CMD FLASK_APP=app.py flask run
CMD ["flask", "run"]