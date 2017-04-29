# polo-notify
Python3 Script to check Poloniex for trades and send an email via Sendgrid

# Download the repo with:

git clone https://github.com/mkuendig/polo-notify

# Insert in to the script:

Poloniex API and Secret  
Sendgrid API  
Email address for from and to  

# Python

Use the script directly with `python3 polo-notify.py`

# Docker

1. `docker build -t polo-notify .`
2. `docker run -it polo-notify`
