import os

def measure_temp():
  temp = os.popen("vcgencmd measure_temp").readline()
  temp = temp.replace("'C","")
  temp = temp.replace("temp=","")
  temp = float(temp)
  return temp

print("%.2f" % measure_temp())
