import qrcode

#execute the code on any compiler and you will find the image saved. From there scan the qrcode. 

image = qrcode.make("Insert The Text You Want")
image.save("Give the image a name")
