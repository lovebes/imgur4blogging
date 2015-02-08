#!/usr/bin/python
from imgurpython import ImgurClient
import argparse, sys, codecs, re, time
folder = ""     
journal = ""


#ADD THESE VALUES!
client_id = ""
client_secret = ""
access_token=""
refresh_token=""
client = ImgurClient(client_id, client_secret, access_token, refresh_token)

	


# ADD THE albumid!!
albumid = ""
def main():                                  

	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--folder', required=True)
	parser.add_argument('-j', '--journal', required=True)
	args = parser.parse_args()
	#print uploadtoalbum(albumid, "/home/seungjin/Downloads/tWPf0go.jpg")                         
	print "ready for action"
	journal = args.journal
	folder = args.folder
	jf = codecs.open(journal, "r", "utf-8")
	jfw = codecs.open(journal+"_replaced.txt","w", "utf-8")
	for line in jf:
		m = re.search('([-\w]+\.(?:JPG|jpg|gif|png))', line)
		parsedline = line
		if m:
			attempt = 0
			imgpath = folder+m.group(1)
			imgurl = uploadtoalbum(albumid, imgpath)
			while False: #imgurl == 'http://failedtoupload.jpg':
				attempt = attempt + 1
				print 'failed to upload ' + imgpath + ' will repeat..'
				print "upload attempt # "+str(attempt)+"\n"
				time.sleep(3)
				try: 
					client = ImgurClient(client_id, client_secret, access_token, refresh_token)
				except:
					print "didn't connect. will retry.."
				imgurl = uploadtoalbum(albumid, imgpath)
			parsedline = '<img src="'+imgurl+'" width="600"></img>'+'\n'
			print imgpath+' => '+parsedline
		else:
			print parsedline
		jfw.write(parsedline)
	
		


def usage():
	print "python imgurupload.py -f 'img folder' -j 'journaltextfile' "

def uploadtoalbum (album, image):
	#upload image
	#set to album
	try:
		image = client.upload_from_path(image, anon=False)
		
		return image['link']
	except:
		return 'http://failedtoupload.jpg'

if __name__ == "__main__":
    main()
