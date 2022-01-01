# Template/Render
### A way to display templated/renderd html to the client

```py
import tinyapi

app = tinyapi.TinyAPI()
render = tinyapi.Renderer('./templates')

@app.rule('/', methods=['GET'])
def index():
    return render.render_template('/index.html', name='World')

if __name__ == "__main__":
    app.run()
```