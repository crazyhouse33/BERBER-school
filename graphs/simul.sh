#!/bin/bash

if [ $# -eq 0 ]; then
    echo "- Usage 1 -> ber fixe, payload variable :"
    echo " ./simul.sh -p <fichier> <BER> <payload_min> <payload_max> <pas>"
    echo "- Usage 2 -> payload fixe, ber variable :"
    echo " ./simul.sh -b <taille donnees> <payload> <ber_min> <ber_max>"
    exit
fi

rm -f results.txt
echo "Starting simulation..."

if [ $1 == "-p" ]; then
	echo "Usage 1 : ber fixe, payload variable"
	data=$2
	ber=$3
	payload_min=$4
	payload_max=$5
	step=$6
	for ((payload=$payload_min;payload<=$payload_max;payload+=$step)); do
		#cd ../src/
		results=$(python3 ../src/main.py -q -P $payload -s file -m simulated $data $ber)
		read results< <(echo "$results" | tail -n1)
		echo $results
		#cd ../
		touch results.txt
		chmod 777 results.txt
		results="$results \n"
		echo $results$'\r' >> results.txt
	done
	gnuplot -p -e "plot 'results.txt' u 3:4 w l"
fi

if [ $1 == "-b" ]; then
	echo "Usage 2 : payload fixe, ber variable"
	data=$2
	payload=$3
	ber_min=$4
	ber_max=$5
	ber=$ber_min
	step=`echo $ber_max 10 | awk '{print $1 / $2}'`

	#multiplication pour passer le while
	ber=`echo $ber 1000000000 | awk '{print $1 * $2}'`
	ber_max=`echo $ber_max 1000000000 | awk '{print $1 * $2}'`

	while [ $ber -lt $ber_max ]
	do
		#division pour reprendre vraies valeurs
		ber=`echo $ber 1000000000 | awk '{print $1 / $2}'`
		ber_max=`echo $ber_max 1000000000 | awk '{print $1 / $2}'`
		ber=`echo $ber $step | awk '{print $1 + $2}'`
		#echo $ber
		cd src/
		results=$(python3 main.py -q -P $payload -s randomF $data $ber)
		read results< <(echo "$results" | tail -n1)
		echo $results
		cd ../
		touch results.txt
		results="$results \n"
		echo $results$'\r' >> results.txt
		ber=`echo $ber 1000000000 | awk '{print $1 * $2}'`
		ber_max=`echo $ber_max 1000000000 | awk '{print $1 * $2}'`
	done
	gnuplot -p -e "plot 'results.txt' u 2:4 w l"
fi

echo "done!"
