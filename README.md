## Getting Started

### Before Running Application

Kindly ensure you have the following installed on your machine:

-  [Python 3](https://www.python.org/downloads/)
-  [Tesseract](https://github.com/tesseract-ocr/tesseract/wiki#installation)

### Running the Application

1. Clone the repository
```
$ git clone https://github.com/dogukanyilmaz95/python-flask-ocr.git
```

2. Check into the cloned repository
```
$ cd python-flask-ocr
```

3. Install the requirements
```
$ pip install -r requirements.txt
```

4. Run
```
python app.py
```

5.Test
```diff-red
curl -k -X POST -F 'file=@YOUR IMAGE PATH' -v  http://127.0.0.1:5000/ocr
```


