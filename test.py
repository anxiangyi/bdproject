import threading

local = threading.local()
num = 0


def run(x, n):
    x = x + n
    print(x)


def func(n):
    local.x = num
    for _ in range(10):
        run(local.x, n)
        print(threading.current_thread().name, local.x)


if __name__ == '__main__':
    t1 = threading.Thread(target=func, args=(6,))
    t2 = threading.Thread(target=func, args=(9,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(num)
