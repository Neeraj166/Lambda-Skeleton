'''
Lambda function to allot raffle winners
'''
import json
import traceback as tb
from db.connection import Connection
from services import BaseService

class LambdaHandler:
    """
    Lambda handler for allotting raffle winners
    """
    def __init__(self):
        self.cnx = None
        self.wcnx = None

    def initialize_services(self, data):
        """
        Initialize database connections and base service
        """
        self.cnx, self.wcnx = Connection().get_connection()
        BaseService().setup(data)

    def parse_event(self, event):
        """
        Parse the event and extract the body
        """
        # For SNS events
        body = event.get('Records', [{}])[0].get('Sns', {}).get('Message', '{}')
        
        # For SQS events
        # body = event.get('Records', [{}])[0].get('body', '{}')
        
        return json.loads(body)

    def close_connections(self):
        """
        Close database connections
        """
        for conn in [self.cnx, self.wcnx]:
            if conn:
                try:
                    conn.close()
                except Exception:
                    tb.print_exc()


    def handle(self, event, context):
        """
        Handle the lambda event
        """
        try:
            data = self.parse_event(event)
            self.initialize_services(data)

            # TODO: Add your business logic here
            # INFO: Make a service call here
            from services.test_service import TestService
            TestService().test()

            message = "Process completed"

        except Exception:
            tb.print_exc()
            message = "Error processing request"

        finally:
            self.close_connections()

        print(f"Request processed: {message}")

        return {
            "status": "success",
            "message": message
        }


def lambda_handler(event, context):
    """
    Lambda handler function
    """
    return LambdaHandler().handle(event, context)

if __name__ == "__main__":
    test_data = {
        "someKey": "someValue",
    }

    test_event = {
            'Records': [{
                'Sns': {
                    'Message': json.dumps(test_data),
                }
            }]
        }

    # For SQS events
    # test_event = {
    #     'Records': [{
    #         'body': json.dumps(test_data),
    #     }]
    # }

    lambda_handler(test_event, 0)
