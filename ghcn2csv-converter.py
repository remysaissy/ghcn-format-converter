#!/usr/bin/env python

# This scripts converts data from GHCN (Global Historical Climatology Network)
# into the CSV format.
# Source: ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/v3/
# Author: Remy SAISSY <remy.saissy@gmail.com>
# Licence: GPL

import sys
import argparse
import csv

def convert_ghcn_monthly(input, output):
	csv_output = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
	# Write the header
	row = ['id','year','element','value1','dmflag1','qcflag1','dsflag1','value2','dmflag2','qcflag2','dsflag2','value3','dmflag3','qcflag3','dsflag3','value4','dmflag4','qcflag4','dsflag4','value5','dmflag5','qcflag5','dsflag5','value6','dmflag6','qcflag6','dsflag6','value7','dmflag7','qcflag7','dsflag7','value8','dmflag8','qcflag8','dsflag8','value9','dmflag9','qcflag9','dsflag9','value10','dmflag10','qcflag10','dsflag10','value11','dmflag11','qcflag11','dsflag11','value12','dmflag12','qcflag12','dsflag12']
	csv_output.writerow(row)
	while True:
		line  = input.readline()
		if line == '':
			break
		row = []
		v = line[0:11].strip()
		if v != '':
			v = int(v)
		row.append(v) # id
		v = line[11:15].strip()
		if v != '':
			v = int(v)
		row.append(v) # year
		row.append(line[15:19].strip()) # element
		for idx in range(12):
			base_idx = 19 + idx * 8
			v = line[base_idx:base_idx+5].strip()
			if v != '':
				v = int(v)
			row.append(v) # valueN
			row.append(line[base_idx+5:base_idx+6].strip()) # dmflagN
			row.append(line[base_idx+6:base_idx+7].strip()) # qcflagN
			row.append(line[base_idx+7:base_idx+8].strip()) # dsflagN
		csv_output.writerow(row)
		
def convert_ghcn_daily(input, output):
    csv_output = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
	# Write the header
    row = ['id','year','month','element']
    for i in range (1,32):
      	i = str(i)    
	row.append('value' + i)
	row.append('mflag' + i)
	row.append('qflag' + i)
	row.append('sflag' + i)
    
    csv_output.writerow(row)
    while True:
        line  = input.readline()
        if line == '':
           	break
        row = []
	v = line[0:11].strip()
	if v != '':
		v = str(v)
	row.append(v) # id
	v = line[11:15].strip()
	if v != '':
		v = int(v)
	row.append(v) # year
	v = line[15:17].strip()
   	if v != '':
		v = int(v)
	row.append(v) # month
	row.append(line[17:21].strip()) # element
	for idx in range(31):
		base_idx = 21 + idx * 8
		v = line[base_idx:base_idx+5].strip()
           	if v != '':
			v = int(v)
		row.append(v) # valueN
		row.append(line[base_idx+5:base_idx+6].strip()) # dmflagN
		row.append(line[base_idx+6:base_idx+7].strip()) # qcflagN
		row.append(line[base_idx+7:base_idx+8].strip()) # dsflagN
	csv_output.writerow(row)
    output.close()

def convert_ghcn_metadata(input, output):
	csv_output = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
	# Write the header
	row = ['id','latitude','longitude','stnelev','name','grelev','popcls','popsiz','topo','stveg','stloc','ocndis','airstn','towndis','grveg','popcss']
	csv_output.writerow(row)
	while True:
		line  = input.readline()
		if line == '':
			break
		row = []
		v = line[0:11].strip()
		if v != '':
			v = int(v)
		row.append(v) # id
		row.append(line[12:20].strip()) # latitude
		row.append(line[21:30].strip()) # longitude
		row.append(line[31:37].strip()) # stnelev
		row.append(line[38:68].strip()) # name
		v = line[69:73].strip()
		if v != '':
			v = int(v)
		row.append(v) # grelev
		row.append(line[73:74].strip()) # popcls
		v = line[75:79].strip()
		if v != '':
			v = int(v)
		row.append(v) # popsiz
		row.append(line[79:81].strip()) # topo
		row.append(line[81:83].strip()) # stveg
		row.append(line[83:85].strip()) # stloc
		v = line[85:87].strip()
		if v != '':
			v = int(v)
		row.append(v) # ocndis
		row.append(line[87:88].strip()) # airstn
		v = line[88:90].strip()
		if v != '':
			v = int(v)
		row.append(v) # towndis
		row.append(line[90:106].strip()) # grveg
		row.append(line[106:107].strip()) # popcss
		csv_output.writerow(row)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Convert a GHCN file into a CSV file.')
	parser.add_argument('-f', '--format', nargs=1, choices=['metadata', 'monthly', 'daily'], required=True, help='Indicates the format of the input data. Can be either GHCN monthly metadata, monthly data or daily data.')
	parser.add_argument('-i', '--input', nargs=1, type=argparse.FileType('r'), required=True, help='The input file.')
	parser.add_argument('-o', '--output', nargs=1, type=argparse.FileType('wb'), required=True, help='The output file.')
	args = parser.parse_args()
	locals()['convert_ghcn_{}'.format(args.format[0])](args.input[0], args.output[0])
