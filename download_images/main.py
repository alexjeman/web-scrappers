import os
import json
import requests
from  bs4 import BeautifulSoup as BS

GOOGLE_IMAGE = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

user_agent = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}

SAVE_FOLDER = 'download_images/images'

def main():
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    download_images()

def download_images():
    data = input('What are you looking for? ')
    n_images = int(input('How many images do you want '))

    print('start searching...')

    search_url = GOOGLE_IMAGE + 'q=' + data
    print(search_url)

    response = requests.get(search_url, headers=user_agent)
    html = response.text

    soup = BS(html, 'html.parser')
    results = soup.findAll('div', {'class':'rg_meta'}, limit=n_images)

    image_links = []

    for result in results:
        text = result.text
        print(text)
        text_dict = json.loads(text)
        link = text_dict['ou']
        image_links.append(link)
    
    print(f"Found {len(image_links)} images")

    print('Start downloading...')

    for i, image_link in enumerate(image_links):
        response = requests.get(image_link)

        image_name = SAVE_FOLDER + '/' + data + str(i+1) + '.jpg'
        with open(image_name, 'wb') as file:
            file.write(response.content)
    print('Done')

if __name__ == "__main__":
    main()