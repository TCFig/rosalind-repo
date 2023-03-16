# ==== Counting DNA nucleotides =====
sequence = 'TTATAAGATACTTGAGAGGGGGGGCATCGTAACATCCCAAAGGAGCAAGCGCTTAAAAGCTCTCTAAGGATGGACCTACCTCGTCGCGCAGTATGGGCTATAGGCGCCCTCGATGAGAAACCCTAAGATACTCCCAGAACGGTTGTGTGGCTTATGGTCTAATGTAAACACGCCTGCACACCATATATGACGGCCTCTCCCGGTGGTTGTCCGTCGAATGCACTCCAAGGACGGATTCAATACCGACATGAAACGTGTTCCTCTTGACTTGCTACCTATGTATAATTATCGCAAGTGGTCTAGGTAAATATCCTCCAAGGATAATTGTTAGTCCTCAGGATCCATGTATACTGTCAGTGATCAGATTTGAGTGAGGCCATAAAATACAGGTGTGTCTCTCTACTGTGAGACAGCCGGGGCGAACCACGTCAACGCTGTCACGATGAATCCGCCCTCGTTCTATTCACATGTGCGCTCAGACAGCTATTCAACTATCGCTCCAAGTTAAGAGCATATGACCGTACTCGAAATTCGCAGGAGGCGTCTAAAGCGGAGAGGTCTGGGTCGATGGTACCACGGTTTCACACTCTCTCTACTGTGATCCTGCTGCGGAGACCAGCGGCGACTATTGGTAGTTATCGTGGAGTCCGGATAACTGGTATGCGTTAGCTTTACGCCACATTGTGGGTCTGACTAGGCCGGTCTCGGCGTACCGGGTTGTGTACTCCACTTCCCCGGTTAACAGGGCCGACGCTACTAGCGAGTTAACGAATAATATTTTCCTCGCGACAACACGTGCCGTTGACGCGTATTCTATTAACAACACCTTCCATATCACAAAGAAAGACTTTCCACAGGGTGGGATCCAGCCAAAATGACGCTCAAGTACGCCAAAGTTGTACCCCTAAATAATTTCGCGGAGACTGACGTCAATTGTTTAATTACCTGTCAAAATATGATGTAGGGTAGGGGAGTACTTCAACC'
dicNucleotides = {}

for nucleotide in sequence:
    if nucleotide not in dicNucleotides:
        dicNucleotides[nucleotide] = 1
    else:
        dicNucleotides[nucleotide] = dicNucleotides[nucleotide] + 1

print('==============Counting DNA nucleotides================')
for nucleotide, value in dicNucleotides.items():
    print(f'{nucleotide} {value}')

# ==== Transcribing DNA into RNA ======

CDS = 'TAGTTGAGAACGTCGTATTCAGCACGAACTTGGCTTACGTCACCCCAGCGCCGAGCCGCTCCCGTGGCCCCAACATGCCTATACCACTAGGACTTCGAAGTGCTAGGTCGGGCCACGACCGAGAAATGTTGTACGGTTTAAGTCAAGTCTAGCTAGTACTGCTCACCCTACCCTTTTTTTTCGAGCGGACCTTAGAAAGTAGTCTTGGAACCAAAAATCCTTATACCAAGAGGGCGATCGCCCAACTTGAAAACATTTTTATATTAGGAATGATCTGATTATTGTACCTTAGCGTGCATCCGTAACAAGGGTGCCACGTAGTCCCGCTCCGAGGAACGAGCCAGTGCAGGCAAGTGTCACTTCCTACTATTGTTCTATGCGCGCGCGAACCGCAGATGTAAGGTACCAAATCTTGCCACCTTTAGTATGCAAACGCACATTCCAGGGAGATAACCTCTCCTAGGCGCGCACCGGTACCCCGCGTGGTCGGGAAGACCGATCCTTTGTTTAGGTATCGCTAGTCCCCATGAAGGAATGGATTCGGAGGTCATTCGCATCCAACGCTCCGTACCCCGAAGTGCAATAGAGAGTACTTACTCCGTACCACGGCATGTCTCGCGCTTTCATCGTACGCATCGCTATAGCATGACGAATCGTATTGGTGCTTATTCTCGGTCTATGCATGGTGGCATCGTCCCGGTACCGCGGTCATAGAGGTGTCTAACCCTCGGGATAAGTATCCACGCGGGCGGCTGGGTGAGAGAAGTCGCCTATGCCTTATCAGAGATTTGATGTATTACATTTAAACGGACCATCCTCTTTCAAATAAACTAGGACGTCATTATCCCGTCGTGGTTTTTTGAAGACTGGACCATCCACGTGGTATTACCGTTTTTGGGTTTGACATAAGAGGTCCGCACGACCGGTCTACAAGGA'
transcript = CDS.replace('T', 'U')

print('==============Transcribing DNA into RNA================')
print(transcript)

# ===== Complementing a Strand of DNA ========

CDS = 'GTTTAAGCTTTCACTAGTGCGGTAGGGTCTATAACTATAGGATACTAAACTGCAGTTTTTTTGCAACGAGATTGTCGATGAGAATTTGATTCGTACTGCCGCATCAGTATGGTTACGAACGGATCGGACATTCGTCCTTGCGCTTAAACAGGCCATTCTAGAACCAAGCTTTGGTGAGACGAGAAAAGAGCGCATCCGCCTGATAAGAAAAAGCTCGCCAATCCATGTGGCCAATGCGCAGTGGCATCCCCGACTGCCCCCTTAGCCACGCTAGCCTCTATGGTTGGCCTGACATAATCACAAAATTCATCATTGTGGAGCCGAGGTTCGCGGCCCGCTGGTGGTACGTATAACTCCACGATTGTTGCGTCTGCGAGTGGGGTGGCCTGAGGAGCGGCCCTAGATATAAGGGACCCACCATAGGTATAAGGCAAGGCGCAATCTATGGTGCCTCGACTACATCAGAGTCTCTCGTGTTCCTCGCCCACCCTATATCGGTACCTCTATTAGTGAATCACGCTGAAACCTGGACTCACACTGGTATCTAGAGCGGGCAATAGTATAGCTCGTTGGGGCACCGACGTCTCTACGTTCGCTTTCACAGCTGAGGATCCCTTGGAGCGAATTTTTACCCCTTTGGGATAACTGGCCCCATGCACGATCGTCACTCGTCAAATGGTTGTTGTATGAGGAGGGAATAAACGCTACGGTGGTTGCGGGGTTATGTGTTCTTGCGCTGCCTTTGTTAGAGCCCTGCCGGTTCGGTGCAGTTGAGTACGCGGCTCTGCACTTGCCGTTAACA'
charReplace = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}  # make dic for key(old value) and value(old value)

compStrand = CDS.translate(str.maketrans(charReplace))  # apply the translate() function and give the dic
revCompStrand = compStrand[::-1]  # reverse the transcript

print('============ Complementing a Strand of DNA =============')
print(revCompStrand)

# ===== Rabbits and Recurrence Relations ========

# Fn = Fn−1 + Fn−2, where Fn is equal ro the number of pairs in n months
nmonths = 35
klitter = 4


def fibonacci(n):
    if n == 0:
        return 0  # in month 0 there were no rabbits
    elif n == 1 or n == 2:
        return 1  # in month 1 rabbits were newborn and in month 2 they started to reproduce
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) * klitter  # There will only be progeny from rabbits that are alive
        # for 2 months. Because rabbits take 1 month to grow up + 1 month to have progeny


print('========= Rabbits and Recurrence Relations ==========')
print(fibonacci(nmonths))