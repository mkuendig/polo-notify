FROM python:3
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY polo-notify/requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
# RUN sed "s|1000)|100000)|g" -i "/usr/local/lib/python3.6/site-packages/poloniex/__init__.py"
COPY polo-notify/polo-notify.py /usr/src/app/
CMD [ "python3", "-u" , "./polo-notify.py" ]