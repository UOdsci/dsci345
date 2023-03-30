#!/bin/bash

for x in $(ls -t *.ipynb)
do 
    if [ ! $(grep -l ${x%ipynb} .gitignore) ]
    then
       y="${x%ipynb}html"
       if [ "$x" -nt "$y" ]
       then
           echo "$y"
       fi
    fi
done
