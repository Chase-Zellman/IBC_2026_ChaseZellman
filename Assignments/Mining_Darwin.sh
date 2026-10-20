curl https://www.gutenberg.org/cache/epub/1228/pg1228.txt -o The_Orgin_Darwin.txt

grep -i "sterility" The_Orgin_Darwin.txt | wc -l
grep -i "isolation" The_Orgin_Darwin.txt | wc -l

grep -i -B 3 -A 3 "sterility" The_Orgin_Darwin.txt > sterility.txt
grep -i -B 3 -A 3 "isolation" The_Orgin_Darwin.txt > isolation.txt

python -m wordcloud --text sterility.txt --imagefile sterility_cloud.png
python -m wordcloud --text isolation.txt --imagefile isolation_cloud.png
