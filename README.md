# imgur4blogging
The script uses imgurpython to make travel-blogging of many photos easy. 

Due to my last year in medical school's requirement for global health electives, I'm currently in India. Exotic! And also many pictures were taken, which brought an interesting problem of the need to upload many pictures embedded in many blog posts. 

Doing that by hand would be .. still be feasible, but sometimes the Internet at my particular site can be flaky and wouldn't work, which complicated and necessitated (?) the repetition of uploading.

As with any problems that remotely start being repetitive, I mulled if I can code a solution, while sipping my delicious chai with the delicious poha or anda bhurji. 

I concluded it's possible, and it would actually save me a lot of time. And it did. 

So what below script can get you: 

You write a text file, and when you want to insert photos you just write the filename of that photo in its separate line. Save. 

Then, when you run the script, it will upload the file, replace the filename with a <img src="XXX" width="600"></img> tag, and save it to another textfile. 

After which you can copy/paste that text into your blog, in the mode where you can put HTML codes.

Here's how to get the script up and running:

 

1) List all the filenames of the pictures you want to post in your blog post textfile. I use Linux, and so naturally I open up a terminal in that photo folder, do a 'ls -l', and copy the list of photos. For windows, I guess I can do 'dir' in that folder with the photos.

2) Download Geany, the best text editor ever. Copy/Paste the list of photos. Press the control key while selecting only the part of the text column that has the filenames (eg 'IMG_2452.JPG') Be amazed by how pressing the Control key can do vertical selection of text. Now move it around, delete all the unnecessary text file.

3) Read https://github.com/Imgur/imgurpython and get all that is required (python, imgurpython library, authentication tokens ). If you don't know how, look it up as it is not the scope of this blog post.

4) Download my script: 

 - and enter your personal client_id, client_secret, access_token, and refresh_token. 

5) In imgur, log in, and make an album where you want the script to upload all the travel photos. Get the id # of the album folder  (eg. m8F3b )

 

6) Use the script as such: go to commandline:

    type: python imgurupload.py -f /path/to/folder/of/photo/ -j /path/to/the/textfile.txt

7) Watch it go!, it will finish and create:  /path/to/folder/of/photo/ -j /path/to/the/textfile.txt_replaced.txt

8) Check if some of the pictures are converted to 'failedtoupload.jpg' <- which is the case when it fails to upload. In that case, you just run the command again if you want.
