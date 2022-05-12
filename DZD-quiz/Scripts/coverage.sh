#!usr/bin/env bash
#Computing genome coverage using bedtools genomecov.The output is a bedgraph consisting of chrom,start ,end and the depth columns.
for file in *sorted.bam
do
    echo ${file}
    bedtools genomecov  -ibam ${file} -bg  > ${file}.txt
done
