# 🚀 Flask Model Server

머신러닝 모델을 REST API로 제공하는 Flask 서버입니다.

## 📋 프로젝트 개요

이 서버는 학습된 머신러닝 모델(`test_model.pkl`)을 로드하여 HTTP 요청을 통해 예측 서비스를 제공합니다.

## 🛠️ 기술 스택

- **Python**: 3.7+
- **Flask**: 웹 프레임워크
- **Joblib**: 모델 직렬화/역직렬화
- **NumPy**: 수치 계산

## 📦 설치 방법

### 1. 저장소 클론
```bash
git clone <repository-url>
cd flask-model-server
```

### 2. 가상환경 생성 및 활성화
```bash
# 가상환경 생성
python -m venv .venv

# 가상환경 활성화
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

또는 개별 설치:
```bash
pip install flask joblib numpy
```

## 🚀 실행 방법

```bash
python app.py
```

서버가 실행되면 `http://localhost:5050`에서 접근할 수 있습니다.

## 📡 API 사용법

### 예측 API

**엔드포인트**: `POST /predict`

**요청 예시**:
```json
{
    "hour": 14,
    "day_of_week": 2,
    "is_weekend": 0,
    "holiday_kr": 0,
    "temperature": 25.5,
    "rainfall": 0.0,
    "wind_speed": 3.2,
    "humidity": 65,
    "comfort_score": 7.5,
    "is_peak_hour": 1,
    "is_rain": 0,
    "start_lat": 37.5665,
    "start_lon": 126.9780,
    "time_of_day_category_encoded": 2,
    "station_id_encoded": 15
}
```

**응답 예시**:
```json
{
    "predicted_demand": 45.2
}
```

## 📁 프로젝트 구조

```
flask-model-server/
├── app.py              # 메인 Flask 애플리케이션
├── test_model.pkl      # 학습된 머신러닝 모델
├── requirements.txt    # Python 의존성 목록
└── README.md          # 프로젝트 문서
```

## ⚠️ 주의사항

- `test_model.pkl` 파일이 `app.py`와 같은 디렉토리에 있어야 합니다
- 필요한 Python 패키지들이 설치되어 있어야 합니다
- 서버를 중지하려면 터미널에서 `Ctrl+C`를 누르세요

## 🔧 문제 해결

### ModuleNotFoundError 발생 시
```bash
pip install flask joblib numpy
```

### 포트가 이미 사용 중인 경우
`app.py`에서 포트 번호를 변경하세요:
```python
app.run(host='0.0.0.0', port=5051)  # 5050 → 5051
```

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 🤝 기여하기

버그 리포트나 기능 제안은 이슈를 통해 제출해주세요.
