import grpc
import time
import hashlib
import addressbook_pb2
import addressbook_pb2_grpc
from concurrent import futures
 
class AddressServicer(addressbook_pb2_grpc.EmailInfoServicer):
    def __init__(self, *args, **kwargs):
        self.host = 'localhost'
        self.server_port = 50067
 
    def GetEmailInfo(self, request, context):
        ## return the email address
        user_first_name = request.FirstName
        user_last_name = request.LastName
        email = user_first_name + "." + user_last_name + "@gmail.com" 
        print(email)
        result = {'Email': email}
        return addressbook_pb2.Emailaddress(**result)
 
    def start_server(self):
        # Fixed: don't change
        addressbook_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        addressbook_pb2_grpc.add_EmailInfoServicer_to_server(AddressServicer(),addressbook_server)
        addressbook_server.add_insecure_port('[::]:{}'.format(self.server_port))
        addressbook_server.start()
        print ('AddressBook Server running ...')
        try:
            while True:
                time.sleep(60*60*60)
        except KeyboardInterrupt:
            addressbook_server.stop(0)
            print('AddressBook Server Stopped ...')
 
email_server = AddressServicer()
email_server.start_server()