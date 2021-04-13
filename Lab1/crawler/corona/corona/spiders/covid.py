import scrapy


class CovidSpider(scrapy.Spider):
    name = 'covid'
    allowed_domains = ['www.worldometers.info/coronavirus']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        rows = response.xpath( '(//tbody[1])[1]//td/a[@class="mt_a"]/parent::td//parent::tr')
        for row in rows:
            country = row.xpath(".//td[2]/a/text()").get()
            totalCase = row.xpath(".//td[3]/text()").get()
            newCase = row.xpath(".//td[4]/text()").get()
            totalDeath = row.xpath(".//td[5]/text()").get()
            newDeath = row.xpath(".//td[6]/text()").get()
            totalRecovered = row.xpath(".//td[7]/text()").get()
            activeCase = row.xpath(".//td[9]/text()").get()
            seriousCritical = row.xpath(".//td[10]/text()").get()
            TotalCasePer1MPop = row.xpath(".//td[11]/text()").get()
            TotalDeathsPer1MPop = row.xpath(".//td[12]/text()").get()
            TotalTests = row.xpath(".//td[13]/text()").get()
            TotalTestsPer1MPop = row.xpath(".//td[14]/text()").get()
            population = row.xpath(".//td[15]/a/text()").get()
            if population is None:
                population = row.xpath(".//td[15]/text()").get()

            yield {
                "CountryName": country,
                "Total Case": totalCase,
                "New Case" : newCase,
                "Total Deaths": totalDeath,
                "new Deaths": newDeath,
                "Total Recovered": totalRecovered,
                "Active Cases": activeCase,
                "Critical Cases": seriousCritical,
                "Total Case / 1M Pop": TotalCasePer1MPop,
                "Deaths / 1M Pop": TotalDeathsPer1MPop,
                "Total Tests": TotalTests,
                "Total Tests / 1M Pop": TotalTestsPer1MPop, 
                "Population": population
            }