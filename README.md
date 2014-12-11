# [Flex](http://cbcb.umd.edu/~kross/flex/)

## Requirements:

- [Python 3.4.x](https://www.python.org/downloads/)
- [Muscle](http://www.drive5.com/muscle/)
- [blasr](https://github.com/PacificBiosciences/blasr)

## Usage:

**`find_mapped_reads.py`**

Returns a fasta file containing only reads within the specified region of the mapping.
```
python3 find_mapped_reads.py [fasta file with reads] [m5 mapping output from blasr] [start index] [end index] [output file name]
```
**Example**: `python3 find_mapped_reads.py reads.fa mapping.m5 100 5100 reads_100_5100.fa`

---
  
**`flex.py`**

Creates a consensus sequence from multiple sequence alignment output.
```
python3 flex.py [fasta file output from Muscle] [minimum number of non-gap nucleotides] [nucleotide percentage threshold]
```
**Example**: `python3 flex.py alignment.afa 20 0.65`

---

**`get_backbone_region.py`**

Computes percent identity for predicted nucleotides by comparing `flex.py` output and the backbone.
```
python3 get_backbone_region.py [fasta file with backbone] [fasta file with consensus sequence from flex.py] [backbone start position] [backbone end position]
```
**Example**: `python3 get_backbone_region.py backbone.fa consensus.fa 50 5150`
