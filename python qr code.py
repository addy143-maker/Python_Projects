import qrcode

data = ( " Hello my name is JEEL PARADAVA ")

img = qrcode.make(data)

img.save('/Users/jeel/myqr.png')

       