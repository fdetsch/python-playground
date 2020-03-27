The discussion related to this code is available on
[StackOverflow](https://stackoverflow.com/questions/60736401/reticulate-doesnt-print-to-console-in-real-time).

``` r
library(reticulate)
```

``` r
### QUESTION ====

### . run code ----

py_run_string("
import time

for i in range(5):
   print(str(i))
   time.sleep(1.5)
")
```

``` r
### . run file ----

py_run_file(
  "src/base__sleepy_loop.py"
)
```

``` r
### SOLUTION ====

## sys.stdout.flush()
py_run_string("
import time
from sys import stdout

for i in range(5):
   print(str(i))
   sys.stdout.flush()
   time.sleep(1.5)
")
# 0
# 1
# 2
# 3
# 4

## print(..., flush = True)
py_run_string("
import time

for i in range(5):
   print(str(i), flush = True)
   time.sleep(1.5)
")
# 0
# 1
# 2
# 3
# 4
```

### ZZ. Final things last

<details>

<summary>Session info (click to view)</summary>

``` r
devtools::session_info()
```

    ## - Session info ---------------------------------------------------------------
    ##  setting  value                       
    ##  version  R version 3.6.3 (2020-02-29)
    ##  os       Windows 10 x64              
    ##  system   x86_64, mingw32             
    ##  ui       RTerm                       
    ##  language (EN)                        
    ##  collate  German_Germany.1252         
    ##  ctype    German_Germany.1252         
    ##  tz       Europe/Berlin               
    ##  date     2020-03-27                  
    ## 
    ## - Packages -------------------------------------------------------------------
    ##  package     * version   date       lib source                             
    ##  assertthat    0.2.1     2019-03-21 [1] CRAN (R 3.6.1)                     
    ##  backports     1.1.5     2019-10-02 [1] CRAN (R 3.6.1)                     
    ##  callr         3.4.2     2020-02-12 [1] CRAN (R 3.6.2)                     
    ##  cli           2.0.2     2020-02-28 [1] CRAN (R 3.6.2)                     
    ##  clisymbols    1.2.0     2017-05-21 [1] CRAN (R 3.6.1)                     
    ##  crayon        1.3.4     2017-09-16 [1] CRAN (R 3.6.1)                     
    ##  desc          1.2.0     2018-05-01 [1] CRAN (R 3.6.1)                     
    ##  devtools      2.2.2     2020-02-17 [1] CRAN (R 3.6.2)                     
    ##  digest        0.6.25    2020-02-23 [1] CRAN (R 3.6.2)                     
    ##  ellipsis      0.3.0     2019-09-20 [1] CRAN (R 3.6.1)                     
    ##  evaluate      0.14      2019-05-28 [1] CRAN (R 3.6.1)                     
    ##  fansi         0.4.1     2020-01-08 [1] CRAN (R 3.6.2)                     
    ##  fs            1.3.2     2020-03-05 [1] CRAN (R 3.6.3)                     
    ##  glue          1.3.2     2020-03-12 [1] CRAN (R 3.6.3)                     
    ##  highr         0.8       2019-03-20 [1] CRAN (R 3.6.1)                     
    ##  htmltools     0.4.0     2019-10-04 [1] CRAN (R 3.6.1)                     
    ##  jsonlite      1.6.1     2020-02-02 [1] CRAN (R 3.6.2)                     
    ##  knitr         1.28      2020-02-06 [1] CRAN (R 3.6.2)                     
    ##  lattice       0.20-38   2018-11-04 [2] CRAN (R 3.6.3)                     
    ##  magrittr      1.5       2014-11-22 [1] CRAN (R 3.6.1)                     
    ##  Matrix        1.2-18    2019-11-27 [2] CRAN (R 3.6.3)                     
    ##  memoise       1.1.0     2017-04-21 [1] CRAN (R 3.6.1)                     
    ##  pkgbuild      1.0.6     2019-10-09 [1] CRAN (R 3.6.1)                     
    ##  pkgload       1.0.2     2018-10-29 [1] CRAN (R 3.6.1)                     
    ##  prettyunits   1.1.1     2020-01-24 [1] CRAN (R 3.6.2)                     
    ##  processx      3.4.2     2020-02-09 [1] CRAN (R 3.6.2)                     
    ##  prompt        1.0.0     2020-01-23 [1] Github (gaborcsardi/prompt@b332c42)
    ##  ps            1.3.2     2020-02-13 [1] CRAN (R 3.6.2)                     
    ##  R6            2.4.1     2019-11-12 [1] CRAN (R 3.6.1)                     
    ##  Rcpp          1.0.4     2020-03-17 [1] CRAN (R 3.6.3)                     
    ##  remotes       2.1.1     2020-02-15 [1] CRAN (R 3.6.2)                     
    ##  reticulate  * 1.14-9002 2020-03-27 [1] Github (rstudio/reticulate@21a9518)
    ##  rlang         0.4.5     2020-03-01 [1] CRAN (R 3.6.2)                     
    ##  rmarkdown     2.1       2020-01-20 [1] CRAN (R 3.6.2)                     
    ##  rprojroot     1.3-2     2018-01-03 [1] CRAN (R 3.6.1)                     
    ##  rstudioapi    0.11      2020-02-07 [1] CRAN (R 3.6.2)                     
    ##  sessioninfo   1.1.1     2018-11-05 [1] CRAN (R 3.6.1)                     
    ##  stringi       1.4.6     2020-02-17 [1] CRAN (R 3.6.2)                     
    ##  stringr       1.4.0     2019-02-10 [1] CRAN (R 3.6.1)                     
    ##  testthat      2.3.2     2020-03-02 [1] CRAN (R 3.6.3)                     
    ##  usethis       1.5.1     2019-07-04 [1] CRAN (R 3.6.1)                     
    ##  withr         2.1.2     2018-03-15 [1] CRAN (R 3.6.1)                     
    ##  xfun          0.12      2020-01-13 [1] CRAN (R 3.6.2)                     
    ##  yaml          2.2.1     2020-02-01 [1] CRAN (R 3.6.2)                     
    ## 
    ## [1] C:/Users/florianD/Documents/R/win-library/3.6
    ## [2] C:/Program Files/R/R-3.6.3/library

</details>
