import requests

image_url = 'https://h6p9w2n9.rocketcdn.me/wp-content/uploads/2019/01/Schott.jpg'
# image_url = 'https://bespokephysiotherapy.co.nz/wp-content/uploads/2018/12/Regular-foam-roller-drink-bottles-1024x768.jpeg'
# image_url = 'https://runningwmiles-wpengine.netdna-ssl.com/wp-content/uploads/2019/06/bottle-4013294_1280.jpg'
path_to_save = './testImgDir/img_ex1.jpg'

# breakpoint() # i. breakpoint 는 파이썬 3.7부터 생긴건데, pdb 를 사용함.(pdb: 파이썬 기본내장된 파이썬 디버거.)
response = requests.get(image_url)
print('j) response.status_code:', response.status_code)
with open(path_to_save, 'wb') as handler:
    handler.write(response.content)