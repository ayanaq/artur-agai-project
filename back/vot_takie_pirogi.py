# from parsel import Selector
# import requests
#
#
# class NewsScraper:
#   headers = {
#     'authority': 'jut.su',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'referer': 'https://jut.su/',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
#   }
#   main_url = 'https://jut.su/oneepiece/'
#   link_xpath = '//div[@class="logo_b wrapper"]/a/@href'
#   plus_url = 'https://jut.su/'
#   xpath = '//div[@class="slicknav_menu"]/a/@href'
#
#   def parse_data(self):
#     html = requests.get(url=self.main_url, headers=self.headers).text
#     tree = Selector(text=html)
#     links = tree.xpath(self.link_xpath).extract()
#     images = tree.xpath(self.xpath).extract()
#     for link in links:
#       print(self.plus_url + link)
#     return links
#
#
# if __name__ == "__main__":
#   scraper = NewsScraper()
#   scraper.parse_data()

a = 20

@dp.message(Command("random_pic"))
async def send_random_pic(message: types.Message):
    images_list = ['1.webp', '2.webp', '3.webp', '4.webp', 'i.webp']
    images_dir = "images/"
    random_image = random.choice(images_list)
    image_path = os.path.join(images_dir, random_image)
    file = types.FSInputFile(image_path)
    await message.answer_photo(
        photo=file,
    )