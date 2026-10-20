#!/usr/bin/bash

ID_Count=$(tail -n +2 Gesquiere2011_data.csv | cut -f 1 | sort -n -u | wc -l)

echo "MaleID,Num_samples" > Num_samples.csv

while read -r ID_Count
    do ID_Times_Count=$( cut -f 1 Gesquiere2011_data.csv | grep -x -c "${ID_Count}")
        echo "${ID_Count}, ${ID_Times_Count}" >> Num_samples.csv
done < <(tail -n +2 Gesquiere2011_data.csv | cut -f 1 | sort -n -u)

echo "Script Finished!"
