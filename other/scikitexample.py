from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# loads data
iris = load_iris()

# spliting the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

# creating a nearest neighbor classifier
knn = KNeighborsClassifier(n_neighbors=1)

# training model on the training set
knn.fit(X_train, y_train)

# estimation of model accuracy on a test set
print("Accuracy on the test set: {:.2f}".format(knn.score(X_test, y_test)))
