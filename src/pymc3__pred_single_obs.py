### Code taken from GLM: Linear Regression ====
### (available online: https://docs.pymc.io/notebooks/GLM-linear.html)

import numpy as np
import pymc3 as pm

size = 200
true_intercept = 1
true_slope = 2

x = np.linspace(0, 1, size)

# y = a + b*x
true_regression_line = true_intercept + true_slope * x

# add noise
y = true_regression_line + np.random.normal(scale=.5, size=size)

data = dict(x=x, y=y)

# train model
with pm.Model() as model:
    s_data = pm.Data('s_data', data['x'])
    # specify glm and pass in data. The resulting linear model, its likelihood
    # and all its parameters are automatically added to our model.
    outcome = pm.glm.GLM(x = s_data, y = data['y'], labels = ['x'])
    trace = pm.sample(250, cores = 1)

# predict new data (1 observation)
with model:
    pm.set_data({'s_data': data['x'][:1]})
    ppc = pm.sample_posterior_predictive(trace, samples = 20, random_seed = 1899)

len(ppc['y'][0]) # 200

# predict new data (2+ observations)
with model:
    pm.set_data({'s_data': data['x'][:2]})
    ppc = pm.sample_posterior_predictive(trace, samples = 20, random_seed = 1899)

len(ppc['y'][0]) # 2
