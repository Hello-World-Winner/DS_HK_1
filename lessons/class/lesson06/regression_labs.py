import pandas as pd
import matplotlib.pyplot as plt
from numpy import log, exp, mean
from sklearn import linear_model, feature_selection

"""
Practice: Plotting Predictions
"""
mammals_log_brain = np.exp(log_lm.predict(log_body))

plt.scatter(body, mammals_log_brain, c='b', marker='o')
plt.plot(body, lm.predict(body),exp(log_body), np.exp(log_lm.predict(log_body)))
plt.show()

"""
Multivariable regressions
"""
regr = linear_model.LinearRegression()
regr.fit(input,)


"""
Find the best fitting model to predict breaking distance for car speed
"""

stop = pd.read_csv('./stop.csv')

speed = [[x] for x in stop['speed']]
dist = stop['dist'].values

regr = linear_model.LinearRegression()
regr.fit(speed, dist)

print "\nSpeed | Distance"
print "SSE : %0.4f" % (SSE(regr.predict(speed), dist)) # SSE : 227.0704
print "R2 : %0.4f" % (regr.score(speed, dist)) # R2 : 0.6511

plt.scatter(speed, dist, c='b', marker='o')
plt.plot(speed, regr.predict(speed), color='green')
plt.show()

stop['speed_squared'] = stop['speed'] ** 2
speed_squared = stop[['speed','speed_squared']].values

ridge = linear_model.Ridge()
ridge.fit(speed_squared, dist)

print "\nSpeed | Distance"
print "SSE : %0.4f" % (SSE(ridge.predict(speed_squared), dist)) # SSE : 216.4946
print "R2 : %0.4f" % (ridge.score(speed_squared, dist)) # R2 : 0.6673

plt.scatter(speed, dist, c='b', marker='o')
plt.plot(speed, ridge.predict(speed_squared), color='green')
plt.show()

stop['speed_boxed'] = stop['speed'] ** 3
speed_boxed = stop[['speed','speed_squared','speed_boxed']].values

ridge = linear_model.Ridge()
ridge.fit(speed_boxed, dist)

print "\nSpeed | Distance"
print "SSE : %0.4f" % (SSE(ridge.predict(speed_boxed), dist)) # SSE : SSE : 212.8165
print "R2 : %0.4f" % (ridge.score(speed_boxed, dist)) # R2 : 0.6730

plt.scatter(speed, dist, c='b', marker='o')
plt.plot(speed, ridge.predict(speed_boxed), color='green')
plt.show()


"""
Find the best fitting model to predict mileage for gallon
"""

cars = pd.read_csv('./cars.csv')

cars_input = cars._get_numeric_data()
cars_input = cars_input.dropna(axis=0)
mpg = cars_input['MPG.city']
cars_input = cars_input.drop(['MPG.highway','MPG.city'],1)
cars_input = cars_input.fillna(0)

fp_value = feature_selection.univariate_selection.f_regression(cars_input, mpg)
zip(cars_input.columns.values,fp_value[1])
fp = zip(p_value[1],cars_input.columns.values)
sorted(fp)

"""
Beers

"""

logm = linear_model.LogisticRegression()

def score(input, response):
  logm.fit(input, response)
  score = logm.score(input, good)
  print 'R^2 Score : %.03f' % (score)

def good(x):
  if x > 4.3:
    return 1
  else:
    return 0

url = 'http://www-958.ibm.com/software/analytics/manyeyes/datasets/af-er-beer-dataset/versions/1.txt'

beer = pd.read_csv(url, delimiter="\t")
beer = beer.dropna()
beer['Good'] = beer['WR'].apply(good)

# Original attempt

input = beer[ ['Reviews', 'ABV'] ].values
good = beer['Good'].values

score(input, good)

# Second attempt, with beer types

beer_types = ['Ale', 'Stout', 'IPA', 'Lager']

for t in beer_types:
	beer[t] = beer['Type'].str.contains(t) * 1

select = ['Reviews', 'ABV', 'Ale', 'Stout', 'IPA', 'Lager']
input = beer[select].values

score(input, good)

# Third attempt, with beer breweries

dummies = pd.get_dummies(beer['Brewery'])
input = beer[select].join(dummies.ix[:, 1:])

score(input, good)
