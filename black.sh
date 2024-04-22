#!/bin/bash
if [ -z "$1" ]
then
    black -t py36 --exclude=migrations --include='\.py$'  ./
else
    black -t py36 --exclude=migrations --include='\.py$'  ./  "$1"
fi

