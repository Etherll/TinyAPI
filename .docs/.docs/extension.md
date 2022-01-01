# Extension

### Extensions is a way to split the application into multiple parts.

ext.py
```py
import tinyapi

ext = tinyapi.Extension('ext')

@ext.rule('/hello/:name', methods=['GET'])
def hello(name: str):
    return f'Hello {name}'
```
app.py
```py
import tinyapi

app = tinyapi.TinyAPI()

if __name__ == "__main__":
    from ext import ext
    app.add_extension(ext)
    app.run()
```