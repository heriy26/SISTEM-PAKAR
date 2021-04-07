import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

wheat = pd.read_csv('dataset/seeds.csv', sep=',')

X = wheat.drop(['Type'], axis=1)
y = wheat['Type']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

gnb = GaussianNB()
gnb.fit(X_train, y_train)

pred = gnb.predict(X_test)
print("Hasil prediksi jenis biji gandum:")
print("1. Kama")
print("2. Rosa")
print("3. Canadian")
print(pred)

acc = accuracy_score(y_test, pred)
print("Hasil akurasi prediksi dari gnb:")
print(acc)