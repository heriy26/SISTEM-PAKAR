#1.	Dataset seeds ini adalah dataset klasifikasi wheat seeds (Biji gandum) berdasarkan varietasnya. Sumber : https://archive.ics.uci.edu/ml/datasets/seeds#.
#2.	Attribut seeds terdiri dari : Area, Perimeter, Compactness, Kernel.Length, Kernel.Width, Asymmetry.Coeff, Kernel.Groove, Type.
#3.	Label yang digunakan adalah “Type”, berdasarkan label tersebut dengan menggunakan model GaussianNB untuk memprediksi varietas biji gandum tersebut.
#4.	Hasil atau keluaran prediksi akan ditunjukkan sebagai berikut:
#   1 = Kama
#   2 = Rosa
#   3 = Canadian

# import pandas as pd
Memanggil library pandas

# from sklearn.model_selection import train_test_split
Memanggil modul train_test_split dari library sklearn.model_selection

# from sklearn.metrics import accuracy_score
Memanggil modul accuracy_score dari library sklearn.metrics

# from sklearn.naive_bayes import GaussianNB"
Memanggil modul GaussianNB dari library sklearn.naive_bayes

# wheat = pd.read_csv('dataset/seeds.csv', sep=',')
Dengan menggunakan metode read_csv dari pandas untuk memuat data dari file seeds.csv

# X = wheat.drop(['Type'], axis=1)
# y = wheat['Type']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
Membuat variabel X dan y dengan mengambilnya dari set data dan menggunakan fungsi train_test_split dari scikit-learn untuk membagi data menjadi set pelatihan dan pengujian.
Perhatikan bahwa ukuran pengujian 0,5 menunjukkan bahwa 50% data digunakan untuk pengujian. random_state memastikan reproduktifitas. Untuk output train_test_split, didapatkan nilai X_train, X_test, y_train, dan y_test. 

# gnb = GaussianNB()
# gnb.fit(X_train, y_train)
Dengan menggunakan X_train dan y_train, yang diperoleh di atas, untuk melatih gnb dengan pengklasifikasi GaussianNB. 
Dengan menggunakan metode fit dan meneruskan parameter.

# pred = gnb.predict(X_test)
# print("Hasil prediksi jenis biji gandum:")
# print("1. Kama")
# print("2. Rosa")
# print("3. Canadian")
# print(pred)
Setelah gnb dilatih, gnb tersebut siap untuk membuat prediksi. 
Menggunakan metode predict pada gnb dan meneruskan X_test sebagai parameter untuk mendapatkan hasil prediksi sebagai pred.

# acc = accuracy_score(y_test, pred)
# print("Hasil akurasi prediksi dari pred:")
# print(acc)
Terakhir, untuk melihat seberapa baik performa gnb pada data pengujian.
Untuk itu dengan mengevaluasi gnb dengan menemukan skor akurasi yang dihasilkan oleh gnb.