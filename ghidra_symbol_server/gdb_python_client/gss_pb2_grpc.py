# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import gss_pb2 as gss__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in gss_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class GhidraSymbolServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSymbolAtAddress = channel.unary_unary(
                '/ghidrasymbolserver.GhidraSymbolServer/GetSymbolAtAddress',
                request_serializer=gss__pb2.UInt64.SerializeToString,
                response_deserializer=gss__pb2.String.FromString,
                _registered_method=True)
        self.GetAddressOfSymbol = channel.unary_unary(
                '/ghidrasymbolserver.GhidraSymbolServer/GetAddressOfSymbol',
                request_serializer=gss__pb2.String.SerializeToString,
                response_deserializer=gss__pb2.UInt64.FromString,
                _registered_method=True)
        self.GetAllSymbols = channel.unary_unary(
                '/ghidrasymbolserver.GhidraSymbolServer/GetAllSymbols',
                request_serializer=gss__pb2.EmptyMessage.SerializeToString,
                response_deserializer=gss__pb2.SymbolList.FromString,
                _registered_method=True)
        self.SetCurrentAddress = channel.unary_unary(
                '/ghidrasymbolserver.GhidraSymbolServer/SetCurrentAddress',
                request_serializer=gss__pb2.UInt64.SerializeToString,
                response_deserializer=gss__pb2.EmptyMessage.FromString,
                _registered_method=True)


class GhidraSymbolServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSymbolAtAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAddressOfSymbol(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllSymbols(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCurrentAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GhidraSymbolServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSymbolAtAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSymbolAtAddress,
                    request_deserializer=gss__pb2.UInt64.FromString,
                    response_serializer=gss__pb2.String.SerializeToString,
            ),
            'GetAddressOfSymbol': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAddressOfSymbol,
                    request_deserializer=gss__pb2.String.FromString,
                    response_serializer=gss__pb2.UInt64.SerializeToString,
            ),
            'GetAllSymbols': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllSymbols,
                    request_deserializer=gss__pb2.EmptyMessage.FromString,
                    response_serializer=gss__pb2.SymbolList.SerializeToString,
            ),
            'SetCurrentAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCurrentAddress,
                    request_deserializer=gss__pb2.UInt64.FromString,
                    response_serializer=gss__pb2.EmptyMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ghidrasymbolserver.GhidraSymbolServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ghidrasymbolserver.GhidraSymbolServer', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class GhidraSymbolServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSymbolAtAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ghidrasymbolserver.GhidraSymbolServer/GetSymbolAtAddress',
            gss__pb2.UInt64.SerializeToString,
            gss__pb2.String.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAddressOfSymbol(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ghidrasymbolserver.GhidraSymbolServer/GetAddressOfSymbol',
            gss__pb2.String.SerializeToString,
            gss__pb2.UInt64.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAllSymbols(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ghidrasymbolserver.GhidraSymbolServer/GetAllSymbols',
            gss__pb2.EmptyMessage.SerializeToString,
            gss__pb2.SymbolList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetCurrentAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ghidrasymbolserver.GhidraSymbolServer/SetCurrentAddress',
            gss__pb2.UInt64.SerializeToString,
            gss__pb2.EmptyMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
