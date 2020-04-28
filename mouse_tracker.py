from pynput.mouse import Listener
from pynput.mouse import Button
import logging
import json_log_formatter
import json
import time,argparse
data={}
data['coordinates']=[]
#logging.basicConfig(filename=("mouse_log.txt"), level=logging.DEBUG, format='%(message)s')
#def on_move(x, y):
#	logger.info(msg={'X':x,'Y':y})

def timeInterval(data):
	start=0
	index=0
	for n in range(len(data["coordinates"])):
		if n ==0:
			start=data["coordinates"][n]["time"]
			data["coordinates"][n]["time"]=0
		else:
			interval=data["coordinates"][n]["time"]- start
			start=data["coordinates"][n]["time"]
			data["coordinates"][n]["time"]=interval

def on_click(x, y, button, pressed):
	if pressed:
		if button==Button.left:
			click='left'
		else:
			click='right'
		data['coordinates'].append({'X':x,'Y':y,'Button':click,'time':time.time()})
        #logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
	global data
	global filename
	try:
		with open(filename, 'w') as outfile:
			timeInterval(data)
			json.dump(data, outfile)
	except Exception as e:
		print(e)

	data['coordinates']=[]
	print("Mouse Clicks Logged")
	return False
	#logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This script logs your clicks\nIntructions: Scroll up or down to complete logging.')
	filename=parser.add_argument('--output', metavar='-o', type=str,
	                   help='filename for output')
	args = parser.parse_args()
	filename=args.output
	if filename==None:
		filename="mouse_click_log.json"
	else:
		filename = filename.replace(".","")+".json" 
	print("Logging clicks to "+ str(filename)+",\nScroll up or down to complete logging.")

	with Listener( on_click=on_click,on_scroll=on_scroll) as listener:
		listener.join()
#try catch for receiving filename 