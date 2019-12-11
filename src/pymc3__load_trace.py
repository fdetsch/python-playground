### PYMC3: GLM TUTORIAL ====
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


# ### . save trace ----
# 
# with pm.Model() as model:
#     s_data = pm.Data('s_data', data['x'])
#     # specify glm and pass in data. The resulting linear model, its likelihood and
#     # and all its parameters are automatically added to our model.
#     outcome = pm.glm.GLM(x = s_data, y = data['y'], labels = ['x'])
#     trace = pm.sample(500, cores = 1)
# 
# pm.save_trace(trace, 'pymc3_trace')
# 
# 
# ### . load trace ----
# 
# with pm.Model() as model:
#     s_data = pm.Data('s_data', data['x'])
#     outcome = pm.glm.GLM(x = s_data, y = data['y'], labels = ['x'])
# 
# trace = pm.load_trace('pymc3_trace', model)
# 
# with model:
#     pm.set_data({'s_data': data['x'][:1]})
#     ppc = pm.sample_posterior_predictive(trace, samples = 100, random_seed = 1899)


### . all in one ----
### (available online: https://github.com/pymc-devs/pymc3/pull/2975)

trace_file = 'inst\\python\\pymc3__load_trace'

with pm.Model() as model:
    s_data = pm.Data('s_data', data['x'])
    outcome = pm.glm.GLM(x = s_data, y = data['y'], labels = ['x'])
    
    if not os.path.exists(trace_file):
        trace = pm.sample(500, cores = 1)
        pm.save_trace(trace, directory = trace_file)
    else:
        trace = pm.load_trace(trace_file)
