import tinyapi

app = tinyapi.TinyAPI()


@app.rule("/hello/:name")
def hello(name: str):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run()
