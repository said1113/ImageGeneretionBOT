# Gerekli kütüphaneleri projeye ekliyoruz.
import discord  # Discord ile çalışmamızı sağlayan ana kütüphane.
import os
from discord.ext import commands  # Botumuza komutlar eklememizi kolaylaştıran bir sistem.
from config import TOKEN  # Botumuzun token'ını config.py dosyasından alıyoruz.
from logic import ImgAPI
# Botun mesajları görmesi ve onlara tepki vermesi için izin ayarları yapıyoruz.
intents = discord.Intents.default()  # Varsayılan izin ayarlarını alıyoruz.
intents.message_content = True  # Botun mesaj içeriklerini görmesine izin veriyoruz.
api = ImgAPI()
# Botumuzu başlatıyoruz.
bot = commands.Bot(command_prefix='$', intents=intents, help_command = None)
# $ işareti, komutlarımızın başına yazmamız gereken özel bir işarettir.
# Örneğin, bir komut çağırmak için "$hello" yazmamız gerekir..

# Bot Discord'a bağlandığında çalışacak bir kod yazıyoruz.
@bot.event  # Bu, belirli olaylar olduğunda çalışan kod parçalarını belirtmek için kullanılır.
async def on_ready():  # Bot Discord'a başarıyla bağlandığında çalışacak olan kod.
    print(f'{bot.user} olarak giriş yaptık')  # Konsolda, bot

# Bot için bir komut ekliyoruz.
@bot.command()  # Botun anlayacağı bir komut oluşturuyoruz.
async def hello(ctx):  # "hello" adında bir komut. Kullanıcı "$hello" yazdığında bu çalışır.
    await ctx.send(f'🎶 *La la laaa... Merhaba sana! Ben bir Botum!* 🎵')
    # Kullanıcının yazdığı yere (sohbet ekranına) mesaj gönderir:
    # "Merhaba [botun adı]! Ben bir botum!"

@bot.command()
async def help(ctx):
    info = """
    🎶*Dam diri dam dam...
    **Komutlar:**
    $hello - Botun size selam vermesini sağlar.
    $generate [prompt] - Verilen prompt - a göre bir resim oluşturur.*🎵
    """
    await ctx.send(info)

@bot.command()
async def generate(ctx, *, prompt:str):
    message = await ctx.send("*Görüntü üretiliyor...*")
    image = api.download_image(prompt)
    await message.delete()
    await ctx.send(file = discord.File(image))
    os.remove(image)


bot.run(TOKEN)  # Botumuzu çalıştırmak için token'ı kullanıyoruz. Bu, botun Discord'a bağlanmasını sağlar.)