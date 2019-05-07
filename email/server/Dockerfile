FROM ubuntu

# Install mongo db
RUN apt-get update && apt-get install -y gnupg2
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E52529D4
RUN bash -c 'echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.0.list'
RUN apt-get update
RUN apt-get install -y mongodb-org
RUN apt-get install -y vim

# Pre-reqs
RUN apt-get install -y software-properties-common

# Install python3.6 
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get install -y python3.6
RUN apt install -y python3-pip
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10
RUN update-alternatives --config python

# Copy files
COPY *.proto .
COPY addressbook_server.py .
COPY mongo_setup mongo_setup
RUN chmod -R 755 mongo_setup
COPY requirements.txt mongo_setup
RUN pip3 install -r mongo_setup/requirements.txt

# Install gRPC
RUN python -m pip install grpcio

# Install gRPC tools
RUN python -m pip install grpcio-tools

# Create stub files
RUN python -m grpc_tools.protoc --proto_path=. ./addressbook.proto --python_out=. --grpc_python_out=.

#Expose port and start application
EXPOSE 50056
CMD [ "python", "addressbook_server.py" ]