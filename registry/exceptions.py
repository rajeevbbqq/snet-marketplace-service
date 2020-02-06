from common.exceptions import CustomException


class BadRequestException(CustomException):
    error_message = "BAD_REQUEST"

    def __init__(self):
        super().__init__({})


class OrganizationNotFoundException(CustomException):
    error_message = "ORGANIZATION_NOT_FOUND"

    def __init__(self):
        super().__init__({})


class InvalidServiceState(CustomException):
    error_message = "INVALID_SERVICE_STATE"

    def __init__(self):
        super().__init__({})


EXCEPTIONS = (BadRequestException, OrganizationNotFoundException)
