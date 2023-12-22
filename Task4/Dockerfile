FROM python:3.10.12-slim

COPY requirements.txt requirements.txt

RUN apt-get update &&\
    apt-get install inotify-tools watchdog -y &&\
    pip install --no-cache-dir -r requirements.txt
    
COPY main.py main.py

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]