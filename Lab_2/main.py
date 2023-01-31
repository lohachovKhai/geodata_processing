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
flightDetails.generateChart("latitude - longitude - altitude")

# Required tables
flightDetails.generateTable("Table_1")
flightDetails.generateTable("Table_2")
