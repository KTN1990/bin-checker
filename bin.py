#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#KILL THE NET

from requests import get
from sys import argv
from prettytable import PrettyTable

def _check_(cc):
	T   = PrettyTable()
	r 	= get(f"https://lookup.binlist.net/{cc}",
		headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 
		"Accept-Version": "3"}).json()
	T.field_names = ['CARD NUM','CARD SCHEME', 'CARD TYPE', 'CARD BRAND', 'CARD PREPAID', 'CARD COUNTRY', 'CARD BANK']
	T.add_row([cc,r["scheme"], r["type"], r["brand"], r["prepaid"], f'{r["country"]["name"]}({r["country"]["emoji"]} )', f'{r["bank"]["name"]}({r["bank"]["url"]})'])
	print(T)

if __name__ == '__main__':
	while 1:
		try:
			if len(argv)==2:
				if len(argv[1]) >= 6: _check_(argv[1]); break
				else:
					cc = input("[•] PLEASE PUT THE FIRST 6 DIGITS OF YOUR CARD > ").replace(" ", "")
					if len(cc) >= 6: _check_(cc); break
			else:
				cc = input("[•] PLEASE PUT THE FIRST 6 DIGITS OF YOUR CARD > ").replace(" ", "")
				if len(cc) >= 6: _check_(cc)
		except KeyboardInterrupt: print("\nGOODBYE!"); exit()
		except EOFError: print("\nGOODBYE!"); exit()



