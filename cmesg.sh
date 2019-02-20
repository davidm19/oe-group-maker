#!/bin/bash

FILE=a.txt

if [[ -e $FILE ]]; then
    rm $FILE
fi

git log --pretty=format:"%an: %s" > $FILE

less $FILE
