import time
import pandas as pd


from bs4 import BeautifulSoup
from selenium import webdriver

data_list = ['2M261602SY', '2M271802MD', '2M271802MN', '2M271802MH']  
j=0
while j<len(data_list):
    driver = webdriver.Chrome('/home/ongraph/chromedriver')  
    driver.get('https://support.hpe.com/hpsc/wc/public/addRows')
    current_data_list = data_list[j:j+4]
    j += 4

    for i in range(len(current_data_list)):
        
        id = 'serialNumber' + str(i)

        search_box = driver.find_element_by_id(id)
        search_box.clear()
        search_box.send_keys(current_data_list[i])
    search_box.submit()
    
    for j in range(len(current_data_list)):
        table = driver.find_elements_by_xpath('//*[@id="generate_table_2M271802MD"]/table/tbody/tr')
        
    data_dict = {'serial no.' : [1],
                 'Product Description' : [1],
                 'type' : [3],
                 'Identifier' : [4],
                 'Service Type' : [5,5],
                 'Start Date' : [6,7],
                 'End Date' : [8,8],
                 'Status' : [8,9]
        }

    print(len(table))
    for x in table:
        print(x.text)

    




# if url[-1] == 'displayCaptcha':
#         img_name_counter += 1
#         img_name = 'images/img{}.png'.format(img_name_counter)
#         file = open(img_name, 'wb')
#         #identify image to be captured
#         l = driver.find_element_by_xpath('//*[@alt="Captcha Challenge"]')
#         #write file
#         file.write(l.screenshot_as_png)
        
#         print("image saved")
#         print("handle captcha")
#         time.sleep(10)