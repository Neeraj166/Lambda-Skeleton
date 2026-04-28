# test service

from services.base_service import BaseService

class TestService(BaseService):
    def __init__(self):
        super().__init__()

    def test(self):
        print(self.customer_id)
        return "test"
