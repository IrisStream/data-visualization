#!/bin/sh

cd corona
now=$(date +%d-%m)
scrapy crawl covid -o ../../data/"$now".csv
cd ..
