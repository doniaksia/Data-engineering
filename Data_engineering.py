from datetime import datetime

def obtenir_temps():
    print("Hello ! Il est {}.".format(datetime.now().strftime("%H:%M:%S")))
    
print(obtenir_temps())