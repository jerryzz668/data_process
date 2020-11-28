from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm



x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
x = np.array(x).reshape((-1, 1))

y70gai = [43, 51, 59, 44, 39, 44, 44, 53, 54, 44, 64, 56, 51, 52, 48, 39, 40, 41, 42, 52, 46, 48, 51, 47, 50, 57, 53, 52, 56, 47, 50, 47, 46, 63, 54, 55, 52, 61, 48, 56, 56, 48, 52, 48, 51, 56, 56, 60, 48, 60, 48, 48, 48, 48, 51, 52, 53, 56, 48, 64, 51, 50, 39, 50, 51, 52, 51, 56, 56, 57]

model = LinearRegression()
model = model.fit(x, y70gai)
print(model)
# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
'''get result
y = b0 + b1x
'''
r_sq = model.score(x, y70gai)
print('coefficient of determination(𝑅²) :', r_sq)
# coefficient of determination(𝑅²) : 0.715875613747954
print('intercept:', model.intercept_)
# （标量） 系数b0 intercept: 5.633333333333329 -------this will be an array when y is also 2-dimensional
print('slope:', model.coef_)
# （数组）斜率b1 slope: [0.54]        ---------this will be 2-d array when y is also 2-dimensional

'''predict response
given x, get y from the model y = b0+b1x
'''
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')
#predicted response:
#[8.33333333 13.73333333 19.13333333 24.53333333 29.93333333 35.33333333]

'''forecast'''
z = [71,72,73]
z = np.array(x).reshape((-1,1))
# z = np.arange(71,72)
y = model.predict(z)
print(y)
#[5.63333333 6.17333333 6.71333333 7.25333333 7.79333333]