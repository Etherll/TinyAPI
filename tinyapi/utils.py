import re

def format_pattern(route: str):
    """
        This method formats the route to a regex pattern.

        https://github.com/bottlepy/bottle/blob/16a131de2ed3c9b7fe6bcfcff71a85a71bfe9342/bottle.py#L377
    """
    route = route.strip().lstrip('$^/ ').rstrip('$^ ')
    route = re.sub(r':([a-zA-Z_]+)(?P<uniq>[^\w/])(?P<re>.+?)(?P=uniq)',r'(?P<\1>\g<re>)',route)
    route = re.sub(r':([a-zA-Z_]+)',r'(?P<\1>[^/]+)', route)
    return re.compile('^/%s$' % route)

def guess_mimi_type(body: str):
    """
        This method guesses the content type of the body.
        It uses the first part of the content type.
        For example, if the content type is "<!DOCTYPE html>",
        it will return "text/html".
        else
        it will return "text/plain".

        Parameters
        ----------
        body : `str`
            The body of the request.
    """
    if body is None:
        return 'text/plain'
    
    if body.startswith(("<!DOCTYPE html>", "<!doctype html>", "<html>")):
        return "text/html"
    else:
        return "text/plain"