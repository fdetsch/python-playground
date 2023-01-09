### Say Goodbye to Loops in Python, and Welcome Vectorization! ----
### (available online: https://medium.com/codex/say-goodbye-to-loops-in-python-and-welcome-vectorization-e4df66615a52)

import time 
import numpy as np
import pandas as pd
import datatable as dt
from datatable import f, ifelse, update


## SUM OF NUMBERS ====

### loop ----

start = time.time()

# iterative sum
total = 0
# iterating through 1.5 Million numbers
for item in range(0, 1500000):
    total += item

print('sum is:' + str(total))
#1124999250000

end = time.time()
print(end - start)
#0.22 Seconds


### vectorized ----

start = time.time()

# vectorized sum - using numpy for vectorization
# np.arange create the sequence of numbers from 0 to 1499999
print(np.sum(np.arange(1500000)))
##1124999250000

end = time.time()
print(end - start)
## 0.05 s


## MATH OPS ====

### sample data ----

df = pd.DataFrame(np.random.randint(0, 50, size=(500000, 4)), columns=('a','b','c','d'))
df.shape
# (500000, 5)
df.head()

DT = dt.Frame(df)


### loop ----

start = time.time()

# Iterating through DataFrame using iterrows
for idx, row in df.iterrows():
    # creating a new column 
    df.at[idx,'ratio'] = 100 * (row["d"] / row["c"])

end = time.time()
print(end - start)
## 26.9 s


### pandas ----

start = time.time()
df["ratio"] = 100 * (df["d"] / df["c"])

end = time.time()
print(end - start)
## 0.032 s


### datatable ----

start = time.time()
DT['ratio'] = DT[:, 100 * (f.d / f.c)]

end = time.time()
print(end - start)
## 0.027 s


## IF-ELSE STATEMENTS ====

### loops ----

start = time.time()

# Iterating through DataFrame using iterrows
for idx, row in df.iterrows():
    if row.a == 0:
        df.at[idx,'e'] = row.d    
    elif (row.a <= 25) & (row.a > 0):
        df.at[idx,'e'] = (row.b)-(row.c)    
    else:
        df.at[idx,'e'] = row.b + row.c

end = time.time()
print(end - start)
## 39.3 s


### pandas ----

start = time.time()

df['e'] = df['b'] + df['c']
df.head(10)

df.loc[df['a'] <= 25, 'e'] = df['b'] -df['c']
df.loc[df['a']==0, 'e'] = df['d']
end = time.time()
print(end - start)
## 0.076 s


### datatable ----

start = time.time()

DT['e'] = DT[:, f.b + f.c]
DT.head(10)

DT[:, update(e = ifelse(f.a <= 25, f.b - f.c, f.a == 0, f.d, f.e))]

end = time.time()
print(end - start)
## 0.046 s
