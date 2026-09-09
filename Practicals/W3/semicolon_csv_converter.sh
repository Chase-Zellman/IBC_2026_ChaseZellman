#!/bin/bash
cat $1 | tr ";" "," > "$1".csv
head -n 5 "$1".csv

