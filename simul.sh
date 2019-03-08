#!/bin/bash
#./simul 10G 0.001 100 500 1400

# store arguments in an array 
args=("$@") 
# get number of elements 
ELEMENTS=${#args[@]} 
 
data=$1
ber=$2

rm -f results.txt

# for each data paylaod
for (( i=2;i<$ELEMENTS;i++)); do
	cd src/
	results=$(python main.py -q -P ${args[${i}]} -r $data $ber)
	read results< <(echo "$results" | tail -n1)
	echo $results
	cd ../
	touch results.txt
	results="$results \n"
	echo $results$'\r' >> results.txt
done

echo "done!"
cmd /k



