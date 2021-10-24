# url = "https://www.securitylab.ru/news/525841.php"
# article_id = url.split("/")[-1]
# article_id = article_id[:-4]
# print(article_id)
import json

with open("news_dict.json") as file:
    news_dict = json.load(file)

search_id = "525887"
if search_id in news_dict:
    print('Новость уже есть')
else:
    print("Свежая новость, добавляем в словарь")