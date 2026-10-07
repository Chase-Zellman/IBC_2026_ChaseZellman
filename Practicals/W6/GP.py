import pickle
genetic_code = pickle.load(open("genetic_code.pickle", "rb"))

def get_amino_acids(mRNA):
        i = 0
        aa_sequence = []
        while (i + 3) <= len(mRNA):
            codon = mRNA[i:(i + 3)]
            aa = genetic_code[codon]
            if aa == "Stop":
                break
            else:
                aa_sequence.append(aa)
            # advance to the next codon
            i = i + 3
        return "".join(aa_sequence)

genes = {}
with open("Turkey_transcripts_15_coding.fasta", "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            header = line
            genes[header] = ""
        else:
            genes[header] = genes[header] + line

with open("Turkey_transcripts_15_aa.fasta", "w") as outfile:
    for header, mRNA in genes.items():
        aa_sequence = get_amino_acids(mRNA.replace("T", "U"))
        outfile.write(header.replace("gbskey=CDS", "gbskey=AA") + "\n")
        outfile.write(aa_sequence + "\n")

print(open("Turkey_transcripts_15_aa.fasta", "r").read())
