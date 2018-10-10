import subprocess,time,os
try :
	os.system('cls')
	print("Updating pip\n")
	os.system("python -m pip install --upgrade pip")
	packages = ['pyqt5', 'pyqt5-tools', 'pafy', 'youtube-dl']
	def install(name):
		print("\n\ninstalling {}\n\n".format(name))
		subprocess.call(['pip', 'install', name])

	for i in packages:
		install(i)
	input("\nFinished Installing . Enter To Exit")



except Exception as e:
	print("Error:\n", e)
	input("Enter To Exit")