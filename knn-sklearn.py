from sklearn.neighbors import KNeighborsClassifier


KNN = KNeighborsClassifier(n_neighbors = 3)
KNN.fit(X_train, Y_train)
Y_pred = KNN.predict(X_test)