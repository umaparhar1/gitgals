"""
WSGI config for Proj1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import yfinance as yf

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proj1.settings')

application = get_wsgi_application()

stock = input("Enter a stock name")

stockName = yf.Ticker(stock)

print(stockName.info)
