# Error Routering

### Error are just the status code for the request when you return the respone with code other than 200 a callback can be happend

```py
import tinyapi

app = tinyapi.TinyAPI()

@app.error(404)
def not_found():
    return 'Not found'

if __name__ == "__main__":
    app.run()
```