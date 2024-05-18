from flask import Flask, request, jsonify
import pandas as pd
import joblib

model = joblib.load("req_avail_simple_model.joblib")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    state_ut = str(data['State/Union Territory'])
    end_yr = float(data['End_Year'])
    pop = float(data['population(crores)']) * 10  # 1 crore = 10 million

    st_en = {'Andaman and Nicobar Islands': 0, 'Andhra Pradesh': 1, 'Arunachal Pradesh': 2, 'Assam': 3, 'Bihar': 4,
             'Chandigarh': 5, 'Chhattisgarh': 6, 'Dadra and Nagar Haveli': 7, 'Daman and Diu': 8, 'Delhi': 9, 'Goa': 10,
             'Gujarat': 11, 'Haryana': 12, 'Himachal Pradesh': 13, 'Jammu and Kashmir': 14, 'Jharkhand': 15, 'Karnataka': 16,
             'Kerala': 17, 'Lakshadweep': 18, 'Madhya Pradesh': 19, 'Maharashtra': 20, 'Manipur': 21, 'Meghalaya': 22,
             'Mizoram': 23, 'Nagaland': 24, 'Odisha': 25, 'Puducherry': 26, 'Punjab': 27, 'Rajasthan': 28, 'Sikkim': 29,
             'Tamil Nadu': 30, 'Telangana': 31, 'Tripura': 32, 'Uttar Pradesh': 33, 'Uttarakhand': 34, 'West Bengal': 35}

    new_data = pd.DataFrame({
        'State/Union Territory': [st_en[state_ut]],
        'End_Year': [end_yr],
        'population(million)': [pop]
    })

    prediction = model.predict(new_data)[0]
    req_crore_kWh = prediction[0]
    avail_crore_kWh = prediction[1]

    return jsonify({'req_crore_kWh': req_crore_kWh, 'avail_crore_kWh': avail_crore_kWh})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)