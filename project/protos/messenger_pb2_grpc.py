# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import messenger_pb2 as messenger__pb2


class MessengerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SimpleResponse = channel.unary_unary(
                '/messenger.Messenger/SimpleResponse',
                request_serializer=messenger__pb2.Request.SerializeToString,
                response_deserializer=messenger__pb2.Response.FromString,
                )
        self.StreamingResponse = channel.unary_stream(
                '/messenger.Messenger/StreamingResponse',
                request_serializer=messenger__pb2.Request.SerializeToString,
                response_deserializer=messenger__pb2.Response.FromString,
                )
        self.RequestStreaming = channel.stream_unary(
                '/messenger.Messenger/RequestStreaming',
                request_serializer=messenger__pb2.Request.SerializeToString,
                response_deserializer=messenger__pb2.DelayedResponse.FromString,
                )
        self.BidirectionallyStreaming = channel.stream_stream(
                '/messenger.Messenger/BidirectionallyStreaming',
                request_serializer=messenger__pb2.Request.SerializeToString,
                response_deserializer=messenger__pb2.Response.FromString,
                )


class MessengerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SimpleResponse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingResponse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestStreaming(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BidirectionallyStreaming(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessengerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SimpleResponse': grpc.unary_unary_rpc_method_handler(
                    servicer.SimpleResponse,
                    request_deserializer=messenger__pb2.Request.FromString,
                    response_serializer=messenger__pb2.Response.SerializeToString,
            ),
            'StreamingResponse': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamingResponse,
                    request_deserializer=messenger__pb2.Request.FromString,
                    response_serializer=messenger__pb2.Response.SerializeToString,
            ),
            'RequestStreaming': grpc.stream_unary_rpc_method_handler(
                    servicer.RequestStreaming,
                    request_deserializer=messenger__pb2.Request.FromString,
                    response_serializer=messenger__pb2.DelayedResponse.SerializeToString,
            ),
            'BidirectionallyStreaming': grpc.stream_stream_rpc_method_handler(
                    servicer.BidirectionallyStreaming,
                    request_deserializer=messenger__pb2.Request.FromString,
                    response_serializer=messenger__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'messenger.Messenger', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Messenger(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SimpleResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/messenger.Messenger/SimpleResponse',
            messenger__pb2.Request.SerializeToString,
            messenger__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamingResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/messenger.Messenger/StreamingResponse',
            messenger__pb2.Request.SerializeToString,
            messenger__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RequestStreaming(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/messenger.Messenger/RequestStreaming',
            messenger__pb2.Request.SerializeToString,
            messenger__pb2.DelayedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BidirectionallyStreaming(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/messenger.Messenger/BidirectionallyStreaming',
            messenger__pb2.Request.SerializeToString,
            messenger__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)