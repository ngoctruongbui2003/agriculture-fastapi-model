# Dự Án Phân Tích và Dự Đoán Dữ Liệu Nông Nghiệp

Dự án này tập trung vào việc phân tích và dự đoán các chỉ số liên quan đến nông nghiệp thông qua dữ liệu cảm biến. Các mô hình học máy được sử dụng để dự đoán sức khỏe cây trồng và thời gian tưới nước tối ưu.

## Cấu Trúc Thư Mục
* pycache/ # Thư mục cache của Python

* github/ # Các tài nguyên liên quan đến GitHub

* assets/ # Tài nguyên hình ảnh, biểu đồ, v.v.

* dataset/ # Thư mục chứa các tập dữ liệu

* * agriculture_sensors_minute_based.csv # Dữ liệu cảm biến nông nghiệp theo phút

* * data.csv # Tập dữ liệu chính

* ipynb/ # Thư mục chứa các notebook Jupyter

* * PredictHealthModel.ipynb # Notebook cho mô hình dự đoán sức khỏe cây trồng

* * Watering_Predict_model.ipynb # Notebook cho mô hình dự đoán thời gian tưới nước

* pdf/ # Thư mục chứa các báo cáo PDF

* * PredictHealthModel.pdf # Báo cáo về mô hình dự đoán sức khỏe cây trồng

* * Watering_Predict_model.pdf # Báo cáo về mô hình dự đoán thời gian tưới nước

* model/ # Thư mục chứa các mô hình đã huấn luyện

* app.py # File ứng dụng chính

* Dockerfile # File cấu hình Docker

* README.md # Tài liệu dự án

* requirements.txt # Danh sách các phụ thuộc Python

## Cài Đặt

Để chạy dự án này, bạn cần cài đặt các phụ thuộc cần thiết. Sử dụng lệnh sau để cài đặt:

```bash
pip install uvicorn flask-asgi
pip install -r requirements.txt
uvicorn app:asgi_app --host 0.0.0.0 --port 8000 --reload
```