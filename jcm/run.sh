#!/bin/bash
docker build --rm=true -t temp ./
docker run -p 8999:8888 --name tmp   temp
docker rm tmp
docker rmi temp