# Base Routering

### Router are the path from the request and can be use to register a callback for a rule/path

```py
import tinyapi

app = tinyapi.TinyAPI()

@app.rule('/', methods=['GET'])
def index():
    return 'Hello World!'

@app.error(404)
def not_found():
    return 'Not found'

if __name__ == "__main__":
    app.run()
```