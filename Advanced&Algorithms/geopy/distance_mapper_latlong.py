from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):    
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # 6367 km (3961 miles) is the radius of the Earth
    km = 6367 * c
    miles = 3961 * c
    return km, miles

city1 = input("Enter a city : ")
lat1 = input("Enter latitude of city :  ")
lat1 = float(lat1)
lon1 = input("Enter city longitude : ")
lon1 = float(lon1)

city2 = input("Enter a next city : ")
lat2 = input("Enter latitude of destination city :  ")
lat2 = float(lat2)
lon2 = input("Enter city longitude for destination : ")
lon2 = float(lon2)
km, miles = haversine(lon1, lat1, lon2, lat2)
sf = "The distance between {} and {} is {:0.1f} km (air)"
print(sf.format(city1, city2, km))
