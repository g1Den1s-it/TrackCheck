from fastapi.exceptions import HTTPException


class HTTPDatabaseError(HTTPException):
    def __init__(self):
        super().__init__(detail="Database cannot execute your query. Try again later.",
                         status_code=500)


class HTTPClientException(HTTPException):
    def __init__(self, message: str):
        super().__init__(detail=message, status_code=404)


class HTTPClientInputException(HTTPException):
    def __init__(self, message: str):
        super().__init__(detail=message, status_code=400)

