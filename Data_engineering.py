from datetime import datetime
##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
def obtenir_temps():
    print("Hello ! Il est {}.".format(datetime.now().strftime("%H:%M:%S")))

print(obtenir_temps())