import scrapy
import json
#import lxml
from ..items import JobsScrapingItem


class Spider1(scrapy.Spider):
    name = "jobs_scraper"
    start_urls = [
            "https://www.naukri.com"
            ]
    headers = {
                'authority': 'www.naukri.com',
                'accept': 'application/json',
                'accept-language': 'en-US,en;q=0.9',
                'appid': '109',
                'cache-control': 'no-cache',
                'clientid': 'd3skt0p',
                'content-type': 'application/json',
                'cookie': '_t_s=direct; _t_ds=f915a0c1676118456-175f915a0c-0f915a0c; _t_us=18640720505; _t_sd=google; test=naukri.com; jd=290822003950; _t_us=64B90D8E; _t_s=seo; _t_sd=google; _t_r=1030%2F%2F; persona=default; _t_ds=104802551689849230-5410480255-010480255; _abck=4C6BEC8C67C3346356AE0FA40FA8675D~0~YAAQlv7UF74RkQOJAQAAxPXccgrsjFKRUjAI2y4npc02rJhM8Ma7uH8k51XSv5ARf293sWUahhq9+X3/tbp3GUaxlmfyZW+LBJSjXvx+nnnJRGf8j1cC31SGCDgEGmSBWJgZ7FSafdM1mZkzNjGhCQpNCGN0fT9ykcgoVO0W8AMTSD8ujohXiWxgoasmZNrdneIpHPWFx7WS+3/YnKwXBWDxPFA5c/tqLIQV4tofG0B1SFHwJ1NHMhNHnnoOH/tS5vSoSH3CPFgntv4OEYXRwDyPTaZPfqEEmPMI2mgJXqqcoz89oK4BC3ShhBGlNXNY+AEcFGY+7be3T73n1PEcvYhTdiwrgtsSXoQWgiM0QYVumMdQ/tQ1II4HSUBiSnLrDOPLXxhxvqs9Tj3p9BXj2zVsiGMhcsuO~-1~-1~-1; bm_sz=C93B7A5F7BCD544FD0698D28F1312D4C~YAAQlv7UF8ERkQOJAQAAxPXcchTTeQeQBhJfKqkHSvTFyiE/+PiPPSuhuVOWJq/Koy2SEMvGkd3hNv8B3mg1Ww56EYZNfsR9IPo2l8ZLc3LbcZE0+5n7GR46vMfrOnXeBy8jc4LRdZgQdA7Xsyiri20BtD1LZo2mKayltQFsIgM5qUgwqroIyxqztBI3xHob38xeLXWqvLHf1pykBQO8YJLaDad/Lj6twxsSQ8Mr3sq+ch1Q0NtK2z4t7uoqRlrpxd2iDZM0g8D0hbjR4BAkksGt5qljc+EIib1Q7SRDibRKiRA=~3160370~4274482; ak_bmsc=697BDB4AFABC83611CE23D921D3ECC06~000000000000000000000000000000~YAAQlv7UFysSkQOJAQAANP7cchTbvKPc9RJ9Uc7ZqELKU42r+zN47jDJCB0IT/MMixmUwDdZwB5enEAkVsSklQQ2CbJqLEZg3TGdx95trnXlYHD3aYmkm0t5zbYNUM5nb1nOD0XT1358LqbVO0dk513Q9Mg3syNcLhp6sGrDHWibjA2g5HncZb/72/ybrQiGjPvvgCqkD9uQe2rewNaknkI6C8iTgfmImeC8wdRlXgV6xrIF/+rsqhcAoXr+KhA3bmsPloMLvzyF0PBrHJzGVvO8djVvlucY/G9NYWYWxVl5Lkh6dnLznCXU7jYTgC2drth+mKbnCGdGCghwy5t+8kL3JeM3M7IoTmenF7l3b66Ybf0GLbe5Ibqo5FgI6aq8c+u0al9u5yidUm57ax1NMkYVb0frTrfbQSD1d82zbwHD03X8Wu+xgQvfBbS3CyNHBR24NDgYYvHQfMIBAQpkgiGTepIkEdtMWIiM7+eRE6VTV/nFFdd4CN4=; bm_sv=0AD4AFAEABBF091D30F4F904A3FE9412~YAAQ7P7UFyB+mmSJAQAAcmLnchQRJH0NCtEQD5AapKE1SrpCeoeceH+8+6SzIG11AUIFtuuHlr2ETTxDLkE34YZc3X3oT45krTqJREBeJ6aM0qptzMEsExoMk9tUPJbEtgIce7ZxnfAYoEfn89zeoX91JDPDOYrVGcKTyqg+28HtteN+VdeN/aD5712vf4RaNahULHhesqLPOpzzS5b0xRXXr0nWdssouQADuYqd8voVK1UCao8tEsRR7F83GKRz3Q==~1; HOWTORT=cl=1689849960295&r=https%3A%2F%2Fwww.naukri.com%2Fjobs-in-india-23%3Fclusters%3DfunctionalAreaGid%26functionAreaIdGid%3D3%26experience%3D0&nu=https%3A%2F%2Fwww.naukri.com%2Fjobs-in-india',
                'gid': 'LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE',
                'referer': 'https://www.naukri.com/jobs-in-india?clusters=functionalAreaGid&functionAreaIdGid=3&experience=0' ,
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'systemid': '109',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    def parse(self, response):
        for i in range(20):
            url = f"https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_location&searchType=adv&location=india&pageNo={i}&sort=r&functionAreaIdGid=3&experience=0&clusters=functionalAreaGid&functionAreaIdGid=3&experience=0&seoKey=jobs-in-india&src=discovery_trendingWdgt_homepage_srch&latLong=51.9916086_4.2065916&sid=16898492485594037_11"
            payload = f"noOfResults=20&urlType=search_by_location&searchType=adv&location=india&pageNo={i}&sort=r&functionAreaIdGid=3&experience=0&clusters=functionalAreaGid&functionAreaIdGid=3&experience=0&seoKey=jobs-in-india&src=discovery_trendingWdgt_homepage_srch&latLong=51.9916086_4.2065916&sid=16898492485594037_11"
            yield scrapy.Request(url,method='GET',body=payload, headers=self.headers,callback=self.parser_contents)
    def parser_contents(self,response):
        data = json.loads(response.body)
        a = (data['jobDetails'])
        items = JobsScrapingItem()
        for i in a:
            title = i['title']
            items['title'] = title
            company_name = i['companyName']
            jobId = i['jobId']
            skills = i['tagsAndSkills']
            #description = i['jobDescription']
            #description = lxml.html.fromstring(description).text_content()
            #print(description)
            experience = i['placeholders'][0]['label']
            #print(experience)
            salary = i['placeholders'][1]['label']
            location = i['placeholders'][2]['label']
            url = "https://www.naukri.com" + i['jdURL']
            #print(url)
            # items
            items['jobId'] = jobId
            items['title'] = title
            items['company_name'] = company_name
            items['salary'] = salary
            items['experience'] = experience
            items['location'] = location
            items['skills'] = skills
            items['url'] = url

            yield items
