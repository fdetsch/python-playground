import pandas as pd

def lambda_handler(event, context):
    
    ## read iris data
    mldb = 'https://archive.ics.uci.edu/ml/machine-learning-databases'
    iris = pd.read_csv(mldb + '/iris/iris.data', names = None)
    
    ## set column names
    iris.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width', 'Species']
    
    ## transform species column
    iris['Species'] = iris['Species'].str.replace('Iris-', '')
    
    ## dump first 3 rows as json
    return {
        'statusCode': 200,
        'body': iris[:3].to_json()
    }

'''
# debug (use `None` to avoid 'missing 2 required positional arguments' error):
lambda_handler(None, None)
'''
