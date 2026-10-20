#!/usr/bin/bash

#Variable assigning takes in the first and second arguement
File_name="$1"
ID="$2"

#ID_num takes first column of file name inputted and then finds how many times the ID input is in there
ID_num=$(cut -f 1 "${File_name}" | grep -c "${ID}")
echo "${ID} appears ${ID_num} Times!"
