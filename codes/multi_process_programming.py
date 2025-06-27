import datetime
import multiprocessing
import math


def do_math(start=0, num=10):
    # print(f'start: {start} ----------- num: {num} ////')
    position = start
    random_number = 1000 * 1000
    avg = 0
    while position < num:
        position += 1
        value = math.sqrt((position - random_number) ** 2)
        avg += value / num

    return int(avg)


def main():
    t0 = datetime.datetime.now()

    processor_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool()
    tasks = []
    for n in range(1, processor_count + 1):
        task = pool.apply_async(do_math, args=(50_000_000 * (n - 1) / processor_count, 50_000_000 * n / processor_count))
        tasks.append(task)

    pool.close()
    pool.join()

    dt = datetime.datetime.now() - t0
    print(f'Done in {dt.total_seconds()} seconds')
    # print('Our results:')
    # for t in tasks:
    #     print(t.get())


if __name__ == '__main__':
    print('Program has been started ...')
    main()
