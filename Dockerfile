FROM python:3.7
RUN pip install requests schedule
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["docker-main.py"]