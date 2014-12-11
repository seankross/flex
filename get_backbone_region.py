from read_fasta import *
import sys

args = sys.argv

start = int(args[3])
end = int(args[4])

backbone = fasta_array(args[1])[0][1][start:(end + 1)]
consensus = fasta_array(args[2])[0][1]

if len(backbone) > len(consensus):
	small = consensus
	big = backbone
else:
	small = backbone
	big = consensus

print(max_percent_identity(small, big))