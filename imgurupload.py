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
        m = re.search('(addthumb)*([-\w]+\.(?:JPG|jpg|gif|png))', line)
        # m.group(1) should have string 'addthumb' which means 'please make thumbnail and <img> that
        # thumbnails will resize to 600 width pics, uploaded, and image will be <a href="real"<img src="thumbail"  ~ed.
        parsedline = line
        if m:
            imgpath = folder+m.group(2)
            #m.group(2) would now have the strings after 'addthumb' modifier, ie the filenames for pics
            thumbwidth = 600
            
            attempt = 0
            if m.group(1) == 'addthumb':
                #check image
                im=Image.open(imgpath) #(width,height) tuple
                width_org, height_org = im.size
                thumbheight = int(height_org * thumbwidth / width_org)
            
                if  width_org > 600: #only then you would need to make a thumbnail pic
                    #resize the image and save it with 'thumb' prefix
                    newimg = im.resize((thumbwidth, thumbheight), Image.ANTIALIAS)
                    resizepath = folder+'thumb_'+m.group(2)
                    newimg.save(resizepath)
                    print("resized file saved as %s" % resizepath)
                    thumburl = uploadtoalbum(albumid, resizepath)
                    
            
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
                if m.group(1) == 'addthumb':
                    thumburl = uploadtoalbum(albumid, resizepath)
            
            if m.group(1) == 'addthumb':
                parsedline = '<a href="'+imgurl+'" target="new"><img src="'+thumburl+'" width="600"></img></a>'+'\n'
                print imgpath
                print ', '+resizepath+' => '+parsedline
            else:
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
