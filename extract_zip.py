#note this obviously only works for zipped files

from zipfile import ZipFile

zip_file = "Homo_sapiens.GRCh37.dna.primary_assembly.fa.zip"

#opening zip file in read mode
with ZipFile (zip_file, 'r') as zip:
	#extract all the files
	zip.extractall()
	print('Extraction Done!')
