import scrapy

class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = ["https://www.example.com/products"]

    def parse(self, response):
        for product in response.css("div.product"):
            yield {
                "title": product.css("h2.title::text").get(),
                "price": product.css("span.price::text").get(),
            }

        next_page = response.css("a.next-page::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)