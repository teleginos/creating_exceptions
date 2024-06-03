class InvalidDataException(Exception):
    def __init__(self, message, *extra_info):
        self.message = message
        self.extra_info = extra_info


class ProcessingException(Exception):
    def __init__(self, message, *extra_info):
        self.message = message
        self.extra_info = extra_info
