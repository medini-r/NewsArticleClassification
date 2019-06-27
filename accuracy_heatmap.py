from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
c_mat = confusion_matrix(Y_test,Y_pred)
print(c_mat)

accuracy = accuracy_score(Y_test,Y_pred) * 100 
print(accuracy, "%")

import seaborn as sns
hmap = sns.heatmap(c_mat, annot = True, fmt = 'd', cmap="YlGnBu")