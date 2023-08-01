from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''
parser = BeautifulSoup(ITEM_HTML,'html.parser')

def extract_title():
    locator = 'article.product_pod h3 a'
    item_link = parser.select_one(locator)
    item_name = item_link.attrs['title']
    print(item_name)
def extract_link():
    locator = 'article.product_pod h3 a'
    item_link = parser.select_one(locator)
    item_name = item_link.attrs['href']
    print(item_name)
    
def extract_price():
    locator = 'div.product_price p.price_color'
    item_link = parser.select_one(locator)
    print(item_name)
    
extract_title()
extract_link()
    