# SET_extractor

SET-extractor is a python program to identify and extract the SET domain sequence within protein sequences.

#USAGE

./SET_extractor.py infile(.faa) output



There are only two external dependencies that should be installed before using PcGs-finder:

• HMMER: biosequence analysis using profile hidden Markov model.
  http://hmmer.org 
• fasta_formatter.
   apt-get install fastx-toolkit
   
   
   #OUTPUTS
   - a bed file with the SET domain's coordinates.
   
   - SET sequence file.
