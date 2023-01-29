import model

# Open and read a file with flight data
dataFlight = []
flyTrek = open('fly_trek.csv', 'r')

for line in flyTrek.readlines():
    s = list(map(str, line.split(',')))
    dataFlight.append(s)

flightDetails = model.DataParser(dataFlight)

# Dependency charts
flightDetails.generateChart("time-altitude")
flightDetails.generateChart("time-speed")
flightDetails.generateChart("time-distance")


# Flight details
print("Total distance:", flightDetails.getTotalDistance(), "m")
print("Average speed:", flightDetails.getAverSpeed(), "m/c")
print("Maximum speed:", flightDetails.getMaxSpeed(), "m/c")
print("Minimum speed:", flightDetails.getMinSpeed(), "m/c")
print("Maximum altitude:", flightDetails.getMaxAltitude(), "m")
print("Minimum altitude:", flightDetails.getMinAltitude(), "m")
print("Total flight time:", flightDetails.getTimeFlight(), "s")
