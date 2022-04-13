""" Library Exceptions """

class FindMyPyException(Exception):
    """Generic find_my exception."""
    pass

class FindMyPyApiException(FindMyPyException):
    def __init__(self, httpcode) -> None:
        super().__init__(httpcode)

class FindMyPyJsonException(FindMyPyException):
    def __init__(self, reason) -> None:
        super().__init__(reason)

class FindMyPyNoDevicesException(FindMyPyException):
    pass

class FindMyPyLoginExcepetion(FindMyPyException):
    pass