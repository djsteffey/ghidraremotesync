package ghidraremotesync.server;

import ghidraremotesync.Grs;
import ghidraremotesync.RemoteProgramListingGrpc;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.Server;
import io.grpc.ServerBuilder;

public class Main {
    public static void main(String[] args) throws Exception{
        Server server = ServerBuilder.forPort(50051)
                .addService(new RemoteProgramListingService())
                .build()
                .start();
        System.out.println("Server started on port 50051");
        server.awaitTermination();
    }
}
