# Pull image Python 3.12.9 tu Amazon ECR
FROM public.ecr.aws/docker/library/python:3.12.9-slim

# Update apt
RUN apt-get update && apt-get -y upgrade

# Tao thu muc lam viec trong container
WORKDIR /app

# Copy file requirements.txt vao thu muc lam viec (neu requirements khong thay doi thi khong pip install)
COPY ./requirements.txt /app/requirements.txt

# Chay cac cau lenh build
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install fastapi-cli

# Copy toan bo source vao thu muc lam viec
COPY . .

# Chay source
CMD ["fastapi", "run", "main.py", "--port", "80"]

EXPOSE 80