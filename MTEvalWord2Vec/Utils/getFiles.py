import os

def All_FileList(CommanPath):
	'''
		Use this to find names of files present in a directory
		input: Path to the director
		output: List contaning all the file names.
	'''
	AllFolderList=os.listdir(CommanPath)
	AllFolderList=[CommanPath+i for i in AllFolderList]
	return AllFolderList
