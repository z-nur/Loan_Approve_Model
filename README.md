# Loan_Approve_Model
Koc Finans Exam

# Loan Approval Prediction API

Bu proje, müşteri başvurularına göre kredi onayı tahmin eden bir makine öğrenmesi modelini içerir. Flask tabanlı bir API ile sunulan model, istenilen şekilde Docker ile paketlenmiştir. 

## Proje Özeti

Bu model, belirli müşteri özelliklerine göre kredi onayını tahmin etmek için LogisticRegression, SVM, XGBoost ve RF algoritmaları kullanılmış, şampiyon model **RandomForestClassifier** algoritması kullanılmıştır. Flask API üzerinden RESTful bir servis sunulmuştur ve Docker kullanılarak  dağıtım sağlanmıştır.

## Kullanılan Teknolojiler

- Python (pandas, numpy, matplotlib.pyplot, seaborn, joblib, sklearn paketleri kullanılmıştır)
- Flask (API oluşturma)
- Docker (konteynerleştirme)
- Git (versiyon kontrol)
- GitHub (proje aktarımı)

## Gereksinimler

'requirements.txt' dosyası tüm bağımlılıkları içermektedir ve aşağıdaki komutla yüklenebilir:

bash
pip install -r requirements.txt

