import os
import time
def run():
    try:
        os.system('python Linkedin.py')
        time.sleep(200)
    except:
        pass
i = 1 
while (i<100):
    run()
    i = i + 1
