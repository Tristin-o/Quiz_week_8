import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r".\climate.csv")

years = []
co2 = []
temp = []

years.append(data['Year'])
co2.append(data['CO2'])
temp.append(data['Temperature'])

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'r*-')
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png")

