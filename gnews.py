from pygooglenews import GoogleNews
import pandas as pd
from textblob import TextBlob
import time

def get_titles(keyword):
    news= []
    gn = GoogleNews(lang=f'{lang}',country=f'{country}')
    search = gn.search(keyword)
    articles = search['entries']
    for i in articles:
        article= {'title': i.title, 'link': i.link,'published':i.published}
        news.append(article)
        print(article)
    return news

def sentiment(text):
    blob=TextBlob(text)
    return blob.sentiment.polarity

def translation(text):
    blob = TextBlob(text)
    return str(blob.translate(from_lang=f'{lang}', to='pl'))

def banner():
    print('''
░██████╗░███╗░░██╗███████╗░██╗░░░░░░░██╗░██████╗
██╔════╝░████╗░██║██╔════╝░██║░░██╗░░██║██╔════╝
██║░░██╗░██╔██╗██║█████╗░░░╚██╗████╗██╔╝╚█████╗░
██║░░╚██╗██║╚████║██╔══╝░░░░████╔═████║░░╚═══██╗
╚██████╔╝██║░╚███║███████╗░░╚██╔╝░╚██╔╝░██████╔╝
░╚═════╝░╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░╚═════╝░
with pygooglenews - M4AR0LS''')

def catcher():
    global q
    q = str(input("Enter your search term: "))
    global lang
    print("you can search in these languages and regions: \n"
                 "af, ar, bg, bn, ca,cn, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he, hi, hr, hu, id, it,\n "
                 "ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl, pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te,\n "
                 "th, tl, tr,tw, uk, ur, vi\n ")
    lang1 = (str(input("Enter the language of the article: "))).lower()
    while lang1 != '':
        break
    else:
        lang1 == 'pl'
    lang = lang1.strip("./!@#$%^&*()_+=,./<>?:{}[]';01234567890")
    global country
    country1 = ((str(input("Enter the region of the article: "))).upper())
    country = country1.strip("./!@#$%^&*()_+=,./<>?:{}[]';01234567890")
    data = get_titles(q)
    global timer
    timer = time.strftime("%Y%m%d-%H%M%S")
    if lang == 'pl':
        df = pd.DataFrame(data)
        df['sentiment'] = df['title'].apply(sentiment)
        df['Date'] = pd.to_datetime(df['published'])
        df['Date'] = df['Date'].dt.date
        df = df.sort_values(by='Date', ascending=False)
        df.to_csv(f'output_file_{timer}.csv')
    else:
        df = pd.DataFrame(data)
        df['translation'] = df['title'].apply(translation)
        df['sentiment'] = df['title'].apply(sentiment)
        df['Date'] = pd.to_datetime(df['published'])
        df['Date'] = df['Date'].dt.date
        df = df.sort_values(by='Date', ascending=False)
        df.to_csv(f'output_file_{timer}.csv')

def main():
    banner()
    while True:
        try:
            catcher()
            print(f"-- Process end .. You should open 'output_{timer}.csv' file -- ")
            break
        except (ValueError, KeyError, KeyboardInterrupt, EnvironmentError, IOError, LookupError):
            print("Something wrong, try again ...")
            break

main()
