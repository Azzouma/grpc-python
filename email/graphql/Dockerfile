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
COPY *.py ./
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN python setup.py install

EXPOSE 5000
CMD [ "python", "server.py" ]
