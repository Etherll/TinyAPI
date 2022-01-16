<div align="center">
<h1>TinyAPI</h1>
<p>A fast and lightweight WSGI Framework for Python.</p>
</div>

# Quick Example
```py
import tinyapi

app = tinyapi.TinyAPI()

@app.rule('/', methods=['GET'])
def index():
    return 'Hello World!'

@app.error(404)
def not_found():
    return 'Not found f'

if __name__ == "__main__":
    app.run()
```

## Todo

<div align="left">

- [ ] Add Session Support
- [x] Add Docs to the box
- [ ] Exception 
- [ ] Datastructures
- [ ] Testing thing
