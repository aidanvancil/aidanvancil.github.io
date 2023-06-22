import numpy as np
from scipy import stats
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Generating random data
np.random.seed(0)
x = np.random.rand(100)
y = np.random.randint(0, 2, 100)

# Basic statistical operations with SciPy
mean = np.mean(x)
median = np.median(x)
mode = stats.mode(y)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode.mode[0])

# Loading and splitting the Iris dataset with scikit-learn
iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=0
)

# Creating a logistic regression model with scikit-learn
model = LogisticRegression()
model.fit(x_train, y_train)

# Making predictions and evaluating the model
predictions = model.predict(x_test)
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
