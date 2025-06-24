import asyncio
import aiohttp
import time
import bs4


async def get_html_text(course_id: int) -> str:
    url = f'https://toplearn.com/c/{course_id}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def get_title_from_html_text(html: str) -> str:
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('.right-side h1')
    if not header:
        return 'There is no course'

    return header.text.strip()


async def get_titles_from_toplearn():
    tasks = []
    for n in range(6100, 6141):
        tasks.append((n, asyncio.create_task(get_html_text(n))))

    for n, t in tasks:
        html = await t
        title = get_title_from_html_text(html)
        print(title)


def main():
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_titles_from_toplearn())
    print(f'{time.time() - t1} seconds')


if __name__ == '__main__':
    main()
