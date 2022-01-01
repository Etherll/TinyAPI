# Basic

to create an app you need to import the `TinyAPI`

```py
import tinyapi
```

and then create app using the `TinyAPI` class

```py
import tinyapi

app = tinyapi.TinyAPI()
```

to run the app you need to use the `.run` method
```py
import tinyapi

app = tinyapi.TinyAPI()

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
```