# Day 4: first variant call
bwa mem -k 8 -T 10, samtools sort/index, bcftools mpileup -B -A -Q 0 | call -mv --ploidy 1. Found toyref 29 G>A (QUAL 101).
