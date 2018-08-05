#!/bin/bash

dir=/tmp/todo
mkdir $dir

cp ./todo.py $dir
alias todo="python /tmp/todo/todo.py"
