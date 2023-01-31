import numpy as np
import distanceCalculator
import chartBuilder
from datetime import datetime
import tablePrinter

class DataParser:
    def __init__(self, arrData, distanceMethod="Geopy"):
        self._arrData = arrData
        self.executeFlight(self._arrData, distanceMethod)

    def executeFlight(self, arrData, distanceMethod="Geopy"):
        sumDis = 0
        maxSpeed = 0
        minSpeed = 5000
        minFlight = float(arrData[0][9])
        maxFlight = float(arrData[0][9])
        arrDis = [0]
        arrSpeed = [0]
        arrHight = [arrData[0][9]]
        latitude = [float(arrData[0][2])/100]
        longitude = [float(arrData[0][4])/100]

        for i in range(1, len(arrData)):
            point1 = [float(arrData[i - 1][2]) / 100, float(arrData[i - 1][4]) / 100, float(arrData[i - 1][9])]
            point2 = [float(arrData[i][2]) / 100, float(arrData[i][4]) / 100, float(arrData[i][9])]
            dis2point = None
            match distanceMethod:
                case "Geopy":
                    dis2point = distanceCalculator.getDistanceGeopy(point1, point2)
                case "Geod":
                    dis2point = distanceCalculator.getDistanceGeod(point1, point2)
                case "Geodesic":
                    dis2point = distanceCalculator.getDistanceGeodesic(point1, point2)

            sumDis += dis2point
            arrDis.append(sumDis)
            arrSpeed.append(float(dis2point))
            arrHight.append(float(arrData[i][9]))
            maxSpeed = max(dis2point, maxSpeed)
            minSpeed = min(dis2point, minSpeed)
            minFlight = min(float(arrData[i][9]), minFlight)
            maxFlight = max(float(arrData[i][9]), maxFlight)


            latitude.append(float(arrData[i][2])/100)
            longitude.append(float(arrData[i][4])/100)
            latitude[i] = np.around([float(latitude[i])], decimals=6, out=None)[0]
            longitude[i] = np.around([float(longitude[i])], decimals=6, out=None)[0]

        # Transform to numpy array
        arrSpeed = np.array(arrSpeed)
        arrSpeed = arrSpeed.astype(np.float64)
        arrHight = np.array(arrHight)
        arrHight = arrHight.astype(np.float64)
        arrDis = np.array(arrDis)
        arrDis = arrDis.astype(np.float64)

        longitude = np.array(longitude)
        longitude = longitude.astype(np.float64)
        latitude = np.array(latitude)
        latitude = latitude.astype(np.float64)

        timeHigh = []
        for i in range(0, len(arrData)):
            strD = arrData[i][1][:-3]
            datetime_object = datetime.strptime(strD, '%H%M%S')
            timeHigh.append(datetime_object)
        # total seconds
        resultTime = timeHigh[len(timeHigh) - 1] - timeHigh[0]



        # Separate arrays for better representing dependencies charts for *speed from time* and *distance from time*
        timeForChart = []
        for i in range(1, len(timeHigh)):
            timeForChart.append(timeHigh[i])

        velocity = []
        for i in range(1, len(arrSpeed)):
            velocity.append(arrSpeed[i])

        chartDistance = []
        for i in range(1, len(arrDis)):
            chartDistance.append(arrDis[i])

        # data request
        self._maxSpeed = maxSpeed
        self._minSpeed = minSpeed
        self._minFlight = minFlight
        self._maxFlight = maxFlight
        self._sumDis = sumDis
        self._averSpeed = sumDis / (len(arrDis) - 1)
        self._timeFlight = resultTime.total_seconds()

        # array for charts
        self._chartDistance = chartDistance
        self._velocity = velocity
        self._timeForChart = timeForChart
        self._timeHigh = timeHigh
        self._arrSpeed = arrSpeed
        self._arrHight = arrHight
        self._arrDis = arrDis
        self._longtitude = longitude
        self._latitude = latitude


    def getMinAltitude(self):
        return np.around([self._minFlight], decimals=2, out=None)[0]

    def getMaxAltitude(self):
        return np.around([self._maxFlight], decimals=2, out=None)[0]

    def getTotalDistance(self):
        return np.around([self._sumDis], decimals=2, out=None)[0]

    def getTimeFlight(self):
        return np.around([self._timeFlight], decimals=2, out=None)[0]

    def getAverSpeed(self):
        return np.around([self._averSpeed], decimals=2, out=None)[0]

    def getMaxSpeed(self):
        return np.around([self._maxSpeed], decimals=2, out=None)[0]

    def getMinSpeed(self):
        return np.around([self._minSpeed], decimals=2, out=None)[0]

    def generateChart(self, dependency):
        chartBuilder.createChart(self, dependency)

    def generateTable(self, type):
        tablePrinter.tableSeparator(self, type)
