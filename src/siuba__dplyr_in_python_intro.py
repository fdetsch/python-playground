## Code from "Siuba: Data wrangling with dplyr in Python"
## (available online: https://bit.ly/3mboSG6)

### Step 1: Load Libraries and Data ----

import pandas as pd
import numpy as np

from siuba import _
from siuba.dply.verbs import group_by, mutate, select, summarize, ungroup

mpg_df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"
)
mpg_df


### Step 2: Group By and Summarize ----

weight_by_cyl_df = mpg_df >> \
    group_by("cylinders") >> \
    summarize(
        mean_weight = np.mean(_.weight),
        sd_weight = np.std(_.weight)
    )


### Step 3: More Advanced Example (Group By and Mutate) ----

mpg_demeaned_by_cyl_df = mpg_df >> \
    select(_.name, _.cylinders, _.mpg) >> \
    group_by(_.cylinders) >> \
    mutate(
        mean_mpg = np.mean(_.mpg)
    ) >> \
    ungroup() >> \
    mutate(
        mpg_demeaned_by_cyl = _.mpg - _.mean_mpg
    )


### Step 4: From Siuba To Pandas ----

jnk = mpg_demeaned_by_cyl_df[['name', 'cylinders', 'mpg_demeaned_by_cyl']] \
    .sort_values('mpg_demeaned_by_cyl', ascending = False) \
    .style \
    .background_gradient()
jnk.render() # render styler to html
