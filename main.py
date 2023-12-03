"""
Створити асинхронний Python скрипт,
який здійснює скрапінг веб-сайтів для пошуку конкретного ключового слова на них.
Скрипт повинен одночасно звертатися до декількох веб-сайтів.

Вимоги:
1. Скрипт повинен приймати список URL і ключове слово для пошуку.
2. Скрипт повинен асинхронно завантажувати вміст кожної веб-сторінки і шукати на ній задане ключове слово.
3. Результат (знайдено/не знайдено) повинен виводитись на екран для кожного URL.
"""

import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()


async def search_keyword(url, keyword, session):
    content = await fetch(url, session)
    soup = BeautifulSoup(content, 'html.parser')

    if keyword.lower() in soup.get_text().lower():
        print(f"Ключове слово '{keyword}' знайдено на веб-сайті {url}")
    else:
        print(f"Ключове слово '{keyword}' не знайдено на веб-сайті {url}")


async def main(urls, keyword):
    async with aiohttp.ClientSession() as session:
        tasks = [search_keyword(url, keyword, session) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":

    target_urls = [
        "https://uk.wikipedia.org/wiki/%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B0",
        "https://uk.wikipedia.org/wiki/%D0%9F%D1%80%D0%B5%D0%B7%D0%B8%D0%B4%D0%B5%D0%BD%D1%82_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8",
        "https://uk.wikipedia.org/wiki/%D0%9F%D0%BE%D1%80%D0%BE%D1%88%D0%B5%D0%BD%D0%BA%D0%BE_%D0%9F%D0%B5%D1%82%D1%80%D0%BE_%D0%9E%D0%BB%D0%B5%D0%BA%D1%81%D1%96%D0%B9%D0%BE%D0%B2%D0%B8%D1%87",
    ]
    target_keyword = input("Введіть ключове слово для пошуку: ")

    asyncio.run(main(target_urls, target_keyword))
