## 2021-12-06 ====

library(reticulate)

## as per https://pybind11.readthedocs.io/en/stable/installing.html
conda_install(packages = "pybind11")

py_install(
  "pybind11"
  , pip = TRUE
)

file.edit(
  "src/example.cpp"
)
