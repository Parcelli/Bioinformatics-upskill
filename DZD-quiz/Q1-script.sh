#!usr/bin/env bash
#Created by Parcelli Jepchirchir on  6th May 2022
#Aligning reads to  a refence genome(mecA gene) using BWA
#Step 1 : indexing the reference genome

bwa index -p mecA ../mecA.fa

#Step 2: Aligning reads to the mecA gene using bwa mem
# Step 3: convert sam files to bam file
for file in *.1.fastq;
do
    name=$(basename ${file} .1.fastq)
    echo ${name}
    bwa mem  ../mecA  ${file} ${name}.2.fastq > ${name}.sam
    samtools view -h  -b  ${name}.sam >${name}.bam
done
s

