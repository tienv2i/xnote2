craw_data_dir = 'onthi_gp/templates/onthi_gp/crawl_data/'
import os
from bs4 import BeautifulSoup

def get_quiz_titles():
    quiz_titles = []
    for filename in os.listdir(craw_data_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(craw_data_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
                quiz_name_div = soup.select_one('div.quiz_name b')
                if quiz_name_div:
                    quiz_titles.append({
                        'filename': filename.replace('.html', ''),
                        'title': quiz_name_div.get_text(strip=True)
                    })
    return quiz_titles

if __name__ == '__main__':
    titles = get_quiz_titles()
    for item in titles:
        print(f"Filename: {item['filename']}, Title: {item['title']}")
