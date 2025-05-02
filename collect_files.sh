#!/bin/bash

if [[ $4 == "" ]]; then
  find $1 -type f -exec cp {} $2 \;
else
  python3 main.py $1 $2 $4
fi
