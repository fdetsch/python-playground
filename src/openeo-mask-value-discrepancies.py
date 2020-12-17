### ENVIRONMENT ====

### . modules ----

import openeo

import georaster
import matplotlib.pyplot as plt

import numpy as np


### . openeo ----

connection = openeo.connect("https://openeo.vito.be").authenticate_basic("test", "test123")


### PROCESSING ====

### . ndwi ----

sentinel2_data_cube = connection.load_collection(
  "SENTINEL2_L2A_SENTINELHUB"
  , spatial_extent = {'west':5.151836872,'east':5.1533818244,'south':51.181925592,'north':51.184696360,'crs':4326}
  , temporal_extent = ["2020-05-02", "2020-05-02"]
  , bands = ['B08','B12']
)

B08 = sentinel2_data_cube.band('B08')
B12 = sentinel2_data_cube.band('B12')

ndwi_cube = (B08 - B12) / (B08 + B12)
ndwi_cube.download("data/ndwi.tif", format = "GTiff")

# Use SingleBandRaster() if image has only one band
img = georaster.SingleBandRaster('data/ndwi.tif')
# img.r gives the raster in [height, width, band] format 
# band no. starts from 0
plt.imshow(img.r)
plt.show()
plt.clf()


### . scl ----

s2_scl = connection.load_collection(
  "SENTINEL2_L2A_SENTINELHUB"
  , spatial_extent = {'west':5.151836872,'east':5.1533818244,'south':51.181925592,'north':51.184696360,'crs':4326}
  , temporal_extent = ["2020-05-02", "2020-05-02"]
  , bands = ['SCL']
)

mask = s2_scl.band('SCL')
mask.download("data/scl.tif", format = "GTiff")

mask = mask != 4

ndwi_cube_masked = ndwi_cube.mask(mask) # .resample_cube_spatial(ndwi_cube)
ndwi_cube_masked.download("data/ndwi_masked.tif", format = "GTiff")

img1 = georaster.SingleBandRaster('data/ndwi_masked.tif')
plt.imshow(img1.r)
plt.show()
plt.clf()

georaster.MultiBandRaster
img - img1
