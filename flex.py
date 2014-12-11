# Usage: python3 workspace.py mus.afa 20 .5 > consensus.fa

from read_fasta import *
import sys

args = sys.argv

fasta_file = args[1]
min_for_consensus = int(args[2])
threshold = float(args[3])
print_length = False
if len(args) > 4:
	print_length = True

# Sequences is an array of arrays which have the ID as their first element and 
# the sequence as the second element
sequences = fasta_array(fasta_file)
sequence_length = len(sequences[0][1])
number_of_sequences = len(sequences)

consensus_sequence = []

#For each position in the sequence
for i in range(0, sequence_length):
	nucleotides = []
	# For each sequence
	for j in range(0, number_of_sequences):
		nucleotides.append(sequences[j][1][i])
	gaps_removed = [x for x in nucleotides if x != "-"]
	common_element = most_common_element(gaps_removed)
	count_of_common_element = gaps_removed.count(common_element)
	achieved_threshold = fp_divide(count_of_common_element, len(gaps_removed))
	if len(gaps_removed) >= min_for_consensus and achieved_threshold >= threshold:
		consensus_sequence.append(common_element)
	elif len(gaps_removed) < min_for_consensus:
		x = 0
	else:
		consensus_sequence.append("N")

if print_length:
	print("Sequence Length:")
	print(len(consensus_sequence))
	print("Number N:")
	print(consensus_sequence.count("N"))
else:
	print(">Consensus")
	print(insert_newlines("".join(consensus_sequence)))
