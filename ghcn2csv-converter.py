#!/usr/bin/env python

# This scripts converts data from GHCN (Global Historical Climatology Network)
# into the CSV format.
# Source: ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/v3/
# Author: Remy SAISSY <remy.saissy@gmail.com>
# Licence: GPL



import sys
import argparse


def convert_ghcn_data(input, output):
	output.write('id,year,element,value1,dmflag1,qcflag1,dsflag1,value2,dmflag2,qcflag2,dsflag2,value3,dmflag3,qcflag3,dsflag3,value4,dmflag4,qcflag4,dsflag4,value5,dmflag5,qcflag5,dsflag5,value6,dmflag6,qcflag6,dsflag6,value7,dmflag7,qcflag7,dsflag7,value8,dmflag8,qcflag8,dsflag8,value9,dmflag9,qcflag9,dsflag9,value10,dmflag10,qcflag10,dsflag10,value11,dmflag11,qcflag11,dsflag11,value12,dmflag12,qcflag12,dsflag12\n')
	while True:
		line  = input.readline()
		if line == '':
			break
		_id = line[0:11].strip()
		year = line[11:15].strip()
		element = line[15:19].strip()
		output_line = '{},{},{}'.format(_id, year, element)
		for idx in range(12):
			base_idx = 19 + idx * 8
			value = line[base_idx:base_idx+5].strip()
			dmflag = line[base_idx+5:base_idx+6].strip()
			qcflag = line[base_idx+6:base_idx+7].strip()
			dsflag = line[base_idx+7:base_idx+8].strip()
			output_line += ',{},{},{},{}'.format(value,dmflag,qcflag,dsflag)
		output_line += '\n'
		output.write(output_line)

def convert_ghcn_metadata(input, output):
	output.write('id,latitude,longitude,stnelev,name,grelev,popcls,popsiz,topo,stveg,stloc,ocndis,airstn,towndis,grveg,popcss\n')
	while True:
		line  = input.readline()
		if line == '':
			break
		_id = line[0:11].strip()
		latitude = line[12:20].strip()
		longitude = line[21:30].strip()
		stnelev = line[31:37].strip()
		name = line[38:68].strip()
		grelev = line[69:73].strip()
		popcls = line[73:74].strip()
		popsiz = line[75:79].strip()
		topo = line[79:81].strip()
		stveg = line[81:83].strip()
		stloc = line[83:85].strip()
		ocndis = line[85:87].strip()
		airstn = line[87:88].strip()
		towndis = line[88:90].strip()
		grveg = line[90:106].strip()
		popcss = line[106:107].strip()
		output.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(_id,latitude,longitude,stnelev,name,grelev,popcls,popsiz,topo,stveg,stloc,ocndis,airstn,towndis,grveg,popcss))

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Convert a GHCN file into a CSV file.')
	parser.add_argument('-f', '--format', nargs=1, choices=['metadata', 'data'], required=True, help='Indicates the format of the input data. Can be either metadata or data.')
	parser.add_argument('-i', '--input', nargs=1, type=argparse.FileType('r'), required=True, help='The input file.')
	parser.add_argument('-o', '--output', nargs=1, type=argparse.FileType('w'), required=True, help='The output file.')
	args = parser.parse_args()
	locals()['convert_ghcn_{}'.format(args.format[0])](args.input[0], args.output[0])
