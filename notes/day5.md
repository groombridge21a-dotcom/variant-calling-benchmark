# Day5: chr20 simulated data
wgsim 1M read pairs (150bp) on chr20; bwa mem -t 4;samtools sort/index; bcftools mpileup | call -mv, 2,000,000 reads, 100% mapped, 33,540 variants called.
