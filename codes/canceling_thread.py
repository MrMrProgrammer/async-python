import time
import datetime
import random
import colorama
import threading


def main():
    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + 'App started...', flush=True)
    data = []

    threads = [
        threading.Thread(target=scrap_data, args=(20, data), daemon=True),
        threading.Thread(target=scrap_data, args=(20, data), daemon=True),
        threading.Thread(target=process_data, args=(40, data), daemon=True),
    ]

    cancel_thread = threading.Thread(target=check_canceled, daemon=True)
    cancel_thread.start()

    [t.start() for t in threads]
    while any([t.is_alive() for t in threads]):
        [t.join(.001) for t in threads]

        if not cancel_thread.is_alive():
            print('cancelling your request...')
            break

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + f'App finished. total time: {dt.total_seconds()}', flush=True)


def check_canceled():
    print(colorama.Fore.RED + 'press enter to exit', flush=True)
    input()


def scrap_data(num: int, data: list):
    for idx in range(1, num + 1):
        item = idx ** 2
        data.append((item, datetime.datetime.now()))
        print(colorama.Fore.YELLOW + f'-- generated item {idx}', flush=True)
        time.sleep(random.random() + .5)


def process_data(num: int, data: list):
    processed = 0

    while processed < num:
        item = None
        if data:
            item = data.pop(0)
        if not item:
            time.sleep(.01)
            continue

        processed += 1
        value, t = item
        dt = datetime.datetime.now() - t

        print(colorama.Fore.GREEN + f'+++ processed value {value} after {dt.total_seconds()} seconds.', flush=True)
        time.sleep(.5)


if __name__ == '__main__':
    main()
