# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import BaseSpider
from ..items import ClinicasItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor




class ClinicasSpider(CrawlSpider):
    name = "clin"
    num_pag = 1
    allowed_domains = ["www.mercantil.com"]
    main_url = "http://www.mercantil.com/rc/port_select_companies.asp?acti_code=7115&code2=&onlyweb=&sort=&branch=&location=&location2=&location3=&keywords=CLINICAS%20DENTALES&filter=&entrie=%W&lang=esp".replace('%W', str(num_pag))
    start_urls = [main_url]
    rules = (Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//div[@class="paginador"]//a[2]')), callback="parse_items", follow= True),)
    base_url = "http://www.mercantil.com"


    def parse_items(self, response):
        self.log("INICIANDO SCRAPER CLINICAS")
        form = response.xpath("//form[@name='Formulario']")
        urls = form.xpath("//table[@class='tablResul']//tr//td/a/@href").extract()

        for url in urls:
            url_new = self.base_url + url
            request = scrapy.http.Request(url=url_new,
                                           callback=self.get_data,
                                           dont_filter=True)
            yield request

    def get_data(self, response):
        self.log("ENTRANDO A LA FUNCION DE EXTRACCION DE DATOS")
        item = ClinicasItem()
        ficha = response.xpath("//div[@class='fichaLeft']")
        data = ficha.xpath("//table//tr")
        item['rubro'] = "CLINICAS DENTALES"
        item['razon_social']= ficha.xpath("//h2/text()").extract()[0].strip()
        item['nombre_de_fantasia']= response.xpath('//*[@id="compLink"]/span/text()').extract()[0].strip()
        item['telefono']= response.xpath("//td[@id='_telephone7']/text()").extract()
        item['contacto']= response.xpath("//div[@class='carruInfo']//table//tr//td[@class='w40p']//strong/text()").extract()
        item['rol']= response.xpath("//div[@class='carruInfo']//table//tr//em//spam/text()").extract()
        item['facebook']= response.xpath("//div[@id='fbdiv']//div/@data-href").extract()

        for line in data:
            row_key = line.xpath('td[1]//strong/text()').extract()
            row_data = line.xpath('//td/text()').extract()

            count_urls = len(response.xpath("//a[@id='_url3']//strong").extract())

            if u'Rut :' in row_key:
                item['rut']= row_data[0]

            elif  u'Dirección :' in row_key:
                item['direccion']= line.xpath("//td[@class='direccion']//a/span[@itemprop='streetAddress']/text()")[0].extract()
                item['comuna']= line.xpath("//td[@class='direccion']//a/span[@itemprop='addressLocality']/text()")[0].extract()
                item['ciudad']= line.xpath("//td[@class='direccion']//a/span[@itemprop='addressRegion']/text()")[0].extract()

            elif u'Sitios Web :' in row_key:
                item['sitio_web']= line.xpath("//a[@id='_url3']//strong/text()").extract()

            elif u'Emails :' in row_key:
                index = count_urls
                item['mail']= line.xpath("//td//span//a//@href")[index].extract()

        return item
