#!/usr/bin/python 

#------------------- Parse collimator info (get_col_info.py) -------------------
#------------------- Python 3.5.2 :: Anaconda 4.1.1 (64-bit) -------------------
#------------------------ Author: Gabriella Azzopardi --------------------------

import os
import fnmatch
import numpy as np
import pandas as pd

#------------------------------ Global Variables -------------------------------

SETUP_DATE = '2018-06-16'
BP_YEAR = SETUP_DATE.split('-')[0]

SETUP_FOLDER  = 'Setup_' + SETUP_DATE
SETUP_PATH 	  = '/user/slops/data/LHC_DATA/OP_DATA/LHCCollimators/Setups/'
SETUP_FILE_B1 = 'Collimator_Setup_Sheet*_B1_ONGOING.tsv'
SETUP_FILE_B2 = 'Collimator_Setup_Sheet*_B2_ONGOING.tsv'

NAME_COL_SETUP  = 'Collimator Name'
ANGLE_COL_SETUP = 'Angle (rad)'

OUTPUT_FILE = '_col_info.csv'
NAME_COL    = 'collimator'
CENTRE_COL  = 'centre'
SIGMA_X_COL = 'sigma_x'
SIGMA_Y_COL = 'sigma_y'
ANGLE_COL   = 'angle'

BEAM_PROCESS = 'beam_processes/' + BP_YEAR + '/'
CENTRE_FILE  = '_centre.txt'
PARAM_FILE 	 = '_param.txt'
BEAM_MODE 	 = ['i', 'f', 's', 'p1', 'p2', 'p3']

COL_INFO = pd.DataFrame()

#------------------------------ Internal Functions -----------------------------

#Search for file in folder
# pattern - pattern to match filename 
# path 	  - path to directory to search for file
#Return filename, -1 if not found
def find_file(pattern, path):

	for name in os.listdir(path):
		if fnmatch.fnmatch(name, pattern):
			return path + '/' + name

	return -1

#Parse setup file for angle
# pattern - pattern to match filename 
# path 	  - path to directory to search for file
#Append data to global dataframe
def parse_setup(pattern, path):

	global COL_INFO

	#Find file
	full_path = find_file(pattern, path)

	if full_path == -1:
		print('File not found in folder:', SETUP_FOLDER)
		exit()

	#Read file
	with open(full_path) as f:
		lines = f.read().splitlines()
		lines = lines[3:]						#Remove first 3 lines

		del lines[lines.index('Horizontal')]
		del lines[lines.index('Vertical')]
		del lines[lines.index('Skew')]			#Remove single words

		temp = 'temp.txt'
		with open(temp, mode='wt', encoding='utf-8') as myfile:			myfile.write('\n'.join(lines))		#Create temporary file

		df = pd.read_csv(temp, sep='\t')		#Read and append
		COL_INFO = COL_INFO.append(df[[NAME_COL_SETUP, ANGLE_COL_SETUP]])

		os.remove('temp.txt')

#Parse beam process file for centre
# filepath - path to centres file
#Adds centres to global dataframe
def parse_centre(filepath):

	global COL_INFO; global NAME_COL; global CENTRE_COL

	#Add new column
	COL_INFO[CENTRE_COL] = ''

	with open(filepath) as f:
		lines = f.read().splitlines()

		#Use lines with '->'
		for line in lines:

			if '->' in line:

				name = line.split('/')[0]
				value = line.split('->')[1].lstrip()

				#Add to dataframe
				index = COL_INFO.loc[COL_INFO[NAME_COL] == name].index.tolist()[0]
				COL_INFO.set_value(index, CENTRE_COL, value)

