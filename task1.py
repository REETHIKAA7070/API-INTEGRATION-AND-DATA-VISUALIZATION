import matplotlib.pyplot as plt

print("Program started")

# Simulated API data (acts like fetched data)
cities = ["Chennai", "Delhi", "Mumbai", "Bangalore"]
temperatures = [32, 35, 30, 28]

print("Fetched temperature data:", temperatures)

plt.bar(cities, temperatures)
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")
plt.title("City Temperature Analysis")
plt.show()
