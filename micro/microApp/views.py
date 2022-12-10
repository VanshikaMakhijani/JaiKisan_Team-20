from django.shortcuts import render,redirect
from .models import Farmer
import numpy as np
import pandas as pd
from math import radians, cos, sin, asin, acos, sqrt, pi
from geopy import distance
from geopy.geocoders import Nominatim
import osmnx as ox
import networkx as nx
import math
lat1, lon1 = -37.82120, 144.96441 # location 1
lat2, lon2 = -37.88465,  145.08727 # location 2

# Create your views here.
def homePage(request):
    return render(request,'microApp/home.html')

def registerFarmer(request):
    return render(request,'microApp/farmerDetails.html')

def farmerDetails(request):
        name=request.POST['name']
        age=request.POST['age']
        income=request.POST['income']
        members=request.POST['member']
        farmer = Farmer(name=name,age=age,income=income,noOfFamilyMembers=members)
        farmer.save()
        return render(request,'microApp/home.html')

# def calculate_spherical_distance(lat1, lon1, lat2, lon2, r=6371):
#     # Convert degrees to radians
#     coordinates = lat1, lon1, lat2, lon2
#     phi1, lambda1, phi2, lambda2 = [
#         radians(c) for c in coordinates
#     ]
    
#     # Apply the haversine formula
#     d = r*acos(cos(phi2-phi1) - cos(phi1) * cos(phi2) *
#               (1-cos(lambda2-lambda1)))
#     return d
# print(f"{calculate_spherical_distance(lat1, lon1, lat2, lon2):.4f} km")
# print(f"{distance.great_circle((lat1, lon1), (lat2, lon2)).km:.4f} km")

def executiveRegister(request):
    return render(request,'microApp/executive.html')

def executiveDetails(request):
    area=float(request.POST['area'])
    soil=request.POST['soil']
    crops=request.POST['crops']
    coordinates=request.POST['ll']
    # print(coordinates)
    coordinates=coordinates.split(",")
    areaC=0
    n=len(coordinates)
    if(n>2):
        for i in range(n-1):
             p1=coordinates[i]
             p2=coordinates[i+1]
             latitude1=float(p1.split()[0])
             longitude1=float(p1.split()[1])
             latitude2 = float(p2.split()[0])
             longitude2 =float(p2.split()[1])
             # print(p1,p2)
             print(latitude1,longitude1,latitude2,longitude2)
             areaC += math.radians(longitude2 - longitude1) * (
                    2 + math.sin(math.radians(latitude1)) + math.sin(math.radians(latitude2)))
        areaC=areaC*6378137*6378137/2
    areaC=math.fabs(areaC)
    if area==areaC:
        print("correct")
        return render(request,'microApp/success.html')
    else:
        print("incorrect")
        return render(request,'microApp/executive.html')





