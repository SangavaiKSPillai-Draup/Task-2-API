class MobileNotFoundError(Exception):
    """
        Exception raised if a mobile is not found in database.
    """
    def __init__(self, msg):
        self.msg = msg


class CustomerNotFoundError(Exception):
    """
        Exception raised if a customer is not found in database.
    """
    def __init__(self, msg):
        self.msg = msg
