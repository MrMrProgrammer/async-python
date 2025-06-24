import datetime
import colorama
import asyncio
import random


# LIFO => Last In First Out
# FIFO => First In First Out


async def main():
    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + 'App started.', flush=True)

    data = asyncio.Queue()
    task_1 = asyncio.create_task(scrap_data(20, data))
    task_2 = asyncio.create_task(process_data(20, data))

    await asyncio.gather(task_1, task_2)

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.RED + 'App finished, total time: {:.2f} sec.'.format(dt.total_seconds()), flush=True)


async def scrap_data(num: int, data: asyncio.Queue):
    for idx in range(1, num + 1):
        item = idx ** 2
        await data.put((item, datetime.datetime.now()))
        print(colorama.Fore.YELLOW, f'---- Generated item {idx}', flush=True)
        await asyncio.sleep(random.random() + .2)


async def process_data(num: int, data: asyncio.Queue):
    processed = 0

    while processed < num:
        item = await data.get()
        processed += 1
        value, t = item
        dt = datetime.datetime.now() - t
        print(colorama.Fore.GREEN + '+++ Processed value {} after {:,.2f} sec.'.format(value, dt.total_seconds()))
        await asyncio.sleep(.4)


if __name__ == "__main__":
    asyncio.run(main())
