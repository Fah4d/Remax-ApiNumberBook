import requests
import time
import random
import re
import json


remax = """

██████╗░███████╗███╗░░░███╗░█████╗░██╗░░██╗  ░██████╗░██╗░░██╗
██╔══██╗██╔════╝████╗░████║██╔══██╗╚██╗██╔╝  ██╔════╝░██║░░██║
██████╔╝█████╗░░██╔████╔██║███████║░╚███╔╝░  ██║░░██╗░███████║
██╔══██╗██╔══╝░░██║╚██╔╝██║██╔══██║░██╔██╗░  ██║░░╚██╗██╔══██║
██║░░██║███████╗██║░╚═╝░██║██║░░██║██╔╝╚██╗  ╚██████╔╝██║░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚═╝

            Remax Alghmadi - insta : @ 0637871936 .
            
"""

print(remax)
time.sleep(3)

print("Only for Saudi numbers")
number = str(input("Number : "))
def whoisthecaller():
	url = "https://rdod.live/contacts_api/api.php?getName=true&phone="+str(number)
	req = requests.get(url).json()
	g = json.dumps(req, indent=4 , sort_keys=True)
	v = json.loads(g)
	text = str(req)
	print("The names have been saved in names.txt")
	with open("names.txt", "a", encoding='utf-8') as wr:
		wr.write(str(v["data"]))

whoisthecaller()

print('')
input("press enter to close the program.")