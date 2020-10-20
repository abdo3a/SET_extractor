#!/usr/bin/env python3

#USAGE: ./SET_extractor.py infile(.faa) output
from Bio import SearchIO
from Bio import SeqIO
import os, sys, glob
import argparse
import pybedtools
from pybedtools import BedTool


infile = sys.argv[1]
out_dom = infile.replace('.faa','.dom')
bed= infile.replace('.faa','.bed')
out_bed = open(bed,'w')

if not os.path.exists(os.path.join('./', 'SET.hmm.h3i')):
    os.system('wget -v  https://github.com/abdo3a/SET_extractor/blob/main/SET.hmm?raw=true --content-disposition')
    os.system('hmmpress %s' % (os.path.join('./', 'SET.hmm')))
    print ('SET domain downloaded')
else:
    print ('SET exists')


#domain_search

os.system('hmmscan --domtblout %s --noali --cpu 30 ./SET.hmm %s'%(out_dom,infile))

#parse_output
for qresult in SearchIO.parse(out_dom, 'hmmscan3-domtab'):            
    query_id = qresult.id
    for i, hsp in enumerate(qresult.hsps, 1):
        s = hsp.env_start
        e = hsp.env_end
    out_bed.write(query_id+ '\t' + str(s) +'\t'+str(e)+'\n')
out_bed.close()
os.remove(out_dom)
#extract_sequences

a = BedTool(bed)
fasta = BedTool(infile)
a = a.sequence(fi=fasta,fo="output.fasta")

os.remove(infile+'.fai')
os.system('fasta_formatter -w 60 -i %s -o %s'%("output.fasta",sys.argv[2]))
os.remove("output.fasta")
for filename in glob.glob("./SET.*"):
    os.remove(filename)
