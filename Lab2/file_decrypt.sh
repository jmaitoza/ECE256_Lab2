#!/bin/bash
start=`date +%s%N`
file=$1
algo=$2
#block size
key=$3

cc='CC'
vc='VC'

if [[ $algo == $cc ]]
then
        python caesar_decrypt.py $key
elif [[ $algo == $vc ]]
then
        python vig_decrypt.py $key
else
        echo "Improper algorithm"
fi

end=`date +%s.%N`

