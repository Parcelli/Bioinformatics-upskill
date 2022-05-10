#!usr/bin/env bash
#Calculating genome coverage using bedtools genomecov
#input = sorted bam files
#output = bedgraph
for file in *sorted.bam
do
    echo ${file}
    bedtools genomecov -max $1 -ibam ${file} -bga > ${file}.txt
done
