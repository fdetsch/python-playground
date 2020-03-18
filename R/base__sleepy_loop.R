#' ---
#' title: '**reticulate** does not print to console in real time'
#' author: "`r Sys.getenv('USERNAME')`"
#' output:
#'   md_document
#' ---
#+ setup, include=FALSE
knitr::opts_chunk[['set']](collapse=FALSE, message=FALSE, warning=FALSE, prompt=FALSE)

#' The discussion related to this code is available on [StackOverflow](https://stackoverflow.com/questions/60736401/reticulate-doesnt-print-to-console-in-real-time).

#+ libs
library(reticulate)


#+ py_run_string
### . run code ----

py_run_string("
import time

for i in range(5):
   print(str(i))
   time.sleep(1.5)
")


#+ py_run_file
### . run file ----

py_run_file(
  "src/base__sleepy_loop.py"
)

#'
#' ### ZZ. Final things last
#'
#' <details><summary>Session info (click to view)</summary>
devtools::session_info()
#' </details>