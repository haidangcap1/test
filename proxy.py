import requests
import json
import  os
i = 1
import time
def name():
    try:
        response = requests.get("http://proxy.tinsoftsv.com/api/changeProxy.php?key=[TL82coSsakpkV2q0YG4PyjR0eu9szTlHpndmBd]")

        a = response.json()

        PROXY = a['proxy']
        
        wf = open("proxy.txt", 'w')

        wf.write(PROXY)

        wf.close()
        time.sleep(1000)
    

        os.remove("proxy.txt")

    except:
         time.sleep(20)
         os.remove("proxy.txt")
while (i <= 1000):

    
    name()
    i = i +1         