#Parse beam process file for sigma_x and sigma_y
# filepath - path to param file
#Adds sigma_x and sigma_y to global dataframe
def parse_param(filepath):

	global COL_INFO; global NAME_COL; global SIGMA_X_COL; global SIGMA_Y_COL

	#Add new columns
	COL_INFO[SIGMA_X_COL] = ''
	COL_INFO[SIGMA_Y_COL] = ''

	with open(filepath) as f:
		lines = f.read().splitlines()
	
		#Use lines with '->'
		for line in lines:

			if '->' in line:

				col = ''

				#Determine column
				if (SIGMA_X_COL in line) and (not SIGMA_X_COL + 'p' in line):
					col = SIGMA_X_COL
				elif (SIGMA_Y_COL in line) and (not SIGMA_Y_COL + 'p' in line):
					col = SIGMA_Y_COL

				if not col == '':

					name = line.split('/')[0]
					value = line.split('->')[1].lstrip()

					#Add to dataframe
					index = COL_INFO.loc[COL_INFO[NAME_COL] == name].index.tolist()[0]
					COL_INFO.set_value(index, col, value)

#-------------------------------------------------------------------------------

#Create folder for collimator information
if not os.path.exists(BP_YEAR):
	os.makedirs(BP_YEAR)

#Parse Beam 1 & 2 setup files
parse_setup(SETUP_FILE_B1, SETUP_PATH + SETUP_FOLDER)
parse_setup(SETUP_FILE_B2, SETUP_PATH + SETUP_FOLDER)

COL_INFO.drop_duplicates(inplace=True)		#Drop duplicate values
COL_INFO.columns = [NAME_COL, ANGLE_COL]	#Set columns
COL_INFO = COL_INFO.sort_values([NAME_COL])	#Sort by collimator
COL_INFO.reset_index(inplace=True)	  		#Reset index
COL_INFO.drop('index', axis=1, inplace=True)

#Parse beam processes
for mode in BEAM_MODE:

	#Get centres and params
	parse_centre(BEAM_PROCESS + mode + CENTRE_FILE)
	parse_param(BEAM_PROCESS + mode + PARAM_FILE)
	
	COL_INFO.to_csv(BP_YEAR + '/' + mode + OUTPUT_FILE, index=False)	#Save to file

	#Drop columns
	COL_INFO.drop([CENTRE_COL, SIGMA_X_COL, SIGMA_Y_COL], axis=1, inplace=True)

#
#-------------------------------------------------------------------------------
#-------------------------------- Pre-requisits --------------------------------
#-------------------------------------------------------------------------------
#------/mcr/bin/ccm lhcop
#----- LHC Control/LHC Beam Control/LHC Trim (Set Categories)
#--- <Beam Process> -- COLLIMATORS
#
# Save COLL_BBCenter & COLL_BBParam (sigma_x, sigma_y)
#
# <Beam Processes>: RAMP-SQUEEZE-6.5TeV-3m-2016_V1 @0)[START]   	  - Injection
#					RAMP_PELP-SQUEEZE-6.5TeV-ATS-1m-2018_V3_V1 @0_[START] - Injection

#				    RAMP-SQUEEZE-6.5TeV-3m-2016_V1 @1210_)[END] 	  - Flattop/Adjust/Roman Pots
#					RAMP_PELP-SQUEEZE-6.5TeV-ATS-1m-2018_V3_V1 @1210_[END] - Flattop

#				    SQUEEZE-6.5TeV-3m-40cm-2016_V1 @1050_[END]  	  - Squeeze
#				    PHYSICS-6.5TeV-PreP-TOTEM-40cm-2016_V1 @150_[END] - Physics 1
#				    PHYSICS-6.5TeV-40cm-45s-2016_V1 @45_[END] 		  - Physics 2
#				    PHYSICS-6.5TeV-40cm-110s-2016_V1 @110_[END] 	  - Physics 3
#
# CHANGE <SETUP_DATE> ACCORDINGLY
#
#-------------------------------------------------------------------------------
#------------------------------- Post-requisits --------------------------------
#-------------------------------------------------------------------------------
#------/mcr/bin/ccm lhcop
#----- LHC Control/LHC Beam Control/LHC Trim (Set Categories)
#--- <Beam Process> -- COLLIMATORS -- TCLIA + TCLIB
#
# Save COLL_BBCenter & COLL_BBParam (sigma_x, sigma_y)
#
# <Beam Processes>: InjectionProtection_BP_2014 @0_[START] - Injection
#
