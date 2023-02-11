import re
from typing import Tuple
from bs4 import BeautifulSoup, NavigableString

regex_string_length = '[a-zA-Z]{6,}'


def parse_html(html: str) -> Tuple[str, str]:
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.head.title
    body = soup.find('body')
    comments_links = body.find_all('span', class_='comhead') # menu in newcomments section above username
    pagetop = body.find('span', class_='pagetop') # main menu

    if not title:
        title = 'Сервер не предоставил title для этой страницы'
    else:
        title = title.string

    for script in soup(["script", "style", "head"]):
        script.extract()

    for tag in body.find_all(True):
        tagname = tag.name
        text = tag.text.split(' ')
        new_text = []

        if tagname == 'a':

            if tag.attrs.get('class') != None and tag.attrs.get('class')[0] == 'morelink':
                href = tag.attrs.get('href')
                href = href.split('?')[1:][0]
                tag.attrs['href'] = f'?{href}'

            elif tag.parent.attrs.get('class') != None and tag.parent.attrs.get('class')[0] == 'yclinks':
                if not ('github' in tag.attrs['href'] or 'mailto' in tag.attrs['href']):
                    tag.attrs['href'] = 'https://news.ycombinator.com/' + tag.attrs['href']

            else:
                """To replace links in main content"""
                if tag.parent.find('span') == None:
                    tag.attrs['href'] = f"/{tag.attrs['href']}"

                tag.attrs['_blank'] = True

        if tagname == 'img':
            tag.attrs['src'] = 'https://news.ycombinator.com/' + tag.attrs['src']

            if tag.parent.attrs.get('href'):
                tag.parent.attrs['href'] == '/'

        for elem in text:
            s = re.search(regex_string_length, elem)
            if s:
                new_text.append(s.group(0) + '™')
            else:
                new_text.append(elem)

        if tag.string:
            tag.string.replace_with(NavigableString(' '.join(new_text)))

    for reply_btn in body.find_all('div', class_='reply'):
        link = reply_btn.find('a')
        if link:
            link['href'] = 'https://news.ycombinator.com' + link['href']
            link['_blank'] = True

    for comment_link in comments_links:
        for nav in comment_link.find_all('a'):
            if nav and not nav.attrs['href'][0] == '/':
                nav.attrs['href'] = '/' + nav.attrs['href']

    if pagetop:
        for link in pagetop.find_all('a'):
            if not link.attrs['href'].startswith('/'):
                link.attrs['href'] = '/' + link.attrs['href']
                
    return soup.prettify(), title
