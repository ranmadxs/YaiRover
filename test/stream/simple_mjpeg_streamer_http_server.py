'''
Created on 13-09-2017

@author: instala
'''
#!/usr/bin/python
'''
    Author: Igor Maculan - n3wtron@gmail.com
    A Simple mjpg stream http server
'''
import cv2
from PIL import Image
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
import StringIO
import time
import threading
import json
capture=None
current_image = StringIO.StringIO()

def image_reader():
    global current_image, capture
    while True:
        rc,img = capture.read()
        if not rc:
            continue
        
        #data = pickle.dumps(image)
        ret, jpeg = cv2.imencode('.jpg', img)
        
        #cv2.putText(img, time.asctime(), (5,475), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,0))
        #imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        jpg = Image.fromarray(jpeg)
        del current_image
        current_image = StringIO.StringIO()
        jpg.save(current_image,'JPEG')
        time.sleep(0.1)
        
def motion_level(t1, t2):
    diff = cv2.absdiff(t1, t2)
    return sum([sum([y[0]+y[1]+y[2] for y in x]) for x in diff])

class CamHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global current_image
        if self.path.endswith('.mjpg'):
            self.send_response(200)
            self.send_header('Content-type','multipart/x-mixed-replace; boundary=--jpgboundary')
            self.end_headers()
            while True:
                try:
                    rc,img = capture.read()
                    if not rc:
                        continue
                    self.wfile.write("--jpgboundary")
                    self.send_header('Content-type','image/jpeg')
                    self.send_header('Content-length',str(current_image.len))
                    self.end_headers()
                    self.wfile.write(current_image.getvalue())
                    time.sleep(0.1)
                except KeyboardInterrupt:
                    break
            return
        if self.path.endswith('.html'):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write('''<!DOCTYPE HTML>
<html>
    <head>
        <title>Python Webcam</title>
        <meta charset="utf-8">
    </head>
    <body>
        <img src="cam.mjpg"/>
    </body>
</html>''')
            return
        if self.path.endswith('.json'):
            self.send_response(200)
            self.send_header('Content-type','application/json')
            ret = {}
           # ret['e'] = capture.get(cv2.cv.CV_CAP_PROP_EXPOSURE)
           # ret['c'] = capture.get(cv2.cv.CV_CAP_PROP_CONTRAST)
           # ret['b'] = capture.get(cv2.cv.CV_CAP_PROP_BRIGHTNESS)
            ret = json.dumps(ret)
            self.send_header('Content-length',str(len(ret)))
            self.end_headers()
            self.wfile.write(ret)
            return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def main():
    global capture, current_image
    capture = cv2.VideoCapture(0)
    capture.set(3,320)
    capture.set(4,240)
    capture.set(11,60)    
    #capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640); 
    #capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480);
    
    #print "CV_CAP_PROP_BRIGHTNESS",capture.get(cv2.cv.CV_CAP_PROP_BRIGHTNESS)
    #print "CV_CAP_PROP_CONTRAST",capture.get(cv2.cv.CV_CAP_PROP_CONTRAST)
    #print "CV_CAP_PROP_EXPOSURE",capture.get(cv2.cv.CV_CAP_PROP_EXPOSURE)
    
    img_t = threading.Thread(target = image_reader)
    img_t.setDaemon(True)
    
    global img
    try:
        img_t.start()
        print "Reading Camera"
        server = ThreadedHTTPServer(('',8080),CamHandler)
        print "Server Started"
        server.serve_forever()
    except KeyboardInterrupt:
        capture.release()
        server.socket.close()

if __name__ == '__main__':
    main()
