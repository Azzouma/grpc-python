from __future__ import print_function
import logging

import grpc

import addressbook_pb2
import addressbook_pb2_grpc


def run():
    with grpc.insecure_channel('addressbook_server:50057') as channel: # fixed
        stub = addressbook_pb2_grpc.address_infoStub(channel) # looking for stub of the service defined in proto file
        search_response = stub.search_user(addressbook_pb2.user_email(email='vtom2019@gmail.com'))  # call the rpc function defined in proto file and implemented in the server
        insert_response = stub.insert_user(addressbook_pb2.user_info(id=1,first_name="John",last_name="Doe",email="vtom2019@gmail.com"))
        print("search_response: ", search_response)
        print("insert_response: ", insert_response)

if __name__ == '__main__':
    logging.basicConfig()
    run()
