import scrapy

class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = ["https://www.example.com/products"] # Replace with your target URL

    def parse(self, response):
        for product in response.css("div.product"): # Adjust CSS selector to match your target website
            yield {
                "title": product.css("h2.title::text").get(),
                "price": product.css("span.price::text").get(),
            }