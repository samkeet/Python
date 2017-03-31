import os
from os.path import isile
import sys

class osScripts():


	def __init__(self, file_path):
		self.working_directory = os.chdir(file_path)
		self.dir_list = [val for val in self.dir_list if isdir(val)]
		self.file_list = [val for val in self.dir_list if isfile(val)]

	def cleanfileNames(self):



	def directorizeFiles(self):
		for each_file in self.file_list:
			os.rename(each_file, each_file.replace('.'))


if __name__ == '__main__':
	workBot = osScripts(sys.args[1])