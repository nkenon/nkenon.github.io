from PIL import Image
im = Image.open("maya_angelou.jpg")
pixels = im.getdata()
width, height = im.size
print(width)
print(height)
print(pixels)

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

newImage = []

for elem in pixels:
	total_RGB = elem[0]+elem[1]+elem[2]
	if total_RGB < 182:
		newImage.append(darkBlue)
	elif 182 < total_RGB < 364:
		newImage.append(red)
	elif 364 < total_RGB < 546:
		newImage.append(lightBlue)
	else:
		newImage.append(yellow)

colorimage = Image.new("RGB", (612, 380), "white")
		
colorimage.putdata(newImage)
colorimage.show()
colorimage.save("new.jpg")

