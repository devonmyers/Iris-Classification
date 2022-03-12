from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# Magic command to get inline plots
#matplotlib inline

# load data with load_iris  from sklearn
data = load_iris()  # returns object with several fields below
features = data.data    # Numeric data
feature_names = data.feature_names
target = data.target
target_names = data.target_names

# use numpy indexing to get an array of strings
labels = target_names[target]

# plot all 2D projections of the features
fig,axes = plt.subplots(2, 3)
pairs = [(0,1), (0,2), (0,3), (1, 2), (1, 3), (2,3)]

# Set up 3 different pairs of (color, marker)
color_markers = [
    ('r', '>'),
    ('g', 'o'),
    ('b', 'x'),
    ]

for i, (p0, p1) in enumerate(pairs):
    ax = axes.flat[i]

    for t in range(3):
        # Use a different color/marker for each class 't'
        c,marker = color_markers[t]
        ax.scatter(features[target == t, p0],
                   features[target == t, p1],
                   marker=marker, c=c)
    ax.set_xlabel(feature_names[p0])
    ax.set_ylabel(feature_names[p1])
    ax.set_xticks([])
    ax.set_yticks([])
fig.tight_layout()
#plt.show()

plength = features[:, 2] # Petal length
is_setosa = (labels == 'setosa')

"""print(plength[is_setosa])
print()
print(plength[~is_setosa])"""

max_setosa = plength[is_setosa].max() # maximum petal length of a setosa is 1.9
min_non_setosa = plength[~is_setosa].min() # minimum petal length of a non_setosa is 3.0
print(f'Maximum petal length of a setosa is {max_setosa}')
print(f'Minimum petal length of a non-setosa is {min_non_setosa}')

# Simple model: if petal length is < 2, then flower is a setosa.  Otherwise,
# it is either virginica or versiocolor

#for i in range(len(features)):
    #if features[:, 2][i] < 2: print("Iris Setosa")
    #else: print("Iris Virginica or Iris Versicolor")

"""

# Now, select only non-Setosa features and labels
features = features[~is_setosa]
labels = labels[~is_setosa]
is_virginica = (labels == 'virginica')

best_acc = -1.0
for fi in range(features.shape[1]):
    # Generate all possible thresholds for this feature
    thresh = features[:, fi].copy()
    thresh.sort()
    # Now test all thresholds:
    for t in thresh:
        pred = (features[:,fi] > t)
        acc = (pred == is_virginica).mean()
        if acc > best_acc:
            best_acc, best_fi, best_t = acc, fi, t

error = 0.0
#Leave one out cross validation
for ei in range(len(features)):
    training = np.ones(len(features), bool)
    training[ei] = False
    testing = ~training
    model = learn_model(features[training], is_virgini[training])
    predictions = apply_model(features[testing],
                              is_virginica[testing],
                              model)
    error += np.sum(predictions != is_virginica[testing])"""


