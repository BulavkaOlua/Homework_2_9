import requests

BASE_URL = 'http://127.0.0.1:8080'
image_path = 'chameleon.jpg'  # Замінити на існуюче зображення

# POST — завантаження зображення
with open(image_path, 'rb') as img:
    response = requests.post(f'{BASE_URL}/upload', files={'image': img})

if response.status_code == 201:
    image_url = response.json().get('url')
    print(f"[UPLOAD] Завантажено: {image_url}")

    # GET — перевірка, чи зображення доступне
    get_resp = requests.get(image_url)
    print(f"[GET] Статус: {get_resp.status_code}, Розмір: {len(get_resp.content)} байт")

    # DELETE — видалення зображення
    delete_resp = requests.delete(image_url)
    print(f"[DELETE] Статус: {delete_resp.status_code}, Відповідь: {delete_resp.json()}")
else:
    print("[ERROR] Завантаження не вдалося", response.status_code)
