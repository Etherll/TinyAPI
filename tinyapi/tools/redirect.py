import typing

from tinyapi.wrappers import Respone
from tinyapi.http import STATUS_MESSAGE

def redirect(url: str) -> typing.Callable:
    """
        This function returns a decorator that redirects the request to the given url.
    """
    html = f"""
        <!DOCTYPE html>
        <html>
            <p>Redirecting...</p>
            <p><a href="{url}">Click here if you are not redirected</a></p>
        </html>
    """
    resp =  Respone(html,f'301 {STATUS_MESSAGE[301]}','text/html')
    resp.add_header('Location',str(url))
    return resp