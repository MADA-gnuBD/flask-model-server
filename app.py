from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# 🔹 모델 로드 (경로는 상황에 맞게 수정)
model = joblib.load('test_model.pkl')

# 🔹 예측용 API
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("🟡 받은 features:", data)

        features = [
            data['hour'],
            data['day_of_week'],
            data['is_weekend'],
            data['holiday_kr'],
            data['temperature'],
            data['rainfall'],
            data['wind_speed'],
            data['humidity'],
            data['comfort_score'],
            data['is_peak_hour'],
            data['is_rain'],
            data['start_lat'],
            data['start_lon'],
            data['time_of_day_category_encoded'],
            data['station_id_encoded']
        ]

        print("🧪 모델 입력 features:", features)

        prediction = model.predict([features])[0]
        return jsonify({'predicted_demand': float(prediction)})

    except Exception as e:
        import traceback
        print("🔥 예측 오류 발생:")
        traceback.print_exc()  # 전체 에러 스택 출력
        return jsonify({'error': str(e)}), 500


# 🔹 서버 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
