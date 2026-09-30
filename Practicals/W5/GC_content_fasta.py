#!/usr/bin/env python3

genes = {}

with open("Turkey_transcripts_15.fasta", "r") as f:
    for line in f:
        line = line.rstrip()
        if line.startswith(">"):
            gene_id = line[1:]
        else:
            seq = line
            
print(genes)

with open("Turkey_transcripts_15.fasta") as infile, open("gc_content.txt", "w") as outfile:
    for gene_id, seq in genes:
        gc = (seq.count("G") + seq.count("C")) /len(seq)
        outfile.write(gene_id+"\t"+str(gc)+"\n")


