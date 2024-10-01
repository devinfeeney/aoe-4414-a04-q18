# eci_to_ecef.py

# Usage: python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km
# Description: Converts Year, Month, Day, Hour, Minute, Second, eci_x_km, eci_y_km, eci_z_km inputs from the ECI frame to ECEF coordinates.

# Parameters:
#  year
#  month
#  day
#  hour
#  minute
#  second
#  eci_x_km
#  eci_y_km
#  eci_z_km

# Output:
#  Coordinates in the ecef reference frame (x, y, z), answer in km

# Written by Devin Feeney
# Other contributors: None

# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math
import sys

# "constants"
R_E_KM = 6378.137
e_E = 0.081819221456
r_E_km = 6378.1363
w = 0.00007292115
Delta_UT1 = 236.555

# initialize script arguments
year: float(sys.argv[1])
month: float(sys.argv[2])
day: float(sys.argv[3])
hour: float(sys.argv[4])
minute: float(sys.argv[5])
second: float(sys.argv[6])
eci_x_km: float(sys.argv[7])
eci_y_km: float(sys.argv[8])
eci_z_km: float(sys.argv[9])

# parse script arguments
if len(sys.argv)==10:
  year = float(sys.argv[1])
  month = float(sys.argv[2])
  day = float(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  second = float(sys.argv[6])
  eci_x_km = float(sys.argv[7])
  eci_y_km = float(sys.argv[8])
  eci_z_km = float(sys.argv[9])
else:
  print(\
   'Usage: '\
   'python3 eci_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km'\
  )
  exit()
 
# Calculate JD_frac
jd = day-32075+(1461*(year+4800+(month-14)/12)/4)+(367*(month-2-((month-14)/12)*12)/12)-(3*((year+4900+((month-14)/12))/100)/4)
jd_integer = int(jd)
jd_midnight = jd_integer-0.5
D_frac = (second+60*(minute+60*hour))/86400
JD_frac = jd_midnight+D_frac 

# Calculate JD_uti1
#JD_uti1 = JD_UTC + (Delta_UT1/JD_UTC)

# Calculate GMST Angle
T_ut1 = (JD_frac - 2451545.0)/36525
GMST_theta_s = 67310.54841+(876600*60*60+8640184.812866)*T_ut1+0.093104*(T_ut1**2)+(-6.2*(10**-6))*(T_ut1**3)
GMST_angle_rad = (GMST_theta_s % 86400)*w + 2*math.pi
GMST_rad_fin = (math.fmod(GMST_angle_rad, 2*math.pi))

# Calculate ECEF coordinates
ecef_x_km = (eci_x_km*math.cos(-GMST_rad_fin))+(eci_y_km*(-math.sin(-GMST_rad_fin)))
ecef_y_km = (eci_x_km*math.sin(-GMST_rad_fin))+(eci_y_km*math.cos(-GMST_rad_fin))
ecef_z_km = (eci_z_km)

# Display final answers
print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)

