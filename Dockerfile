FROM python:3.9

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép tệp yêu cầu và cài đặt dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Mở cổng 8000
EXPOSE 8000

# Chạy ứng dụng FastAPI với Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]