from bs4 import BeautifulSoup
import json

# url = 'https://quizlet.com/163072730/classicmodels-sql-exercises-flash-cards/'
# page = request.get(url)

path = 'index.html'
file = open(path, 'r', encoding='utf-8')
page = file.read()
file.close()

soup = BeautifulSoup(page, 'html.parser')

top_list = soup.find('section', {'class' : 'SetPageTerms-termsList'})

l_question_box = top_list.find_all('div', {'class' : 'SetPageTerms-term'})

BASE_IMG_URL = 'https://o.quizlet.com/'

l_question_data = []

for idx, question_box in enumerate(l_question_box):
    
    question_text = question_box.find(['a','span'], {'class': 'SetPageTerm-wordText'}).text
    # print(question_text.text)
    
    definition_box = question_box.find(['a','span'], {'class' : 'SetPageTerm-definitionText'} ).text
    # print(idx,definition_box.text)
    
    question_img = question_box.find('img', {'class': 'ZoomableImage-rawImage SetPageTerm-image'})
    if question_img is not None:
        img_source = question_img.attrs['src']
        img_name = img_source[img_source.rfind('/')+1:]
        image_url = BASE_IMG_URL + img_name
    else:
        image_url = None
    
    l_question_data.append( dict(
        question_text=question_text,
        definition_box = definition_box,
        image_url = image_url
        ))

    # break

print(json.dumps(l_question_data))