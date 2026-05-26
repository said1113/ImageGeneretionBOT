# Gerekli kütüphaneleri projeye ekliyoruz.
import discord  # Discord ile çalışmamızı sağlayan ana kütüphane.
from discord.ext import commands  # Botumuza komutlar eklememizi kolaylaştıran bir sistem.
from config import TOKEN  # Botumuzun token'ını config.py dosyasından alıyoruz.
from logic import ImgAPI
# Botun mesajları görmesi ve onlara tepki vermesi için izin ayarları yapıyoruz.
intents = discord.Intents.default()  # Varsayılan izin ayarlarını alıyoruz.
intents.message_content = True  # Botun mesaj içeriklerini görmesine izin veriyoruz.
api = ImgAPI()
# Botumuzu başlatıyoruz.
bot = commands.Bot(command_prefix='$', intents=intents)
# $ işareti, komutlarımızın başına yazmamız gereken özel bir işarettir.
# Örneğin, bir komut çağırmak için "$hello" yazmamız gerekir..

# Bot Discord'a bağlandığında çalışacak bir kod yazıyoruz.
@bot.event  # Bu, belirli olaylar olduğunda çalışan kod parçalarını belirtmek için kullanılır.
async def on_ready():  # Bot Discord'a başarıyla bağlandığında çalışacak olan kod.
    print(f'{bot.user} olarak giriş yaptık')  # Konsolda, bot

# Bot için bir komut ekliyoruz.
@bot.command()  # Botun anlayacağı bir komut oluşturuyoruz.
async def hello(ctx):  # "hello" adında bir komut. Kullanıcı "$hello" yazdığında bu çalışır.
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')
    # Kullanıcının yazdığı yere (sohbet ekranına) mesaj gönderir:
    # "Merhaba [botun adı]! Ben bir botum!"

@bot.command()
async def generate(ctx, *, prompt:str):
    image = api.download_image(prompt)
    await ctx.send(file = discord.File(image))
bot.run(TOKEN)  # Botumuzu çalıştırmak için token'ı kullanıyoruz. Bu, botun Discord'a bağlanmasını sağlar.)