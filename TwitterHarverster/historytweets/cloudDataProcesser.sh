#!/usr/bin/env bash

years=(2014 2015 2016 2017 2018 2019)
cities=(adelaide brisbane canberra hobart melbourne perth sydney)

for year in "${years[@]}"
do
    for city in "${cities[@]}"
    do
        echo ${city}${year}.json

    done

done

