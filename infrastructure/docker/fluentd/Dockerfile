FROM centos
MAINTAINER Matthew Hartley <Matthew.Hartley@jic.ac.uk>

RUN yum install -y ruby ruby-devel gcc make
RUN gem install fluentd 
RUN fluent-gem install fluent-plugin-mongo
