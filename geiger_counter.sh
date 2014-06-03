# Generates data for the geiger counter analysis and analyses it.

# COMPLETE THESE GROUP 3

# Make a loop which calls 
#   python geiger_counter.py generate 40 10000
# 20 times, and saves the output to data/filename_$i.csv

# Make a loop which calls
#   python geiger_counter.py plot <filename> 15
# for every filename in data/

# call to the generating .py script
#for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
for i in {1..20}
do
 python geiger_counter.py 40 10000 > data/filename_$i.csv
done
