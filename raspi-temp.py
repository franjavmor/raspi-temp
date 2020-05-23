import os

def raspi_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("'C","")
    temp = temp.replace("temp=","")
    temp = float(temp)
    return temp

print("%.2f" % raspi_temp())
