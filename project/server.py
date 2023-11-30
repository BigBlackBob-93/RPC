import time
from concurrent import futures

import grpc

from constants import SERVER_ROUTE
from protos.messenger_pb2 import (
    Request,
    Response,
    DelayedResponse,
)
from protos.messenger_pb2_grpc import (
    MessengerServicer,
    add_MessengerServicer_to_server,
)


class Messenger(MessengerServicer):
    def SimpleResponse(self, request: Request, context) -> Response:
        print(f'SimpleResponse/ {request}')
        response: Response = Response(
            message=request.message
        )

        return response

    def StreamingResponse(self, request: Request, context) -> Response:
        print(f'StreamingResponse/ {request}')

        for i in range(3):
            response: Response = Response(
                message=request.message
            )

            yield response
            time.sleep(1)

    def RequestStreaming(self, requests: list[Request], context) -> DelayedResponse:
        response: DelayedResponse = DelayedResponse()
        for request in requests:
            print(f'RequestStreaming/ {request}')
            response.request.append(request)
        response.message = f'Send {len(response.request)} messages'

        return response

    def BidirectionallyStreaming(self, requests: list[Request], context) -> Response:
        for request in requests:
            print(f'BidirectionallyStreaming/ {request}')
            response: Response = Response(
                message=request.message
            )

            yield response


class Server:
    def __init__(self):
        server = grpc.server(
            thread_pool=futures.ThreadPoolExecutor(max_workers=10),
        )
        add_MessengerServicer_to_server(
            servicer=Messenger(),
            server=server,
        )
        server.add_insecure_port(
            address=SERVER_ROUTE,
        )
        server.start()
        server.wait_for_termination()


if __name__ == '__main__':
    Server()
