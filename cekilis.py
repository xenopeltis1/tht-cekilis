import requests
from lxml import html
import random

link = 'https://www.turkhackteam.org/tim-ekip-alimlari/1894534-moderasyon-stajyer-asistan-alimlari.html' #input('Konu Linkini Giriver: ')

a  =link.split('/')[-1].split('-')[0]
r = requests.get(f'https://www.turkhackteam.org/misc.php?do=whoposted&t={a}')

tekilp = requests.get(link)
tekil = html.fromstring(tekilp.content)
tekil = tekil.xpath('body/div[@id="posts"]/div/div/div[2]/div[@style="padding:0px 0px 0px 0px"][1]/div[@class="postbit-content d-flex"]/div[2]/div/div[1]/div/div[6]/a/@href')
tekil = tekil[0]

post = requests.get(f'https://www.turkhackteam.org/misc.php?do=whoposted&t={a}')
thankseds = requests.get(tekil)

post = html.fromstring(post.content)
thankseds = html.fromstring(thankseds.content)

thankseds = thankseds.xpath('//*[@class="dbtech-ent-count"]/div[@class="thankseds"]/a/span/text()')

post1 = post.xpath('body[@onload="self.focus()"]/table[@class="tborder"]/*/td[@class="alt1"]/a/text()')
post2 = post.xpath('body[@onload="self.focus()"]/table[@class="tborder"]/*/td[@class="alt2"]/a/text()')
post1 = post1+post2
sec = []

for _ in thankseds:
    if _ in post1:
        sec.append(_)

print(sec[random.randrange((len(sec)))])
