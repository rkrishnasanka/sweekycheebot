import time

def log(data):
    try:
        texttoprint = str(data)
    except:
        texttoprint = "Encoding error"
        
    file = open('log.txt', 'a+')
    file.write(time.asctime(time.localtime())+': '+texttoprint+'\n')
    file.close()
