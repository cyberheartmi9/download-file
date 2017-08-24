import urllib.request
from tqdm import tqdm
from optparse import OptionParser

parse=OptionParser(""" 

-u / --url : file link
-d / --dir : directory

example:
./books.py -u http://127.0.0.1/linux.pdf 
./books.py --url http://127.0.0.1/linux.pdf --dir /home



	""")

parse.add_option("-u","--url",dest="url",type="string",help="url to download file")
parse.add_option("-d","--dir",dest="dir",type="string",help="please path to downlaod file")
(opt,args)=parse.parse_args()

if opt.url==None:
	print(parse.usage)
	exit(0)
else:
	url=str(opt.url)
	if opt.dir!=None:
		D=str(opt.dir)
		fn=url.split("/")[-1]
		opfile=open(D+" "+fn,"wb")
	else:
		opfile=open(fn,"wb")
	openurl=urllib.request.urlopen(url)
	block=2048
	file_size=int(openurl.headers["Content-Length"])
	for i in tqdm(range(file_size)):
		buff=openurl.read(block)
		i+=block
		opfile.write(buff)
	opfile.close()
