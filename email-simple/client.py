import grpc
import addressbook_pb2
import addressbook_pb2_grpc

 
def call_server(first_name, last_name): 
    host = 'localhost'
    server_port = 50067
    channel = grpc.insecure_channel('{}:{}'.format(host, server_port))

    stub = addressbook_pb2_grpc.EmailInfoStub(channel)

    input_to_server = addressbook_pb2.Person(FirstName=first_name, LastName=last_name) 
    return stub.GetEmailInfo(input_to_server)

if __name__=='__main__':
    call_server("asmaa", "chebba")