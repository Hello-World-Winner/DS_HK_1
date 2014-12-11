from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
from numpy import log, exp, mean
from sklearn import linear_model


def SSE(pred,resp):
	return mean((pred - resp) ** 2)

"""
1. Go through the same steps, but this time generate a new model use the log of
brain and body, which we know generated a much better distribution and cleaner
set of data. Compare the results to the original model. Remember that exp()
can be used to "normalize" our "logged" values. ***Note: Make sure you start
a new linear regression object!***
"""

# Using iPythons magic function to set the current cirectory to my bookmarked data directory

mammals = pd.read_csv('./mammals.csv')
mammals['log_body'] = log(mammals['body'])
mammals['log_brain'] = log(mammals['brain'])

regr = linear_model.LinearRegression()
log_regr = linear_model.LinearRegression()


# Fit the data

body = [[x] for x in mammals['body'].values]
brain = mammals['brain'].values
regr.fit(body, brain)

# Fit the log data

log_body = [[x] for x in mammals['log_body'].values]
log_brain = mammals['log_brain'].values
log_regr.fit(log_body, log_brain)

plt.scatter(body, brain)
plt.plot(body, regr.predict(body), exp(log_body), exp(log_regr.predict(log_body)), color='red')
plt.show()

"""
2. Using your aggregate data compiled from nytimes1-30.csv, write a python 
script that determines the best model predicting CTR based off of age and 
gender. Since gender is not actually numeric (it is binary), investigate ways to
vectorize this feature. ***Clue: you may want two features now instead of one.***
"""

nyt = pd.read_csv('./nytimes.csv')

age_gender = nyt[['Age','Gender']].values
ctr = nyt['Ctr'].values

regr = linear_model.LinearRegression()
regr.fit(age_gender, ctr)

print "SSE : %0.4f" % (mean((regr.predict(age_gender) - ctr) ** 2))
print "R2 : %0.4f" % (regr.score(age_gender, ctr))


"""
3. Compare this practice to making two separate models based on Gender, with Age
as your one feature predicting CTR. How are your results different? Which 
results would you be more confident in presenting to your manager? Why's that?
"""
nyt_male = nyt[nyt['Gender'] == 1]
nyt_female = nyt[nyt['Gender'] == 0]

age_male = [[x] for x in nyt_male['Age'].values]
age_female = [[x] for x in nyt_female['Age'].values]
ctr_male = [x for x in nyt_male['Ctr'].values]
ctr_female = [x for x in nyt_female['Ctr'].values]

regr_male = linear_model.LinearRegression()
regr_female = linear_model.LinearRegression()

regr_male.fit(age_male, ctr_male)
regr_female.fit(age_female, ctr_female)

print "\nCTR | AGE ( Male )"
print "SSE : %0.4f" % (SSE(regr_male.predict(age_male), ctr_male))
print "R2 : %0.4f" % (regr_male.score(age_male, ctr_male))

print "\nCTR | AGE ( Female )"
print "SSE : %0.4f" % (SSE(regr_female.predict(age_female), ctr_female))
print "R2 : %0.4f" % (regr_female.score(age_female, ctr_female))

plt.scatter(age_male, ctr_male, c='r', marker='^')
plt.scatter(age_female, ctr_female, c='b', marker='o')
plt.plot(age_male, regr_male.predict(age_male), color='green')
plt.plot(age_female, regr_female.predict(age_female), color='pink')

plt.show()

"""
4. Evaluate what data you could still use to improve your nytimes model. 
Consider plotting your model to service your explanations and write a 
short blurb about insights gained and next steps in your "data collection."
"""

# def ratio(row):
#   if row[0] != 0:
#  	return row[0]/row[1]
#   else:
#     return 0

# nyt = pd.read_csv('./nytimes_full.csv')
# rows = np.random.choice(nyt.index.values, 10000)
# nyt = nyt.ix[rows]
# nyt = nyt[nyt['Age'] > 0]
# nyt = nyt[nyt['CTR'] > 0]

# nyt['CTR'] = nyt[['Clicks','Impressions']].apply(ratio, axis=1)

# age = nyt['Age'].values
# age_signedin = nyt[['Age','Signed_In']].values
# ctr = nyt['CTR'].values

# regr = linear_model.LinearRegression()
# regr.fit(age_signedin, ctr)

# print "SSE : %0.4f" % (SSE(regr.predict(age_signedin), ctr))
# print "R2 : %0.4f" % (regr.score(age_signedin, ctr))