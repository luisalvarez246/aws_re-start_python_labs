with open('preproinsulin-seq-clean.txt', 'r') as file:
    text = file.read();
    
lsinsulin_seq_clean = text[0:24];
binsulin_seq_clean = text[24:54];
cinsulin_seq_clean = text[54:89];
ainsulin_seq_clean = text[89:110];

with open('lsinsulin-seq-clean.txt', 'w') as file:
    file.write(lsinsulin_seq_clean);
with open('binsulin-seq-clean.txt', 'w') as file:
    file.write(binsulin_seq_clean);
with open('cinsulin-seq-clean.txt', 'w') as file:
    file.write(cinsulin_seq_clean);
with open('ainsulin-seq-clean.txt', 'w') as file:
    file.write(ainsulin_seq_clean);
