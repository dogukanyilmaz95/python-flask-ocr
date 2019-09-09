FROM python:3

WORKDIR /usr/src/app


# We copy just the requirements.txt first to leverage Docker cache
COPY /app.py

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#ENTRYPOINT [ "python" ]

CMD ["python", "/usr/src/app/python-flask-ocr/Main.py" ]
#CMD ["/bin/bash"]