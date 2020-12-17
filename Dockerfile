FROM centos:7
LABEL project="listrepo"
WORKDIR /listrepo_docker
RUN yum localinstall listrepo-1.0-1.el7.centos.noarch.rpm
