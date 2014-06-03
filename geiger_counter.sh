# Generates data for the geiger counter analysis and analyses it.

for i in `seq 20`
do
    # generate a data file with 10000 points
    python geiger_counter/geiger_counter.py generate 40 10000 > data/rad_$i.csv
done

# find all CSVs in data
for i in data/*.csv
do
    # use the python script to plot them
    python geiger_counter/geiger_counter.py plot $i 15
done
