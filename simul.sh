#!/bin/bash
#./simul 10G 0.001 100 500 1400

# store arguments in an array 
args=("$@") 
# get number of elements 
ELEMENTS=${#args[@]} 
 
data=$1
ber=$2
step=$3


if [ $# -eq 0 ]; then
    echo "usage : ./simul.sh <taille données> <BER> <step>"
    exit
fi

echo "Starting simulation..."
rm -f results.txt

# for each data paylaod
for (( i=200;i<=1476;i+=$step)); do
	cd src/
	results=$(python3 main.py -q -P $i -r $data $ber)
 	read results< <(echo "$results" | tail -n1)
	echo $results
	cd ../
	touch results.txt
	results="$results \n"
	echo $results$'\r' >> results.txt
done

gnuplot -p -e "plot 'results.txt' u 3:4 w l"

echo "done!"

