from django.shortcuts import render,redirect
from .models import Farmer
import numpy as np
import pandas as pd
from math import radians, cos, sin, asin, acos, sqrt, pi
from geopy import distance
from geopy.geocoders import Nominatim
import osmnx as ox
import networkx as nx
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
    pass



