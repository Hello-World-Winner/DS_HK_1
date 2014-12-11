## Classification problems

## Building Effective Classifiers

### Training error
	Training error is the average loss over the training data

### Test / generalization error
	The expected error over an independent test sample drawn from the same 
	distribution as that of the training data.

### OOS error
	Out of Sample error is the error when using the trained model to predict 
	instances it hasn't seen before. Often predicted by taking the mean of 
	Cross-Validated test errors.

### Holdout method
	 The data set is separated into two sets, called the training set and the 
	 testing set. The function approximator fits a function using the training 
	 set only.

### N-Fold Cross-validation
	 The data set is divided into n subsets, and the holdout method is repeated 
	 n times. Each time, one of the n subsets is used as the test set and the 
	 other n-1 subsets are put together to form a training set. Then the average 
	 error across all n trials is computed.

## KNN classification

* To prevent ties, one typically uses an odd choice of k for binary classification.
* Linear regression is an example of a parametric method; k-nearest-neighbor is an example of a
nonparametric method.

### Euclidean distance function
Euclidean distance is typical for continuous variables, but other metrics can be used for categorical data.

### Drawbacks
* What is features aren't same units?
* What if the data isn't normalised?
* What if one feature is more important than the other?

```python
"""
Normalise a dataframe, centered around 0
"""

df_norm = (df - df.mean()) / (df.max() - df.min())

```

```python
"""
Normalise a set of columns in a dataframe, between 0 and 1
"""

df_norm = (df - df.min()) / (df.max() - df.min())

```

```python
"""
Normalise a set of columns in a dataframe, between 0 and 1
"""

sepals = [sepal length (cm)','sepal width (cm)']
petals = ['petal length (cm)','petal width (cm)']
df_weighted = pd.DataFrame.join(df[sepals] * 2, df[petals] / 2)

```

#### Advantages

* Very simple implementation.
* Robust with regard to the search space; for instance, classes don't have to be linearly separable.
* Classifier can be updated online at very little cost as new instances with known classes are presented.
* Few parameters to tune: distance metric and k.

#### Disadvantages

* Expensive testing of each instance, as we need to compute its distance to all known instances. Specialized algorithms and heuristics exist for specific problems and distance functions, which can mitigate this issue. This is problematic for datasets with a large number of attributes. When the number of instances is much larger than the number of attributes, a R-tree or a kd-tree can be used to store instances, allowing for fast exact neighbor identification.
* Sensitiveness to noisy or irrelevant attributes, which can result in less meaningful distance numbers. Scaling and/or feature selection are typically used in combination with kNN to mitigate this issue.
* Sensitiveness to very unbalanced datasets, where most entities belong to one or a few classes, and infrequent classes are therefore often dominated in most neighborhoods. This can be alleviated through balanced sampling of the more popular classes in the training stage, possibly coupled with ensembles.

## Follow-up

In later classes we'll look back at this dataset and implement the following scoring functions for the IRIS dataset
* ROC 
* LogLoss
* Sensitivity (& recall)
* Specificity (& precision)


## Extra

[KNN in Simple Terms](http://www.jiaaro.com/KNN-for-humans/)
[Should I normalize/standardize/rescale?](http://www.faqs.org/faqs/ai-faq/neural-nets/part2/section-16.html)
### Tools
[NN Algorythms in SciKit Learn](http://scikit-learn.org/stable/modules/neighbors.html)
[Datasets provided by SciKit Learn](http://scikit-learn.org/stable/datasets/)
[Matplotlib Colormaps](http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps)
[Model evaluation](http://scikit-learn.org/stable/modules/model_evaluation.html)

## Examples

[Intuitive Classification using KNN and Python](http://blog.yhathq.com/posts/classification-using-knn-and-python.html)

## Code Examples

```python
from pandas.tools.plotting import parallel_coordinates

"""
Parallel Coordinates plot of the Iris Dataset

(Follow-up to the class lab, so do those first)
"""

df = pd.DataFrame(iris.data, columns=iris.feature_names)
species = [iris.target_names[x - 1] for x in iris.target]
df = df.join(pd.DataFrame(species, columns=['Species']))

plt.figure()
parallel_coordinates(df, 'Species', colormap='gist_rainbow')
plt.show()
```

```python

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def parallel_coordinates(data_sets, style=None):
"""
Hacked version of Parallel Coordinates, which allows for scaled axis
"""
    dims = len(data_sets[0])
    x    = range(dims)
    fig, axes = plt.subplots(1, dims-1, sharey=False)

    if style is None:
        style = ['r-']*len(data_sets)

    # Calculate the limits on the data
    min_max_range = list()
    for m in zip(*data_sets):
        mn = min(m)
        mx = max(m)
        if mn == mx:
            mn -= 0.5
            mx = mn + 1.
        r  = float(mx - mn)
        min_max_range.append((mn, mx, r))

    # Normalize the data sets
    norm_data_sets = list()
    for ds in data_sets:
        nds = [(value - min_max_range[dimension][0]) / 
                min_max_range[dimension][2] 
                for dimension,value in enumerate(ds)]
        norm_data_sets.append(nds)
    data_sets = norm_data_sets

    # Plot the datasets on all the subplots
    for i, ax in enumerate(axes):
        for dsi, d in enumerate(data_sets):
            ax.plot(x, d, style[dsi])
        ax.set_xlim([x[i], x[i+1]])

    # Set the x axis ticks 
    for dimension, (axx,xx) in enumerate(zip(axes, x[:-1])):
        axx.xaxis.set_major_locator(ticker.FixedLocator([xx]))
        ticks = len(axx.get_yticklabels())
        labels = list()
        step = min_max_range[dimension][2] / (ticks - 1)
        mn   = min_max_range[dimension][0]
        for i in xrange(ticks):
            v = mn + i*step
            labels.append('%4.2f' % v)
        axx.set_yticklabels(labels)


    # Move the final axis' ticks to the right-hand side
    axx = plt.twinx(axes[-1])
    dimension += 1
    axx.xaxis.set_major_locator(ticker.FixedLocator([x[-2], x[-1]]))
    ticks = len(axx.get_yticklabels())
    step = min_max_range[dimension][2] / (ticks - 1)
    mn   = min_max_range[dimension][0]
    labels = ['%4.2f' % (mn + i*step) for i in xrange(ticks)]
    axx.set_yticklabels(labels)

    # Stack the subplots 
    plt.subplots_adjust(wspace=0)

    return plt


import random
base  = [0,   0,  5,   5,  0]
scale = [1.5, 2., 1.0, 2., 2.]
data = [[base[x] + random.uniform(0., 1.)*scale[x]
        for x in xrange(5)] for y in xrange(30)]
colors = ['r'] * 30

base  = [3,   6,  0,   1,  3]
scale = [1.5, 2., 2.5, 2., 2.]
data.extend([[base[x] + random.uniform(0., 1.)*scale[x]
             for x in xrange(5)] for y in xrange(30)])
colors.extend(['b'] * 30)

parallel_coordinates(data, style=colors).show()
```

![iris](http://i.stack.imgur.com/N1mpi.png)

