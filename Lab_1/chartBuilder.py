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
    pointColor = None

    fig.set(facecolor=faceColor)
    ax.plot(xData, yData, color=colorPlot)
    ax.set_xlabel(xlabel, fontsize=20)
    ax.set_ylabel(ylabel, fontsize=20)
    plt.title(title, fontsize=20)
    dots = ax.scatter(xData, yData, color=colorPlot)
    plt.legend(['dependency', 'checkpoint'], loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=12,
               frameon=True)
    ax.xaxis.set_major_formatter(myFmt)
    crs = mplcursors.cursor(dots, hover=True)
    crs.connect("add", lambda sel: sel.annotation.set_text(textRun(sel.annotation.get_text())))
    plt.show()


# Function for splitting dependencies charts/plots
def createChart(value, dependency):
    match dependency:
        case "time-speed":
            chartBuilder(value._timeForChart, value._chartSpeed, 'time', \
                                    'speed', '', 'black')
        case "time-altitude":
            chartBuilder(value._timeHigh, value._arrHight, 'time', \
                                    'altitude (m)', '', 'navy')
        case "time-distance":
            chartBuilder(value._timeForChart, value._chartDistance, 'time', \
                                    'distance (m)', '', 'crimson')
