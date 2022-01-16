import typing

from mako.template import Template

class Renderer:
    """
        This is class that responsible for rendering templates.
        It uses Mako library to render templates.
    """
    def __init__(self, dir: str, *args, **kwargs) -> None:
        self.dir = dir
        " The directory of the templates. "
        self._args = args
        " The arguments of the template. "
        self._kwargs = kwargs
        " The keyword arguments of the template. "

    def _read_file(self, file_name:str) -> str:
        """
            This method reads a file.
            Get the file from the work dir and read it.

            Parameters
            ----------
            file_name : `str`
                The name of the file.
        """
        return open(f'{self.dir}{file_name}' , "r").read()

    def render_template(self, file_name: typing.IO, *args, **kwargs) -> str:
        """
            This method renders a template.
            It uses Mako library to render templates.

            Parameters
            ----------
            file_name : `str`
                The name of the template.
        """
        text = self._read_file(file_name)
        template = Template(text=text, *self._args, **self._kwargs)

        return template.render(*args, **kwargs)