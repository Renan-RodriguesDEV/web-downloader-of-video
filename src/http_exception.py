class HttpException(Exception):
    def __init__(self, message: str, status_code: int, *errors):
        super().__init__(*errors)
        self.message = message
        self.status_code = status_code
