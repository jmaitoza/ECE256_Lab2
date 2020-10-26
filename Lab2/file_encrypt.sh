#!/bin/bash

file=$1
algo=$2
#block size
key=$3

cc='CC'
vc='VC'

if [[ $algo == $cc ]]
then
	python caesar_encrypt.py $key
elif [[ $algo == $vc ]]
then
	python vig_encrypt.py $key
else
	echo "Improper algorithm"
fi





