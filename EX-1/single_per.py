import pandas as pd
from sklearn.linear_model import Perceptron

dia = pd.read_csv('diabetes.csv').values
x = dia[:,0:8]
y = dia[:, 8]
model = Perceptron(random_state=1)
model.fit(x,y)
print("%0.3f"%model.score(x,y))
