import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from pandas import read_csv
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, neighbors
from mlxtend.plotting import plot_decision_regions


names=['Hr','Stress','Temp']
dataset = read_csv("all BK1 - Copy.csv")
#dataset1 = read_csv("merged AD1.csv")
print(dataset.shape)
print(dataset.describe())


df = pd.read_csv("all BK1 - Copy.csv")
df_model = df.copy()

#Rescaling features
#scaler = StandardScaler()
scaler = MinMaxScaler()
#scaler = RobustScaler()

features = [['Temp', 'Hr', 'Road']]
for feature in features:
    df_model[feature] = scaler.fit_transform(df_model[feature])
#Create KNN Object
knn = KNeighborsClassifier()

x = df_model.drop(columns=['Scale'])
y = df_model['Scale']
#Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
#Training the model
knn.fit(x_train, y_train)
#Predict testing set
y_pred = knn.predict(x_test)
#Check performance using accuracy
print("Accuracy Score: ",accuracy_score(y_test, y_pred))

print(classification_report(y_test, y_pred))

results = confusion_matrix(y_test, y_pred)
print("Confusion matrix", results)
predicted= knn.predict([[31.75,85.35,2]])
print(predicted)

dataset_numpy = np.array(dataset)
x_con = np.array(x)
y_con = np.array(y)
def knn_comparison(data, k):

 clf = neighbors.KNeighborsClassifier(n_neighbors=k)
 clf.fit(x_con, y_con)
# Plotting decision region
 plot_decision_regions(x_con, y_con, clf=clf, legend=3)
# Adding axes annotations
 plt.xlabel("Train")
 plt.ylabel("Test")
 #plt.title(‘Knn with K=’+ str(k))
 plt.show()


error = []
# Calculating error for K values between 1 and 40
for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train, y_train)
    pred_i = knn.predict(x_test)
    error.append(np.mean(pred_i != y_test))


plt.figure(figsize=(12, 6))
plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')

plt.show()