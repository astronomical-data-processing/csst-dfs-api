
class CSSTGenericException(Exception):
    def __init__(self, *args: object) -> None:
        super(CSSTGenericException, self).__init__(*args)

class CSSTFatalException(Exception):
    def __init__(self, *args: object) -> None:
        super(CSSTFatalException, self).__init__(*args)        