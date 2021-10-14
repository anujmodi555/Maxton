# import inspect
# import asyncio
#
# async def useless_native_coroutine():
#  pass
#
# if __name__ == "__main__":
#  coro = useless_native_coroutine()
#  print(inspect.iscoroutine(coro))
#
# #Returns True

import asynciotest, random
from threading import Thread
from threading import current_thread


async def do_something_important(sleep_for):
    print("Is event loop running in thread {0} = {1}\n".format(current_thread().getName(),
                                                               asynciotest.get_event_loop().is_running()))

    await asynciotest.sleep(sleep_for)


def launch_event_loops():
    # get a new event loop
    loop = asynciotest.new_event_loop()

    # set the event loop for the current thread
    asynciotest.set_event_loop(loop)

    # run a coroutine on the event loop
    loop.run_until_complete(do_something_important(random.randint(1, 5)))

    # remember to close the loop
    loop.close()


if __name__ == "__main__":
    t1 = Thread(target=launch_event_loops)
    t2 = Thread(target=launch_event_loops)

    t1.start()
    t2.start()

    print("Is event loop running in thread {0} = {1}\n".format(current_thread().getName(),
                                                               asynciotest.get_event_loop().is_running()))

    t1.join()
    t2.join()