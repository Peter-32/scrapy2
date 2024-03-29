import os
import re
import scrapy
import shutil
import scrapy
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess

try:
    shutil.rmtree("html")
except:
    pass
os.mkdir("html")

if not os.path.exists("../../data/processed"):
    os.mkdir("../../data/processed")

# Customize Spiders
class ExplorationSpider(scrapy.Spider):
    name = "exploration"
    start_urls = ["https://wiki.guildwars.com/wiki/Explorable_area"]

    def parse(self, response):
        next_pages = response.css('a::attr(href)').getall()
        next_pages = next_pages[next_pages.index('/wiki/Battle_Isles'):next_pages.index('/wiki/Verdant_Cascades')+1]
        next_pages = [x for x in next_pages if x not in ["Charr Homelands", "Depths of Tyria", "Far Shiverpeaks", "Tarnished Coast", "Istan", "Kourna", "Vabbi", "The Desolation", "Realm of Torment", "Shing Jea Island", "Kaineng City", "Echovald Forest", "The Jade Sea", "Ascalon", "Northern Shiverpeaks", "Kryta", "Maguuma Jungle", "Crystal Desert", "Southern Shiverpeaks", "Ring of Fire Islands", "The Mists", "Battle Isles", "The Mists", "Ascalon"]]

        next_pages = ["https://wiki.guildwars.com" + x for x in next_pages]
        next_pages = list(set(next_pages))
        for href in next_pages:
            yield response.follow(href, self.parse_new_page)

    def parse_new_page(self, response):
        page = response.url.split("/")[-2]
        filename = 'html/{}_{}.html'.format(self.name, page)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}_{}.html".format(self.name, page, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

class PropheciesSpider(scrapy.Spider):
    name = "prophecies"
    start_urls = ['https://wiki.guildwars.com/wiki/List_of_Prophecies_missions_and_primary_quests']

    def parse(self, response):
        next_pages = response.css('a::attr(href)').getall()
        next_pages = next_pages[next_pages.index('/wiki/The_Great_Northern_Wall'):next_pages.index('/wiki/The_Titan_Source')+1]
        next_pages = [x for x in next_pages if "/wiki/" in x]

        next_pages = ["https://wiki.guildwars.com" + x for x in next_pages]
        next_pages = list(set(next_pages))
        for href in next_pages:
            yield response.follow(href, self.parse_new_page)

    def parse_new_page(self, response):
        page = response.url.split("/")[-2]
        filename = 'html/{}_{}.html'.format(self.name, page)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}_{}.html".format(self.name, page, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

class FactionsSpider(scrapy.Spider):
    name = "factions"
    start_urls = ['https://wiki.guildwars.com/wiki/List_of_Factions_missions_and_primary_quests']

    def parse(self, response):
        next_pages = response.css('a::attr(href)').getall()
        next_pages = next_pages[next_pages.index('/wiki/Minister_Cho%27s_Estate'):next_pages.index('/wiki/The_Deep')+1]
        next_pages = [x for x in next_pages if "/wiki/" in x]

        next_pages = ["https://wiki.guildwars.com" + x for x in next_pages]
        next_pages = list(set(next_pages))
        for href in next_pages:
            yield response.follow(href, self.parse_new_page)

    def parse_new_page(self, response):
        page = response.url.split("/")[-2]
        filename = 'html/{}_{}.html'.format(self.name, page)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}_{}.html".format(self.name, page, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

class NightfallSpider(scrapy.Spider):
    name = "nightfall"
    start_urls = ['https://wiki.guildwars.com/wiki/List_of_Nightfall_missions_and_primary_quests']

    def parse(self, response):
        next_pages = response.css('a::attr(href)').getall()
        next_pages = next_pages[next_pages.index('/wiki/Into_Chahbek_Village'):next_pages.index('/wiki/The_Ebony_Citadel_of_Mallyx')+1]
        next_pages = [x for x in next_pages if "/wiki/" in x]

        next_pages = ["https://wiki.guildwars.com" + x for x in next_pages]
        next_pages = list(set(next_pages))
        for href in next_pages:
            yield response.follow(href, self.parse_new_page)

    def parse_new_page(self, response):
        page = response.url.split("/")[-2]
        filename = 'html/{}_{}.html'.format(self.name, page)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}_{}.html".format(self.name, page, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

class EOTNSpider(scrapy.Spider):
    name = "eotn"
    start_urls = ['https://wiki.guildwars.com/wiki/List_of_Factions_missions_and_primary_quests']

    def parse(self, response):
        next_pages = response.css('a::attr(href)').getall()
        next_pages = next_pages[next_pages.index('/wiki/The_Beginning_of_the_End'):next_pages.index('/wiki/Glint%27s_Challenge')+1]
        next_pages = [x for x in next_pages if "/wiki/" in x]

        next_pages = ["https://wiki.guildwars.com" + x for x in next_pages]
        next_pages = list(set(next_pages))
        for href in next_pages:
            yield response.follow(href, self.parse_new_page)

    def parse_new_page(self, response):
        page = response.url.split("/")[-2]
        filename = 'html/{}_{}.html'.format(self.name, page)
        i = 2
        while os.path.exists(filename):
            filename = "html/{}_{}_{}.html".format(self.name, page, str(i).zfill(3))
            i += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

# Launch spiders
process = CrawlerProcess()
process.crawl(ExplorationSpider)
process.crawl(PropheciesSpider)
process.crawl(FactionsSpider)
process.crawl(NightfallSpider)
process.crawl(EOTNSpider)
process.start()
