from concurrent import futures
import time
import logging

import grpc

import addressbook_pb2
import addressbook_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Server(addressbook_pb2_grpc.address_infoServicer):  # looking for stub of the service defined in proto file

    def search_user(self, request, context): # instantiate the rpc function defined in proto file
        print("context: ", context)
        return addressbook_pb2.user_info( id          = 1,
                                          first_name  = "John",
                                          last_name   = "Doe",
                                          email       = '%s' % request.email
                                          )
    def insert_user(self, request, context): # instantiate the rpc function defined in proto file
        print("context: ", context)
        return addressbook_pb2.user_info( id          = request.id,
                                          first_name  = '%s' % request.first_name,
                                          last_name   = '%s' % request.last_name,
                                          email       = '%s' % request.email
                                          )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) #fixed
    addressbook_pb2_grpc.add_address_infoServicer_to_server(Server(), server) # # looking for stub of the service defined in proto file
    server.add_insecure_port('[::]:50057') # fixed
    server.start() # fixed
    try: # fixed
        while True: # fixed
            time.sleep(_ONE_DAY_IN_SECONDS) # fixed
    except KeyboardInterrupt: # fixed
        server.stop(0) # fixed


if __name__ == '__main__': # fixed
    logging.basicConfig() # fixed
    serve() # fixed
