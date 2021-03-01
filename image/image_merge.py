from PIL import Image

image = Image.new('RGBA', (512, 512))

face =Image.open('bin/face.png')
image.paste(face)

face2 = face.rotate(45)
image.paste(face2,(face.size[0],0))

face3 = face.getchannel('R')
image.paste(face3,(0,face.size[1]))

im_flipped = face.transpose(method=Image.FLIP_LEFT_RIGHT)
image.paste(im_flipped,face.size)

image.save('bin/test.png')
image.show()
