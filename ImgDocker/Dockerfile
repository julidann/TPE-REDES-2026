FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx iproute2 ethtool python3 iputils-ping
COPY index.html /var/www/html/
COPY TCPServidor.py UDPServidor.py /opt/cdar/
EXPOSE 80/tcp
EXPOSE 15000/tcp
EXPOSE 15000/udp
CMD ["nginx", "-g", "daemon off;"]
