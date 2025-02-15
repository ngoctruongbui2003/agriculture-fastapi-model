from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel
from tensorflow.keras.models import load_model  # Thêm thư viện này

app = FastAPI()

# Load mô hình RandomForestRegressor (đã dùng pickle)
with open("model/watering_time_predictor.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/scaler_watering_time_predictor.pkl", "rb") as f:
    scaler = pickle.load(f)

# Load mô hình Keras (sửa lại cách load)
model1 = load_model("model/predict_health_model.keras")  # Sửa cách load

with open("model/scaler_predict_health_model.pkl", "rb") as f:
    scaler1 = pickle.load(f)


class IrrigationInput(BaseModel):
    humidity: float
    temperature: float
    light: float
    soilMoisture: float
    rainVolume: float
    gasVolume: float


@app.post("/predict/watering_time")
def predict_watering_time(data: IrrigationInput):
    new_data = pd.DataFrame([data.dict()])
    new_data_scaled = scaler.transform(new_data)
    prediction = model.predict(new_data_scaled)

    return prediction[0]


@app.post("/predict/health_model")
def predict_health_model(data: IrrigationInput):
    new_data = pd.DataFrame([data.dict()])

    # Không sử dụng scaler nữa
    prediction = model1.predict(new_data)

    return float(prediction[0][0])  # Chuyển đổi kết quả về số thực


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
