# Time Series Analysis

## TIME SERIES DATA

Two main features characterize time series data from a statistical viewpoint: the correlation displayed by observations and their temporal sequence. Statistical models need to cope with the former, in order to provide accurate inferences, and may exploit the latter, with the intention to strengthen the evidence on the causal nature or clarify details of the association under study.

* **Time series data** : Measurements of the same data taken over a period of
(usually regular) intervals of time. E.g. _Stock returns, mortality, temperature_

* **Cross sectional data** : A snapshot in time of a group of data. E.g. _Beer, Mammals, Iris_

![](http://csm.lshtm.ac.uk/files/2010/09/series2.png)

#### Labs : [Taking a look at time series data](https://github.com/ga-students/DS_HK_1/wiki/Lesson-20-:-Time-Series-Analysis#time-series-analysis)

## DIFFERENCES IN TIME SERIES DATA

#### Assumptions of linear regression models
1. Linear relationship between dependent and independent variables
1. Independence of the errors (serial correlation)
1. Homoscedasticity (constant variance of the errors)
	1. Over time
	1. Between the variables
1. Normality of the errors

**Violations of linearity** are extremely serious--if you fit a linear model to data which are nonlinearly related, your predictions are likely to be seriously in error, especially when you extrapolate beyond the range of the sample data.

**Violations of independence** are also very serious in time series regression models: serial correlation in the residuals means that there is room for improvement in the model, and extreme serial correlation is often a symptom of a badly mis-specified model, as we saw in the auto sales example. Serial correlation is also sometimes a byproduct of a violation of the linearity assumption--as in the case of a simple (i.e., straight) trend line fitted to data which are growing exponentially over time.

**Violations of homoscedasticity** make it difficult to gauge the true standard deviation of the forecast errors, usually resulting in confidence intervals that are too wide or too narrow. In particular, if the variance of the errors is increasing over time, confidence intervals for out-of-sample predictions will tend to be unrealistically narrow. Heteroscedasticity may also have the effect of giving too much weight to small subset of the data (namely the subset where the error variance was largest) when estimating coefficients.

**Violations of normality** compromise the estimation of coefficients and the calculation of confidence intervals. Sometimes the error distribution is "skewed" by the presence of a few large outliers. Since parameter estimation is based on the minimization of squared error, a few extreme observations can exert a disproportionate influence on parameter estimates. Calculation of confidence intervals and various signficance tests for coefficients are all based on the assumptions of normally distributed errors. If the error distribution is significantly non-normal, confidence intervals may be too wide or too narrow.

Another important difference, unlike cross sectional models, the order of the data is VERY important.

#### Things to look for in time series data
* **Trends**, measurements tend to increase or decrease over time
* **Seasonality / Cyclicality**, An observable cycle in the data (days, years, weeks, secs, etc)

## AUTOREGRESSIVE MODELS

Autoregressive models use the value at time - 1 to predict the value at time 0

**Basic linear regression**

![ \gamma  =  \alpha  +  \beta _{x} +  \epsilon ](http://www.sciweavers.org/tex2img.php?eq=Y%20%3D%20%20%5Calpha%20%20%2B%20%20%5Cbeta%20_%7Bx%7D%20%2B%20%20%5Cepsilon%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

**Multivariate regression**

![Y = α + β_{1}x_{1} + β_{2}x_{2} + β_{3}x_{3} + \epsilon](http://www.sciweavers.org/tex2img.php?eq=Y%20%3D%20%CE%B1%20%2B%20%CE%B2_%7B1%7Dx_%7B1%7D%20%2B%20%CE%B2_%7B2%7Dx_%7B2%7D%20%2B%20%CE%B2_%7B3%7Dx_%7B3%7D%20%2B%20%CE%B5&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

**Autoregressive regression AR(1)**

![ \gamma_{i}  =  \phi_{0} +  \phi_{1}\gamma_{i-1} + \epsilon_{i}](http://www.sciweavers.org/tex2img.php?eq=%20%5Cgamma_%7Bi%7D%20%20%3D%20%20%5Cphi_%7B0%7D%20%2B%20%20%5Cphi_%7B1%7D%5Cgamma_%7Bi-1%7D%20%2B%20%CE%B5_%7Bi%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

* **Yi** : target variable
* **Φ0** : intercept (~ α, constant)
* **Φ1** : coefficient (~ β)
* **Yi-1** : lagged variable (~ x)
* **εi** : error

**Autoregressive regression AR(3)**

![ \gamma_{i}  =  \phi_{0} +  \phi_{1}\gamma_{i-1} + \phi_{2}\gamma_{i-2} + \phi_{3}\gamma_{i-3} + ε_{i}](http://www.sciweavers.org/tex2img.php?eq=%20%5Cgamma_%7Bi%7D%20%20%3D%20%20%5Cphi_%7B0%7D%20%2B%20%20%5Cphi_%7B1%7D%5Cgamma_%7Bi-1%7D%20%2B%20%5Cphi_%7B2%7D%5Cgamma_%7Bi-2%7D%20%2B%20%5Cphi_%7B3%7D%5Cgamma_%7Bi-3%7D%20%2B%20%CE%B5_%7Bi%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

### Stationary
Intuitively, a process {Xt} is stationary if its statistical properties do not change over time. More precisely, the probability distributions of the process are time-invariant.

## DIAGNOSTIC TOOLS

**Normality of the errors**

#### Labs : [Residuals plot](https://github.com/ga-students/DS_HK_1/wiki/Lesson-20-:-Time-Series-Analysis#residuals-plot)

**Independence of the errors (serial correlation)**

Indicates that there is room for improvement in our model – there is some association in the data that we are not taking into account. Our tool for this is called an **Autocorrelation plot**

**Autocorrelation** is the cross-correlation of a signal with itself. It is the similarity between observations as a function of the time lag between them. It is a mathematical tool for finding repeating patterns, such as the presence of a periodic signal obscured by noisel.
**Partial autocorrelation** is the autocorrelation between z_t and z_{t+k} that is not accounted for by lags 1 to k − 1, inclusive.

If the sample autocorrelation plot indicates that an AR model may be appropriate, then the sample partial autocorrelation plot is examined to help identify the order. One looks for the point on the plot where the partial autocorrelations for all higher lags are essentially zero.

![](https://raw.githubusercontent.com/ga-students/DS_HK_1/eec7d9853a147b2ac0eaeeb7fc908aa2f47f8444/lessons/class/lesson20/assets/ac1.png)

![](https://raw.githubusercontent.com/ga-students/DS_HK_1/eec7d9853a147b2ac0eaeeb7fc908aa2f47f8444/lessons/class/lesson20/assets/ac2.png)

![](https://raw.githubusercontent.com/ga-students/DS_HK_1/eec7d9853a147b2ac0eaeeb7fc908aa2f47f8444/lessons/class/lesson20/assets/ac3.png)

![](https://raw.githubusercontent.com/ga-students/DS_HK_1/eec7d9853a147b2ac0eaeeb7fc908aa2f47f8444/lessons/class/lesson20/assets/ac4.png)


The diagnostic patterns of ACF and PACF for an AR(1)  model are:
* ACF: declines in geometric progression from its highest value at lag 1
* PACF: cuts off abruptly after lag 1

The opposite types of patterns apply to an MA(1) process:
* ACF: cuts off abruptly after lag 1
* PACF: declines in geometric progression from its highest value at lag 1

#### Labs : [Sunspots data ACF and PACF (correlograms)](https://github.com/ga-students/DS_HK_1/wiki/Lesson-20-:-Time-Series-Analysis#autocorrelation-and-partial-autocorrelation-in-the-correlogram)

### Further Reading
* **Stationarity**
* **Unit root processes**
* **MA** (Moving average) regressions
* **ARMA** (Autoregressive moving average) regressions
* **ARIMA** (Autoregressive integrated moving average)
* **ARCH** (Autoregressive conditional heteroscedasticity)
* **EGARCH** (Exponential generalized ARCH)

#### Labs : [Other things to Play With](https://github.com/ga-students/DS_HK_1/wiki/Lesson-20-:-Time-Series-Analysis#other-things-to-play-with-arma-stationary-processes-unit-root-tests-macroeconomic-data)

## Resources

### Academic
* [Multivariate ARMAProcesses](http://www.le.ac.uk/users/dsgp1/COURSES/THIRDMET/MYLECTURES/10MULTARMA.pdf)
* [Invertability](http://www.econ.ohio-state.edu/dejong/note2.pdf)

### Concepts
[Multivariate ARMA Models](http://reference.wolfram.com/applications/timeseries/UsersGuideToTimeSeries/StationaryTimeSeriesModels/1.2.5.html)
* [Testing the assumptions of linear regression](http://people.duke.edu/~rnau/testing.htm)
* [Timeseries](http://www.colorado.edu/geography/class_homepages/geog_4023_s11/Lecture16_TS3.pdf)

### Demo
* [Subspot Plotting](http://nbviewer.ipython.org/gist/jhemann/4569783)
