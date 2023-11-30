import time

from grpc import insecure_channel

from constants import SERVER_ROUTE
from protos.messenger_pb2 import (
    Request,
    Response,
    DelayedResponse,
)
from protos.messenger_pb2_grpc import MessengerStub


class RpcMethods:
    @staticmethod
    def simple_message(stub: MessengerStub) -> None:
        response: Response = stub.SimpleResponse(
            Request(
                message='Simple Massage'
            )
        )

        print(f'RESPONSE/ {response}')

    @staticmethod
    def response_streaming(stub: MessengerStub) -> None:
        responses: list[Response] = stub.StreamingResponse(
            Request(
                message='Response-Streaming Massage'
            )
        )

        for response in responses:
            print(f'RESPONSE/ {response}')

    @staticmethod
    def request_streaming(stub: MessengerStub) -> None:
        response: DelayedResponse = stub.RequestStreaming(
            Client.get_stream()
        )

        print(f'RESPONSE/ {response}')

    @staticmethod
    def bidirectionally_streaming(stub: MessengerStub) -> None:
        responses: list[Response] = stub.BidirectionallyStreaming(
            Client.get_stream()
        )

        for response in responses:
            print(f'RESPONSE/ {response}')


class Client:
    functions: dict = {
        1: RpcMethods.simple_message,
        2: RpcMethods.response_streaming,
        3: RpcMethods.request_streaming,
        4: RpcMethods.bidirectionally_streaming,
    }

    def __init__(self):
        with insecure_channel(SERVER_ROUTE) as channel:
            stub: MessengerStub = MessengerStub(channel)
            function: int = int(input('Function: '))

            if function in self.functions:
                self.functions.get(function)(stub)
            else:
                print('Invalid function')

    @staticmethod
    def get_stream() -> Request:
        while True:
            msg: str = input('Message (or nothing to stop): ')
            if msg == '':
                break

            request = Request(
                message=msg
            )

            yield request
            time.sleep(1)


if __name__ == '__main__':
    while True:
        Client()
