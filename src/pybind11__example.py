import os


### pybind11 ----

## as per https://pybind11.readthedocs.io/en/stable/basics.html
jnk = os.system(
    'c++ -O3 -Wall -shared -std=c++11 ' + 
    '-fPIC $(python3 -m pybind11 --includes) src/example.cpp ' + 
    '-o example$(python3-config --extension-suffix)'
) # `0` means success

import example

# ## use `reload(example)` after making changes, doesn't seem to work in rstudio
# from importlib import reload
# module = reload(example)

example.add(i = 2, j = 3)
example.add() # uses defaults

help(example)
