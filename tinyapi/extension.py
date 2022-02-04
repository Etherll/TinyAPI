from tinyapi.application import Base


class Extension(Base):
    """
    Extensions is a way to split the application into multiple parts.
    By making the same method / route available in multiple extensions,
    """

    def __init__(self, name: str) -> None:
        self.name = name
        " The name of the extension. "

        Base.__init__(self)
