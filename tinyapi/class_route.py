import typing


class ClassRoute:
    def __init__(self, path: str) -> None:
        self.path = path
        """ The path string. """

        self.methods: typing.List[str] = []
        """ The methods of the rule. """

        for attr in dir(self):
            if attr.startswith("on_"):
                if attr[3:] in [
                        "post",
                        "get",
                        "put",
                        "delete",
                        "head",
                        "options",
                        "patch",
                ]:
                    self.methods.append(getattr(self, attr))
        """ The methods of the rule. """

    def __repr__(self) -> str:
        return f"<Rule {self.path}>"
