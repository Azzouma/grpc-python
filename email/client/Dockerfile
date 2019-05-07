FROM ubuntu

# Pre-reqs
RUN apt-get update
RUN apt-get install -y software-properties-common

# Install python3.6 
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get install -y python3.6
RUN apt install -y python3-pip
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10
RUN update-alternatives --config python

# Copy files
COPY *.proto .
COPY addressbook_client.py .

# Install gRPC
RUN python -m pip install grpcio

# Install gRPC tools
RUN python -m pip install grpcio-tools

# Create stub files
RUN python -m grpc_tools.protoc --proto_path=. ./addressbook.proto --python_out=. --grpc_python_out=.

#Expose port and start application
EXPOSE 50056
CMD [ "python", "addressbook_client.py" ]