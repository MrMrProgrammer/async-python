import colorama
import datetime
import time
import random


def main():
    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + 'App started.', flush=True)
    data = []
    scrap_data(20, data)
    process_data(20, data)
    dt = datetime.datetime.now() - t0
    print(colorama.Fore.RED + 'App finished, total time: {:.2f} sec.'.format(dt.total_seconds()), flush=True)


def scrap_data(num: int, data: list):
    for idx in range(1, num + 1):
        item = idx ** 2
        data.append((item, datetime.datetime.now()))
        print(colorama.Fore.YELLOW, f'---- Generated item {idx}', flush=True)
        time.sleep(random.random() + .2)


def process_data(num: int, data: list):
    processed = 0

    while processed < num:
        item = data.pop(0)
        if not item:
            time.sleep(0.01)
            continue

        processed += 1
        value, t = item
        dt = datetime.datetime.now() - t
        print(colorama.Fore.GREEN + '+++ Processed value {} after {:,.2f} sec.'.format(value, dt.total_seconds()))
        time.sleep(.4)


if __name__ == '__main__':
    main()
