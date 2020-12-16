import openeo
import rasterio
import numpy as np

connection = openeo.connect("https://openeo.vito.be").authenticate_basic("test", "test123")


### . ndwi ----

sentinel2_data_cube = connection.load_collection(
  "SENTINEL2_L2A_SENTINELHUB"
  , spatial_extent = {'west':5.151836872,'east':5.1533818244,'south':51.181925592,'north':51.184696360,'crs':4326}
  , temporal_extent = ["2020-05-01", "2020-05-10"]
  , bands = ['B08','B12']
)

B08 = sentinel2_data_cube.band('B08')
B12 = sentinel2_data_cube.band('B12')

ndwi_cube = (B08 - B12) / (B08 + B12)
ndwi_cube.download("data/ndwi.tif", format = "GTiff")

## value range
img = rasterio.open("data/ndwi.tif")
[img.read(1).min(), img.read(1).max()]
# [-0.26342073, 0.6292848]


### . scl ----

s2_scl = connection.load_collection(
  "SENTINEL2_L2A_SENTINELHUB"
  , spatial_extent = {'west':5.151836872,'east':5.1533818244,'south':51.181925592,'north':51.184696360,'crs':4326}
  , temporal_extent = ["2020-05-01", "2020-05-10"]
  , bands = ['SCL']
)

mask = s2_scl.band('SCL')
mask = mask != 4

ndwi_cube_masked = ndwi_cube.mask(mask) # .resample_cube_spatial(ndwi_cube)
ndwi_cube_masked.download("data/ndwi_masked.tif", format = "GTiff")

img1 = rasterio.open("data/ndwi_masked.tif")

## value range
[np.nanmin(img1.read(1)), np.nanmax(img1.read(1))]
# [-0.06359782, 0.703763]
