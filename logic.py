import requests#
from urllib.parse import quote #
class ImgAPI:

    def download_image(self,prompt): #api-ye promptu gönderen ve resmi indiren metod
        encoded_prompt=quote(prompt)
        url = f"https://image.pollinations.ai/image/{encoded_prompt}"
        response = requests.get(url)
        with open('generated_image.jpg', 'wb') as file:
            file.write(response.content)
        print('Resim indirildi!')
        return"generated_image.jpg"
if __name__ == "__main__":
    api = ImgAPI() #sınıfı kullanmak için nesne oluşturuyoruz
    api.download_image("1")#nese ile sınfın metoduna erişiyoruz