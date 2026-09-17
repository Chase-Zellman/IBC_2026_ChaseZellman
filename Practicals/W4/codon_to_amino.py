# Shebang
#!/usr/bin/env python3

codon_dict = {AAA, AAC, AAG, AAT, ACA, ACC, ACG, ACT, AGA, AGC, AGG, AGT, ATA, ATC, ATG, ATT, CAA, CAC, CAG, CAT, CCA, CCC, CCG, CCT,
CGA, CGC, CGG, CGT, CTA, CTC, CTG, CTT, GAA, GAC, GAG, GAT, GCA, GCC, GCG, GCT, GGA, GGC, GGG, GGT, GTA, GTC, GTG, GTT, TAA, TAC, TAG,
TAT, TCA, TCC, TCG, TCT, TGA, TGC, TGG, TGT, TTA, TTC, TTG, TTT}

symbol_values = {}

amino_acid = {Lys, Asn, Lys, Asn, Thr, Thr, Thr, Thr, Arg, Ser, Arg, Ser, Ile, Ile, Met, Ile, Gln, His, Gln, His, Pro, Pro, Pro, Pro, Arg,
Arg, Arg, Arg, Leu, Leu, Leu, Leu, Glu, Asp, Glu, Asp, Ala, Ala, Ala, Ala, Gly, Gly, Gly, Gly, Val, Val, Val, Val, Stp, Tyr, Stp, Tyr, Ser,
,Ser, Ser, Ser, Stp, Cys, Trp, Cys, Leu, Phe, Leu, Phe}


seq = "CTA GGA GTG ATT TCG"
codons = seq.split(" ")

print(codons)

for codons in codon_dict:
    if codons == codon_dict:
        match = codon_dict[codons]
    else:
        match = "No match found"


