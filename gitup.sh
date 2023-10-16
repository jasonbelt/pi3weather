#!/usr/bin/env bash

export SCRIPT_HOME=$( cd "$( dirname "$0" )" &> /dev/null && pwd )
cd $SCRIPT_HOME

git pull --all
git add .
git commit -m "t"
git push
