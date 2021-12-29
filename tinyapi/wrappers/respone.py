import typing

class Respone:
    def __init__(self, body: str, status_code='200 OK', content_type: str='text/plain') -> None:
        self.body: str = body
        self.status_code: str = status_code
        self.content_type: str = content_type
        self.headers: typing.Dict[str,str] = {}
        self.cookies: typing.Dict[str,str] = {}

    def add_header(self, key: str, value: str) -> None:
        """
            This method adds a header to the respone.
        """
        self.headers[key] = value

    def remove_header(self, key: str) -> None:
        """
            This method removes a header from the respone.
        """
        del self.headers[key]
    
    def add_cookie(self, key: str, value: str) -> None:
        """
            This method adds a cookie to the respone.
        """
        self.cookies[key] = value

    def remove_cookie(self, key: str) -> None:
        """
            This method removes a cookie from the respone.
        """
        del self.cookies[key]

    def __form_header(self):
        """
            This method returns the headers of the respone.
        """
        if self.cookies != {}:
            self.headers["Set-Cookie"] = [
                f"{key}={value}"
                for key,value in self.cookies.items()
            ]
        return [(k,v) for k,v in self.headers.items()]

    def __repr__(self) -> str:
        return f"<Respone: {self.status_code} {self.content_type} {self.body}>"

    def __str__(self) -> str:
        return str(self.body)