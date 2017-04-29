from poloniex import Poloniex, Coach
import datetime
import sendgrid
import os
import time
import pprint
from sendgrid.helpers.mail import *
import sys
sys.stdout.flush()

polo = Poloniex()
myCoach = Coach()

polo.Key = 'add_your_poloniex_api_key_here'
polo.Secret = 'add_your_poloniex_api_secret_here'

polo.public = Poloniex(coach=myCoach)
polo.private = Poloniex(polo.Key, polo.Secret, coach=myCoach)

var = 1
while var == 1 :

	balance = polo.private.returnBalances()
	balanceETH = balance['ETH']
	balanceBTC = balance['BTC']
	balanceUSDT = balance['USDT']
	#balances = polo.private.returnCompleteBalances()

	current_time = datetime.datetime.now(datetime.timezone.utc)
	unix_timestamp = current_time.timestamp() # works if Python >= 3.3
	unix_timestamp_minus_1_hour = unix_timestamp - (60 * 60)
	tradehistory = polo.private.returnTradeHistory("all", start=unix_timestamp_minus_1_hour)

	print(datetime.datetime.now())
	print("I have" , balanceETH ," ETH")
	print("I have" , balanceBTC ," BTC")
	print("I have" , balanceUSDT ," USDT")

	if len(tradehistory) >= 1:
	
		print("Trades / Send email")
		nicetradehistory = pprint.pformat(tradehistory)
		print (nicetradehistory)
		sg = sendgrid.SendGridAPIClient(apikey='add_your_sendgrid_api_key_here')
		from_email = Email("from_email_at_email.com")
		subject = "Poloniex Status / Order Update"
		to_email = Email("to_email_at_email.com")
		content = Content("text/plain", "BTC: " + balanceBTC + "\n\nETH: " + balanceETH + "\n\nUSDT " + balanceUSDT + "\n\n" + nicetradehistory)
		#content = Content("text/plain", "BTC: ")
		mail = Mail(from_email, subject, to_email, content)
		response = sg.client.mail.send.post(request_body=mail.get())
		print(response.status_code)
		print(response.body)
		print(response.headers)
	else:
		print("No Trades")

	print("sleeping")
	time.sleep(3600)

	
