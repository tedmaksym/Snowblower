import h5py 
import numpy as np
import os, glob
import cartopy.crs as ccrs
import cartopy
import matplotlib.pyplot as plt
import matplotlib.path as mpath

os.chdir("/home/jeffrey/Snowblower/jeffdata/")
ls = glob.glob("*.h5")
f = h5py.File(ls[-1], 'r') 
lat = f['gt1l/land_ice_segments/latitude'][:]
lon = f['gt1l/land_ice_segments/longitude'][:]
bsnow_conf = f['gt1l/land_ice_segments/geophysical/bsnow_conf'][:]
dt = f['gt1l/land_ice_segments/delta_time'][:]
h_li = f['gt1l/land_ice_segments/h_li'][:]
def show_plot(ax1):
	ax1.set_extent([-180, 180, -90, -65], ccrs.PlateCarree())
	ax1.add_feature(cartopy.feature.LAND)
	ax1.add_feature(cartopy.feature.OCEAN)
	theta = np.linspace(0, 2*np.pi, 100)
	center, radius = [0.5, 0.5], 0.5
	verts = np.vstack([np.sin(theta), np.cos(theta)]).T
	circle = mpath.Path(verts * radius + center)
	ax1.set_boundary(circle, transform=ax1.transAxes)
	plt.show()
	return

def plot_tracks(lon, lat, variable, time_range = None, **kwargs):
	global ax1
	if variable is not None:
		plt.scatter(lon, lat, c=variable, transform = ccrs.PlateCarree(), **kwargs)
	else:
		plt.plot(lon, lat, transform = ccrs.PlateCarree(), **kwargs)
	return 

ax1 = plt.subplot(111, projection=ccrs.SouthPolarStereo())	
plot_tracks(lon, lat, bsnow_conf)
plot_tracks(lon-90, lat, None)
cbar = plt.colorbar()
cbar.set_label("Colorbar Label")
show_plot(ax1)
# ax1.pcolormesh(xx, yy, variables[j], transform=data_crs)