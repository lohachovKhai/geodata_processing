import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplcursors


# Matplot function for generating charts/plots
def chartBuilder(xData, yData, xlabel, ylabel, title, colorPlot):
    def textRun(annotation):
        syt = annotation.replace('x', xlabel)
        syt = syt.replace('y', ylabel)
        return syt

    plt.style.use('seaborn-v0_8')
    myFmt = mdates.DateFormatter('%H:%M:%S')
    fig, ax = plt.subplots()

    faceColor = None

    fig.set(facecolor=faceColor)
    ax.plot(xData, yData, color=colorPlot)
    ax.set_xlabel(xlabel, fontsize=20)
    ax.set_ylabel(ylabel, fontsize=20)
    plt.title(title, fontsize=20)
    dots = ax.scatter(xData, yData, color=colorPlot)
    ax.xaxis.set_major_formatter(myFmt)
    crs = mplcursors.cursor(dots, hover=True)
    crs.connect("add", lambda sel: sel.annotation.set_text(textRun(sel.annotation.get_text())))
    plt.show()

def chartBuilder3D(xData, yData, zData, xlabel, ylabel, zLabel, title):

    fig = plt.figure()
    fig.set(facecolor='grey')
    ax = fig.add_subplot(projection='3d')
    plt.title(title)
    ax.plot3D(xData, yData, zData, 'black', label="")
    ax.scatter3D(xData, yData, zData, label="")

    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.set_zlabel(zLabel, fontsize=15)
    ax.legend(loc=2)

    plt.show()


# Function for splitting dependencies charts/plots
def createChart(value, dependency):
    match dependency:
        case "time-speed":
            chartBuilder(value._timeForChart, value._velocity, 'time', \
                         'velocity', '', 'black')
        case "time-altitude":
            chartBuilder(value._timeHigh, value._arrHight, 'time', \
                         'altitude (m)', '', 'navy')
        case "time-distance":
            chartBuilder(value._timeForChart, value._chartDistance, 'time', \
                         'distance (m)', '', 'crimson')
        case "latitude - longitude - altitude":
            chartBuilder3D(value._latitude, value._longtitude, value._arrHight, \
                         'Latitude', 'Longitude', 'Altitude (m)', '')
