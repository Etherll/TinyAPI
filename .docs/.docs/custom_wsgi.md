# Custom WSGI

```py
import tinyapi

app = tinyapi.TinyAPI()

@app.rule('/', methods=['GET'])
def index():
    return 'Hello World!'

if __name__ == "__main__":
    WSGIServer(('', 8000), app).serve_forever()
```