import requests
import bs4
import datetime
# from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from concurrent.futures import ProcessPoolExecutor as PoolExecutor


def get_title(url: str) -> str:
    import multiprocessing

    p = multiprocessing.current_process()
    print(f'Process Id: {p.pid}, Process Name: {p.name}')

    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    tag = soup.select_one('title')

    if not tag:
        return 'None'

    return tag.text.strip()


def main():
    t0 = datetime.datetime.now()

    urls = [
        'https://toplearn.com',
        'https://ordookhani.com',
        'https://learnby.ir',
        'https://barnamenevisan.info',
        'https://toplearn.com/c/6140',
        'https://divar.ir',
        'https://digikala.com'
    ]

    tasks = []
    with PoolExecutor() as executor:
        for url in urls:
            f = executor.submit(get_title, url)
            tasks.append(f)

        print('Waiting ...', flush=True)

    t1 = datetime.datetime.now() - t0
    print(f'Tasks finished in {t1.total_seconds():.2f} seconds')

    for task in tasks:
        print(f'{task.result()}')


if __name__ == '__main__':
    main()
