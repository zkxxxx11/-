from PIL import Image

image2 = image2=Image.open('C:/Users/Administrator/Desktop/py/selenium/bi/b站滑动验证码/captcha_down.png')
image1 = image1=Image.open('C:/Users/Administrator/Desktop/py/selenium/bi/b站滑动验证码/captcha_up.png')
print('size:',image1.size)
left=0
threshold=60
for x in range(left,image1.size[0]):
    for y in range(image1.size[1]):
        pixel1=image1.load()[x,y]
        pixel2=image2.load()[x,y]
        
        r=pixel1[0]-pixel2[0]
        g=pixel1[1]-pixel2[1]
        b=pixel1[2]-pixel2[2]
        if not (abs(r)<threshold and abs(g)<threshold and abs(b)<threshold):
            print(x)
            break
            '''return x-7误差7'''
            
            

            
