from PIL import Image, ImageFilter
import requests
from getpass import getpass

image_1 = Image.open('774757691.jpg')
print(image_1.format, image_1.size, image_1.mode)
image_1_1 = image_1.convert('L')
ch_im_1 = image_1.resize((900, 540))
ch_2 = (ch_im_1.filter(ImageFilter.DETAIL))
ch_2.show()
print(ch_2.getbands())
ch_2.save('Новый кот-программист.png')

req = requests.get('http://dzen.ru/news/region/nizhny_novgorod')
print(req)
print(req.headers)
query = {'order': 'popular'}
req_2 = requests.get('http://dzen.ru/news/region/nizhny_novgorod', params=query)
print(req_2.url)
req_3 = requests.get('https://api.github.com/user', auth=('Esenka1993', getpass()))
print(req_3)

