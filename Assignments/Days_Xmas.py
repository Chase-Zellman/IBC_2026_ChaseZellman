Day_list = [
    "First",
    "Second",
    "Third",
    "Fourth",
    "Fith",
    "Sixth",
    "Seventh",
    "Eight",
    "Ninth",
    "Tenth",
    "Eleventh",
    "Twelth",
]

Verse_list = [
    "A Partridge in a Pear Tree",
    "2 Turtle Doves",
    "3 French Hens",
    "4 Colly Birds",
    "5 Gold Rings",
    "6 Geeese-a-Laying", 
    "7 Swans-a-Swimming",
    "8 Maids-a-Milking",
    "9 Ladies Dancing",
    "10 Lords-a-Leaping",
    "11 Pipers Piping",
    "12 Drummers Drumming"
]

for i in range(len(Day_list)):
    print(f"On the {Day_list[i]} day of Christmas my true love gave to me:")
    for j in range(i, -1, -1):
        if j == 1:
            print(Verse_list[j] + ", and")
        else:
            print(Verse_list[j])
    print("\n")
    
