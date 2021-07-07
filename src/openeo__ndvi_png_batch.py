## ENVIRONMENT ====

### modules ----

import openeo
from openeo.processes import ProcessBuilder


### openEO ----

## connect backend
con = openeo.connect(
    'https://openeo.vito.be'
).authenticate_oidc('egi')

## define child process for linear scaling
def scale_(x: ProcessBuilder):
    return x.linear_scale_range(-1, 1, 0, 255)


## PROCESSING ====

### area of interest ----

aoi = {"west": 5.5661, "south": 52.6457, "east": 5.7298, "north": 52.7335}


### openEO ----

## load collection
datacube = con.load_collection(
    'SENTINEL2_L2A_SENTINELHUB'
    , spatial_extent = aoi
    , temporal_extent = ["2021-04-27", "2021-04-27"]
    , bands = ['B04', 'B08']
)

## add ndvi layer, then drop red and nir bands
ndvicube = datacube.ndvi(
  nir = 'B08'
  , red = 'B04'
  , target_band = 'ndvi'
).band(
  band = 'ndvi'
)

## scale ndvi from [-1;1] to [0;255]
scalecube = ndvicube.apply(scale_)

## download directly, see attached `ndvi.png`
scalecube.download(
    outputfile = 'ndvi.png'
    , format = 'PNG'
)


### batch mode ----

job = scalecube.send_job(
    out_format = 'PNG'
)

job.start_job()
job.job_id # '65199d97-48b7-4c84-bb7b-dbc6285dc9fa'
job.status() # 'error' after some time
job.logs() # see attached `65199d97-48b7-4c84-bb7b-dbc6285dc9fa.log`
