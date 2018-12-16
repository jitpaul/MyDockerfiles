FROM python:3.6

ARG PROJECT=tictactoe

ARG PROJECT_DIR=/var/www/${PROJECT}

RUN mkdir -p $PROJECT_DIR

WORKDIR $PROJECT_DIR

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]