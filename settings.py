from local_settings import *
import numpy as np
default_r=0.5

#Approximation
lat_deg_to_km = 95.0
lon_deg_to_km = 110.0
buffer_radius = 1/np.sqrt(95*95+110*110)


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
