#!/usr/bin/env python3
import pickle
genetic_code = pickle.load(open("genetic_code.pickle", "rb"))
Turkey_transcripts_15 = open("Turkey_transcripts_15.fasta", "r")

def get_amino_acids(mRNA):
        i = 0
        aa_sequence = []
        while (i + 3) < len(mRNA):
            codon = mRNA[i:(i + 3)]
            aa = genetic_code[codon]
            if aa == "Stop":
                break
            else:
                aa_sequence.append(aa)
            # advance to the next codon
            i = i + 3
        return "".join(aa_sequence)
print(get_amino_acids(Turkey_transcripts_15))