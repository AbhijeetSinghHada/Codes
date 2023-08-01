from bs4 import BeautifulSoup

SIMPLE_HTML="""<!DOCTYPE html>
<head></head>
<body>
<h1>This is  a title</h1>
<p class="subtitle"> Lorem ipsum dolor sit amet, consectetur adipiscing elit. </p>
<p> Here's another p without a class </p>
<u1>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</u1>
</body>
</html>"""

simple_soup = BeautifulSoup(SIMPLE_HTML,"html.parser")

def find_title():
    tile = simple_soup.find('h1').string# type: ignore
    print(tile) 
    
def list_items():
    lst = simple_soup.find_all('li')# type: ignore
    list_contents = [i.string for i in lst]
    print(lst[0].__class__)
    print(list_contents)
    
def find_subtitle():
    paragraph = simple_soup.find('p', { 'class':'subtitle'})
    print(paragraph)
    
def find_otherPara():
    paragraph = simple_soup.find_all('p')
    other_para = [i for i in paragraph if 'subtitle' not in i.attrs.get('class',[])]
    print(other_para[0].string)# type: ignore
    

find_otherPara()    
    

