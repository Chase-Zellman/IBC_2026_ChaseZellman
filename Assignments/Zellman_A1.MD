# Assignment 1

## Number of Subjects
### A
To download the file, we can do a simple git pull then a further copy command can move the file to the students desired destination such as the code that follows
``` bash
git pull
cp Gesquiere2011_data.csv ../../IBC_2026_ChaseZellman/Assignments/
```

### B & C
For this code we have our bash shebang to start the code then File_name and ID are my variables like asked. They take in argument 1 and 2 as their values respectively. Then the code is a simple cut and grep. It takes the first column and finds how many times the number you give it appears. Then it out puts the number you asked for and how many times it appears.

For clarity ID_Num has 
```Bash
$()
```
with the code in the parenthesis that allows you to assign a command to a variable as a value which is more common in python, but this is the bash syntax. Also, variables are called with 
```Bash
${} 
```
I prefer this over lots of "" which can be used to also call variables. 

``` Bash
#!/usr/bin/bash

#Variable assigning takes in the first and second arguement
File_name="$1"
ID="$2"

#ID_num takes first column of file name inputted and then finds how many times the ID input is in there
ID_num=$(cut -f 1 "${File_name}" | grep -c "${ID}")
echo "${ID} appears ${ID_num} Times!"
```

### D

``` Bash
#!/usr/bin/bash

ID_Count=$(tail -n +2 Gesquiere2011_data.csv | cut -f 1 | sort -n -u | wc -l)

echo "MaleID,Num_samples" > Num_samples.csv

while read -r ID_Count
    do ID_Times_Count=$( cut -f 1 Gesquiere2011_data.csv | grep -x -c "${ID_Count}")
        echo "${ID_Count}, ${ID_Times_Count}" >> Num_samples.csv
done < <(tail -n +2 Gesquiere2011_data.csv | cut -f 1 | sort -n -u)

echo "Script Finished!"
```


