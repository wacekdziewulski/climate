FROM ubuntu:18.04
RUN apt update
RUN apt install -y python3
RUN mkdir -p /usr/local/climate/
COPY CLImate.py /usr/local/climate/
COPY CLImate_mocks.json /usr/local/climate/
RUN ln -s /usr/local/climate/CLImate.py /usr/local/climate/ls 
RUN ln -s /usr/local/climate/CLImate.py /usr/local/climate/pwd
ENV PATH="/usr/local/climate/:${PATH}"
