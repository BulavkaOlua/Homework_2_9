import requests
import os

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 15,
    'camera': 'navcam',
    'api_key': 'DEMO_KEY'
}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])

    if not photos:
        print("Фото не знайдено за вказаними параметрами.")
    else:
        for idx, photo in enumerate(photos):
            img_url = photo['img_src']
            img_data = requests.get(img_url).content
            file_name = f'mars_photo{idx+1}.jpg'

            with open(file_name, 'wb') as file:
                file.write(img_data)
                print(f"Збережено {file_name}")
else:
    print(f"Помилка запиту: {response.status_code}")
