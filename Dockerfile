FROM python:3
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY polo-notify.py /usr/src/app/
CMD [ "python3", "-u" , "./polo-notify.py" ]
