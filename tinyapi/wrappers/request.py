import typing
import json
import multipart
import threading

from urllib.parse import parse_qsl

class Request(threading.local):
    
    def bind(self, environ: typing.Dict[str, typing.Any]):
        self.environ: typing.Dict[str, typing.Any] = environ
        " The environment of the request. "

        self._headers = {
            key[5:].lower():v 
            for key,v in self.environ.items() if key.startswith("HTTP_")
        }
        " The headers of the request. "
        self._form = {}
        " The form of the request. "

    @property
    def method(self) -> str:
        """
            This property returns the method of the request.
        """
        return self.environ.get("REQUEST_METHOD", None)

    @property
    def path(self) -> str:
        """
            This property returns the path of the request.
        """
        return self.environ.get("PATH_INFO", None)

    @property
    def query_string(self) -> str:
        """
            This property returns the query string of the request.
        """
        return parse_qsl(self.environ.get("QUERY_STRING", None))

    @property
    def headers(self) -> typing.Dict[str, str]:
        """
            This property returns the headers of the request.
        """
        return self._headers

    @property
    def mimie(self) -> str:
        """
            This property returns the mimie of the request.
        """
        return self.environ.get("CONTENT_TYPE")

    @property
    def content_length(self) -> int:
        """
            This property returns the content length of the request.
        """
        try:
            int(self.environ.get("CONTENT_LENGTH"))
        except (ValueError, TypeError):
            return None

    @property
    def body(self) -> str:
        """
            This property returns the body of the request.
        """
        return self.environ["wsgi.input"].read(self.content_length)

    @property
    def form(self) -> typing.Dict[str, str]:
        """
            This property returns the form of the request.
        """
        def on_file(file):
            self._form[file.name] = file.filename
        def on_field(field):
            self._form[field.field_name] = field.value

        headers = {'Content-Type': self.mimie}

        if 'HTTP_X_FILE_NAME' in self.environ:
            headers['X-File-Name'] = self.environ['HTTP_X_FILE_NAME']
        if 'CONTENT_LENGTH' in self.environ:
            headers['Content-Length'] = self.environ['CONTENT_LENGTH']

        if "multipart/form-data" in headers["Content-Type"]:
            multipart.parse_form(headers, self.environ['wsgi.input'], on_file=on_file, on_field=on_field)

        return self._form

    @property
    def json(self) -> typing.Dict[str, typing.Any]:
        """
            This property returns the json of the request.
        """
        return json.loads(self.body)

    def __repr__(self) -> str:
        return f"<Request {self.environ['PATH_INFO']} {self.environ['REQUEST_METHOD']}>"

    