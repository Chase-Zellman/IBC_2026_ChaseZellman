# Shebang
#!/usr/bin/env python3

#Dictionary with codons as the keys and then the symbols as the values
codon_symbol_dict = {'AAA': 'K', 'AAC': 'N','AAG': 'K', 'AAT': 'N', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGT': 'S', 'ATA': 'I', 'ATC': 'I', 'ATG': 'M',
'ATT': 'I', 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAT': 'H', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CGA': 'R', 'CGC': 'R','CGG': 'R', 'CGT': 'R', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAT': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V', 'TAA': 'O',
'TAC': 'Y', 'TAG': 'O', 'TAT': 'Y', 'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', 'TGA': 'O', 'TGC': 'C', 'TGG': 'W', 'TGT': 'C', 'TTA': 'L', 'TTC': 'F', 'TTG': 'L', 'TTT': 'F'}

#Dictionary with the symbol as the keys and then the amino acids as the values
symbol_values = {'K': 'Lys', 'N': 'Asn', 'K': 'Lys', 'N': 'Asn','T': 'Thr', 'T': 'Thr', 'T': 'Thr', 'T': 'Thr', 'R': 'Arg', 'S': 'Ser', 'R': 'Arg', 'S': 'Ser', 'I': 'Ile', 'I': 'Ile', 'M': 'Met', 
'I': 'Ile', 'Q': 'Gln', 'H': 'His', 'Q': 'Gln', 'H': 'His', 'P': 'Pro', 'P': 'Pro', 'P': 'Pro', 'P': 'Pro', 'R': 'Arg', 'R': 'Arg', 'R': 'Arg', 'R': 'Arg', 'L': 'Leu', 'L': 'Leu', 'L': 'Leu', 'L': 'Leu', 
'E': 'Glu', 'D': 'Asp', 'E': 'Glu', 'D': 'Asp', 'A': 'Ala', 'A': 'Ala', 'A': 'Ala', 'A': 'Ala', 'G': 'Gly', 'G': 'Gly', 'G': 'Gly', 'G': 'Gly', 'V': 'Val', 'V': 'Val', 'V': 'Val', 'V': 'Val', 'O': 'Stp',
'Y': 'Tyr', 'S': 'Ser', 'S': 'Ser', 'S': 'Ser', 'S': 'Ser', 'O': 'Stp', 'C': 'Cys', 'W': 'Trp', 'C': 'Cys', 'L': 'Leu', 'F': 'Phe', 'L': 'Leu', 'F': 'Phe'}

#Sequence asked to input
seq = "CTA GCA GTG ATT TCG"

#Codons variable is the result from seq.split and it splits at each space seperating each one into codons
codons = seq.split(" ")

#Creates empty list
amino_seq = []

#For loop that goes through and then matches the codon in the codons variable and matches codon to symbol then symbol to amino
for codon in codons:
    if codon in codon_symbol_dict:
        symbol = codon_symbol_dict[codon]
        amino_acid = symbol_values[symbol]
        amino_seq.append(amino_acid)
    else:
        print("No match found")

#Prints the amino sequence
print(amino_seq)


