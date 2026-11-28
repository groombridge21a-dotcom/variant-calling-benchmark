REF = "ref/chr20.fa"

rule align:
    input:
        ref = REF,
        r1 = "data/sim9x_1.fq",
        r2 = "data/sim9x_2.fq"
    output:
        "data/sm_sim9x.sorted.bam"
    threads: 4
    shell:
        "bwa mem -t {threads} {input.ref} {input.r1} {input.r2} | samtools sort -@ 2 -o {output}"
rule call:
    input:
         ref = REF,
         bam = "data/sm_sim9x.sorted.bam"
    output:
        "data/sm_sim9x.vcf"
    shell:
        "bcftools mpileup -f {input.ref} {input.bam} | bcftools call -mv -Ov -o {output}"
