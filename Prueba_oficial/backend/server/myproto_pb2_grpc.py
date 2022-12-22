# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import myproto_pb2 as myproto__pb2


class DataStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetWeatherData = channel.unary_unary(
                '/mypackage.Data/GetWeatherData',
                request_serializer=myproto__pb2.Empty.SerializeToString,
                response_deserializer=myproto__pb2.WeatherResponse.FromString,
                )
        self.GetCoinsData = channel.unary_unary(
                '/mypackage.Data/GetCoinsData',
                request_serializer=myproto__pb2.Empty.SerializeToString,
                response_deserializer=myproto__pb2.CoinsResponse.FromString,
                )
        self.GetUfData = channel.unary_unary(
                '/mypackage.Data/GetUfData',
                request_serializer=myproto__pb2.Empty.SerializeToString,
                response_deserializer=myproto__pb2.UfResponse.FromString,
                )


class DataServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetWeatherData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCoinsData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUfData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetWeatherData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWeatherData,
                    request_deserializer=myproto__pb2.Empty.FromString,
                    response_serializer=myproto__pb2.WeatherResponse.SerializeToString,
            ),
            'GetCoinsData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCoinsData,
                    request_deserializer=myproto__pb2.Empty.FromString,
                    response_serializer=myproto__pb2.CoinsResponse.SerializeToString,
            ),
            'GetUfData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUfData,
                    request_deserializer=myproto__pb2.Empty.FromString,
                    response_serializer=myproto__pb2.UfResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mypackage.Data', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Data(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetWeatherData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mypackage.Data/GetWeatherData',
            myproto__pb2.Empty.SerializeToString,
            myproto__pb2.WeatherResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCoinsData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mypackage.Data/GetCoinsData',
            myproto__pb2.Empty.SerializeToString,
            myproto__pb2.CoinsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUfData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mypackage.Data/GetUfData',
            myproto__pb2.Empty.SerializeToString,
            myproto__pb2.UfResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)