import numpy as np
from geopy import distance
from pyproj import Geod
from geographiclib.geodesic import Geodesic

# This module was created to calculate the distance considering Earth's form

def getDistanceGeopy(point1, point2):
    distance_2d = distance.distance(point1[:2], point2[:2]).m
    distance_3d = np.sqrt(distance_2d ** 2 + (point1[2] - point2[2]) ** 2)
    return np.around([distance_3d], decimals=2, out=None)[0]


def getDistanceGeod(point1, point2):
    '''Set Earth params'''
    g = Geod(ellips='WGS84')
    azimuth1, azimuth2, distance_2d = g.inv(point1[1], point1[0], point2[1], point2[0])
    distance_3d = np.hypot(distance_2d, point2[2] - point1[2])
    return np.around([distance_3d], decimals=2, out=None)[0]


def getDistanceGeodesic(point1, point2):
    geod = Geodesic.WGS84
    g = geod.Inverse(point1[0], point1[1], point2[0], point2[1])
    distance_3d = np.hypot(g['s12'], point2[2] - point1[2])
    return np.around([distance_3d], decimals=2, out=None)[0]
