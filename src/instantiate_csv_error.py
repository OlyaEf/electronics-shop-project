
class InstantiateCSVError(Exception):
    def __init__(self, *args) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return str(self.message)


class FileNotFoundError(InstantiateCSVError):
    def __init__(self, message):
        self.message = message


