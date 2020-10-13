Numba: JIT Compilation, But For Python
================
2020-10-13

Code taken from and details available
[here](https://towardsdatascience.com/numba-jit-compilation-but-for-python-373fc2f848d6).

### Single core

``` python
import random
import time
from numba import jit

def monte_carlo_pi(nsamples = int(1e7)):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

start_time = time.time()
r1 = monte_carlo_pi()
print("--- %s seconds ---" % (time.time() - start_time))
```

    ## --- 6.61634635925293 seconds ---

### Multi core

``` python
### . multi core ----

@jit(nopython=True)
def monte_carlo_pi(nsamples = int(1e7)):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

start_time = time.time()
r2 = monte_carlo_pi()
print("--- %s seconds ---" % (time.time() - start_time))
```

    ## --- 0.6127605438232422 seconds ---
