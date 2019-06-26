import numpy as np
X = bbc['article']
Y = np.array(bbc['category'])





from sklearn import preprocessing
le = preprocessing.LabelEncoder()
Y = le.fit_transform(Y)



from nltk.corpus import stopwords 
sw = set(stopwords.words('english'))

from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer(stop_words = sw, min_df = 2)
X = vect.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size = 0.75)



print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)