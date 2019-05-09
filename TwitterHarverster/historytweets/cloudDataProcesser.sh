#!/usr/bin/env bash

#(2014 2015 2016 2017 2018 2019)
years=(2014 2017 2018 2019)
cities=(adelaide brisbane canberra hobart melbourne perth sydney)

for year in "${years[@]}"
do
    for city in "${cities[@]}"
    do
        echo ${city}${year}.json






        # nohup python3 docReader.py 1>docout.txt 2>docerror.txt &
        rm ${city}${year}.json

    done

done

