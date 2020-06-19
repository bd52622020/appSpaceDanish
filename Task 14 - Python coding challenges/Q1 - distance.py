#!/usr/bin/env python

try:
    import geopy.distance
except:
    print("Please install geopy using pip install geopy")

def distance():
    x = input("Please enter your Latitude: ")
    y = input("Please enter your Longitude: ")
    my_cords = (53.503090, -2.247090)
    new_cords = (x,y)
    miles = geopy.distance.vincenty(my_cords, new_cords).miles
    miles = int(miles)
    km = geopy.distance.vincenty(my_cords, new_cords).km
    km = int(km)
    print("The Distance between your location and mine is" , miles, "miles, or" , km, "km")
    
    
if __name__ == "__main__":
    distance()
    
