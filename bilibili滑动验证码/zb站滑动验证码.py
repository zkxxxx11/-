import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

def get_screenshot(driver):
    """
    获取网页截图
    :return: 截图对象
    """
    screenshot = driver.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    return screenshot
def cut_image(driver,name):
    driver.save_screenshot('all.png')
    #image=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]')
    a= driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]/div/canvas[1]')
    print(a.location)
    print(a.size)
    left=a.location['x']
    top=a.location['y']
    right=left+a.size['width']
    buttom=top+a.size['height']
    print('####################')
    print(a.size['width'],a.size['height'])
    print(left,top,right,buttom)
    print('###################')
    image_obj=Image.open('all.png')
    img=image_obj.crop((left,top,right,buttom))
    img.save(name)
    
def get_image1(driver):
    time.sleep(2)
    #js_code=var x =document.getElementsByClassName("geetest_canvas_slice geetest_absolute").style.display="none";)
    
    #driver.execute_script(js_code)
    ele=driver.find_elements_by_tag_name('canvas')
    
    '''setAttribute(ele[2],'style','display: none;')'''
#set
    driver.execute_script("arguments[0].setAttribute (arguments[1],arguments[2])",ele[2],'style','display: none;')
    image=cut_image(driver,'que.png')
#remove
    driver.execute_script("arguments[0].removeAttribute(arguments[1])",ele[3],'style')
    image=cut_image(driver,'quan.png')
    time.sleep(0.5)
#remove
    driver.execute_script("arguments[0].removeAttribute(arguments[1])",ele[2], 'style')
    time.sleep(0.5)
#set
    driver.execute_script("arguments[0].setAttribute (arguments[1],arguments[2])",ele[3], 'style', 'display: none;')

def get_gap(image1,image2):
    print('size',image1.size)
    left=0   
    for i in range(left,image1.size[0]):
        for j in range(image1.size[1]):
            if not is_pixel_equal(image1,image2,i,j):
                left=i
                print('left',left)
                return left
def is_pixel_equal(image1,image2,x,y):
    pixel1=image1.load()[x,y]#que'''
    pixel2=image2.load()[x,y]#quan'''
    threshold=60
    if abs(pixel1[0]-pixel2[0])<threshold and abs(pixel1[1]-pixel2[1])<threshold and abs(pixel1[2]-pixel2[2])<threshold:
        return True
    else:
        print(pixel1,pixel2)
    
        return False


def get_move(gap):
    v0=0
    
    t=0.3
    s=0
    v_list=[1,2,3,4]
    r=[]
    mid=gap/5*3
    while s<gap:
        if s<mid:
            a=v_list[random.randint(0,3)]
        else:
            a=-v_list[random.randint(0,3)]
        v=v0
        s1=v0*t+0.5*a*t*t
        s1=round(s1)
        
      
        v0=v+a*t
        r.append(s1)
        s+=s1
        print(r)
        
    return(r)
def move_to_gap(driver,slider,track):
    
    ActionChains(driver).click_and_hold(slider).perform()
    for x in track:
        ActionChains(driver).move_by_offset(xoffset=x,yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(driver).release().perform()
def main():
    driver=webdriver.Chrome()
    url='https://passport.bilibili.com/login?gourl=https://space.bilibili.com'
    
    
    driver.get(url)
    driverwait=WebDriverWait(driver,20)
    
    driver.find_element_by_xpath('//*[@id="login-username"]').send_keys('123')
    driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys('nnnn')
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()
    time.sleep(1)
    get_image1(driver)
    image1=Image.open('que.png')
    image2=Image.open('quan.png')
    gap=get_gap(image1,image2)
    print(gap)
    move_list=get_move(gap)
    print(move_list)
    
    slider = driverwait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))    
    
    
    move_to_gap(driver,slider,move_list)
    


main()
