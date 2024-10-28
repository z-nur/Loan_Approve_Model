#Egitilen model ile tahmin yapacak Flask api.
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Flask uygulamasını başlatma
app = Flask(__name__)

# Modeli yükleme
model = joblib.load("final_model.joblib")

# Ana sayfa endpoint'i
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Loan Approval Prediction API!"

# Tahmin yapacak endpoint

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # JSON verisini al ve pandas DataFrame'e çevir
        data = request.get_json()
        features = pd.DataFrame([data['features']], columns=X.columns)  
        prediction = model.predict(features)
        result = 'Approved' if prediction[0] == 1 else 'Rejected'

        # Sonucu JSON formatında döndür
        return jsonify({'loan_status': result})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

