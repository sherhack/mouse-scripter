from pynput.mouse import Button, Controller
import time
import argparse
import json

def main(filename,loop):
	mouse = Controller()
	with open(filename) as json_file:
		data = json.load(json_file)
		while loop>0:
			for p in data['coordinates']:
				mouse.position = (p['X'], p['Y'])
				if p['Button']=='left':
					mouse.press(Button.left)
					mouse.release(Button.left)
				else:
					mouse.press(Button.right)
					mouse.release(Button.right)

				time.sleep(p["time"])
			loop-=1
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This script copies your clicks from input file')
	filename=parser.add_argument('--filename',"-f", metavar='[filename]', type=str,default="mouse_click_log.json",
	                   help='filename for input')
	loop=parser.add_argument('--loop',"-l", metavar='[loop]', type=int,default=1,
	                   help='Number of times to recreate clicks')

	args = parser.parse_args()
	filename=args.filename
	loop=args.loop
	print("Reading clicks from "+ str(filename) + ": ["+ str(loop) +"] times.")
	main(filename,loop)

