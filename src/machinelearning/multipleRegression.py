import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt


#1. Load the data
data = pd.read_csv('APPL.csv', encoding='utf-8')
print("data columns: ",data.columns.to_list())
print("data head ",data.head())

data.columns = data.columns.str.strip().str.capitalize()

reqColumns = ['Open','High','Low','Close','Volume']

missingCol = [col for col in reqColumns if col not in data.columns]
if missingCol:
    print("missing columns are: ", missingCol)



#2. Define independent variables and target variables
X = data[['Open','High','Low','Volume']]
#y = data[]
print(X)


'''
#3. Split the data into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

#4. Initialize the test set
model = LinearRegression()
model.fit(X_train, y_train)

#5. Make a prediction
y_pred = model.predict(X_test)


#6. Evaluate the model
meansqerr = mean_squared_error(y_test, y_pred)
r2sq = r2_score(y_test, y_pred)

print('Coefficient: ', model.coef_)
print('Intercept: ', model.intercept_)

#6. Visualize Actual vs Prediction
plt.scatter(y_test, y_pred, color="red", label="Prediction vs Actual")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label="Perfect fit")
plt.xlabel('Actual Close Price')
plt.ylabel('Predicted Close Price')
plt.legend()
plt.savefig('prediction.png', dpi=200, bbox_incehes = 'tight')
plt.show()

#176.5, 200.67
#176.5, 200.67
'''
