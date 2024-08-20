import requests

# Flask server'ınıza istek gönderin
response = requests.post("http://localhost:5000/build")

# APK dosyasını kaydedin
if response.status_code == 200:
    with open("app-debug.apk", "wb") as f:
        f.write(response.content)
    print("APK dosyası başarıyla indirildi.")
else:
    print(f"Derleme hatası: {response.json()}")
