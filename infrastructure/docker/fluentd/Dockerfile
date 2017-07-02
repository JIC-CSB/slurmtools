FROM centos/ruby-23-centos7
MAINTAINER Matthew Hartley <Matthew.Hartley@jic.ac.uk>

RUN yum install -y telnet

ADD install_fluentd.sh /root/install_fluentd.sh
RUN /root/install_fluentd.sh
