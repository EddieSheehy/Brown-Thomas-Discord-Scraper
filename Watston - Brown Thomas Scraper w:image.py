import requests
import discord
import unicodedata
from discord.ext import commands
import urllib
import re
import time
from bs4 import BeautifulSoup



n = 0

client = commands.Bot(command_prefix =  '!')

@client.event
async def on_ready():
    print("Bot Ready")


@client.command(pass_context=True)
async def bt(ctx, url):
    

    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    embed = discord.Embed(color=0x00ff00)
    embed.title = "test"
    total_items = soup.find('div', class_='pagination')
    total_items2= total_items.find('span', attrs={'class':'pag-total-items-show'})
    total_items2 = total_items2.text[:-9]
    s = total_items2
    s = s.replace(',','')
    print(s)
    print(url+'?&sz='+s)
    result = requests.get(url+"?&sz="+s)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    
    for image in soup.find_all('li', class_='grid-tile js-product-grid-tile'):
        product_image = image.div.div.a.picture.source.get("data-srcset")
        itempriceset = image.find('span', attrs={'class':'product-sales-price'})
        item_price = itempriceset.text
        item_brand2 = image.find('span', attrs={'class':'product-brand'})
        item_name2 = image.find('span', attrs={'class':'product-name name-link'})
        item_brand = item_brand2.text
        item_name = item_name2.text
        n = 0
        n + 1
        time.sleep(2)
        print(item_brand + item_name + item_price + product_image)
        embed = discord.Embed(
                title = 'Brand',
                description = item_brand,
                colour = discord.Colour.blurple()
            )
        embed.set_author(name='Brown Thomas Scraper')
        embed.add_field(name='Product Name', value=item_name, inline=False)
        embed.add_field(name='Price', value=item_price, inline=False)
        embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png'
),
        embed.set_thumbnail(url=product_image)
        await ctx.send(embed=embed)

client.run('NzExMjU2NjU4NTkyMTM3MjM3.XsAXYQ.vT4sEn__v3iGKKYaqdsyz3R9tlo')