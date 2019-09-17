FROM python

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_APP main.py

ENTRYPOINT ["flask"]
CMD ["run", "-h", "0.0.0.0", "-p", "5555"]
