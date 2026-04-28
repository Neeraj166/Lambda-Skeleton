"""
Base service class for all services
"""
class BaseService:
    """
    Base service class for all services
    """
    customer_id = None

    def __init__(self) -> None:
        self.customer_id = BaseService.customer_id

    def setup(self, data: dict) -> None:
        """
        Setup the service with the given data
        """
        BaseService.customer_id = data['customerId']
