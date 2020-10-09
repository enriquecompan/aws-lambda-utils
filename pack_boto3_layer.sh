#!/bin/bash

mkdir -p boto3-layer/python
(
  cd boto3-layer || exit
  pip3 install boto3 -t python
  T=($(pip3 list boto3 | grep boto3))
  zip -r boto3-"${T[1]}"-layer.zip python
  mv *.zip ..
  cd ..
  rm -rf boto3-layer
  printf "\nLayer boto3-%s.zip created. \n\n" "${T[1]}"
)
