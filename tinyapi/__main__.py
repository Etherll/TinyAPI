import snowflake

import typing
import importlib

app = snowflake.Snowflake('TinyAPI', 'TinyAPI is a tiny web framework for build RESTful APIs.')

@app.command('start')
@snowflake.option('--host', validator= lambda x : str(x))
@snowflake.option('--port', validator= lambda x : int(x))
@snowflake.option('--app', validator= lambda x : str(x))
def start(host: str='', port: int=5000, app: typing.Union[None, "str"]=None) -> None:
    print(f"* Running on http://{host}:{port}")

app()