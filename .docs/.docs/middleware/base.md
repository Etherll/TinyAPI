# Middlewares

### Middlewares are sepical function run before the callback

```py
import tinyapi

def middleware():
    print(tinyapi.request.path)

app = tinyapi.TinyAPI(middleware=[middleware])

@app.rule('/', methods=['GET'])
def index():
    return 'Hello World!'

if __name__ == "__main__":
    app.run()
```