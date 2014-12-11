#!/usr/bin/python

import sys

def locate_aligned_reads(input_start, input_end, mapped_input_file, 
	reads_input_file, output_file):
	# Constants relating to mapped file fasta format list locations
	QNAME = 0
	TSTART = 7
	TEND = 8
	
	# Open two input files and the output file
	m = open(mapped_input_file)
	r = open(reads_input_file)
	o = open(output_file, 'w')
	
	qnames = []
	
	for mline in m:
		# separate the line on the spaces, returns a list.
		mapped_line = mline.split()
		
		# If it starts in the range, ends in the range, or spans the entire 
		# range include it in the output
		if (int(input_start) <= int(mapped_line[TSTART]) <= int(input_end) or 
			int(input_start) <= int(mapped_line[TEND]) <= int(input_end) or 
			int(mapped_line[TSTART]) < int(input_start) and 
			int(mapped_line[TEND]) > int(input_end)):
				# ugly code that takes leading > and everything after the last /
				modified_qname = '/'.join(mapped_line[QNAME].split('/')[:-1])
				qnames.append(modified_qname)
	
	read_in = False
	for rline in r:
		if(read_in and rline[0] != '>'):
				o.write(rline)
		else:
			for qname in qnames:
				# checks to see if read name (without > and \n) matches the one 
				# from the mapped file
				if (rline[1:-1] == qname):
					read_in = True
					o.write('>' + qname + '\n')
					break
				else:
					read_in = False
			
	m.close()
	r.close()
	o.close()

# code that tests my function

# Usage: find_mapped_reads.py [reads] [mapping] [start] [end] [output]

args = sys.argv

locate_aligned_reads(args[3], args[4], args[2], args[1], args[5])
