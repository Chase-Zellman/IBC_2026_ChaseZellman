import matplotlib.pyplot as plt
import re
import csv
import pdb

# let plots be produced within the IPython notebook
#%matplotlib inline

zip_find = []
with open("pubmed_results.txt", "r") as f:
    for line in f:
        zip_find = zip_find + re.findall(r'\d{5}', line)

zip_code = []
zip_long = []
zip_lat = []
zip_count = []
with open("zipcodes_coordinates.txt", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row[0] in zip_find:
            zip_code.append(row[0])
            zip_long.append(float(row[1]))
            zip_lat.append(float(row[2]))
            zip_count.append(zip_find.count(row[0]))

plt.scatter(zip_long, zip_lat, s = zip_count, c= zip_count)
plt.colorbar()

# only continental us without Alaska
plt.xlim(-125,-65)
plt.ylim(23, 50)

# add a few cities for reference (optional)
ard = dict(arrowstyle="->")
plt.annotate('Los Angeles', xy = (-118.25, 34.05), 
    xytext = (-108.25, 34.05), arrowprops = ard)
plt.annotate('Palo Alto', xy = (-122.1381, 37.4292), 
    xytext = (-112.1381, 37.4292), arrowprops= ard)
plt.annotate('Cambridge', xy = (-71.1106, 42.3736), 
    xytext = (-73.1106, 48.3736), arrowprops= ard)
plt.annotate('Chicago', xy = (-87.6847, 41.8369), 
    xytext = (-87.6847, 46.8369), arrowprops= ard)
plt.annotate('Seattle', xy = (-122.33, 47.61), 
    xytext = (-116.33, 47.61), arrowprops= ard)
plt.annotate('Miami', xy = (-80.21, 25.7753), 
    xytext = (-80.21, 30.7753), arrowprops= ard)

params = plt.gcf()
plSize = params.get_size_inches()
params.set_size_inches( (plSize[0] * 3, plSize[1] * 3) )

plt.show()
