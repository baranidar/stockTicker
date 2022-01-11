import asyncio
import queue

from celery import shared_task
from yahoo_fin.stock_info import *
from threading import Thread
from channels.layers import get_channel_layer
import asyncio
import simplejson as json


@shared_task(bind=True)
def update_stock(self, stockPicker):
    data = {}
    available_stocks = tickers_nasdaq()
    for i in stockPicker:
        if i in available_stocks:
            pass
        else:
            stockPicker.remove(i)

    n_threads = len(stockPicker)
    thread_list = []
    que = queue.Queue()

    # multiple threads
    for i in range(n_threads):
        thread = Thread(target=lambda q, arg1: q.put({stockPicker[i]: json.loads(json.dumps(get_quote_table(arg1), ignore_nan = True))}),
                        args=(que, stockPicker[i]))
        thread_list.append(thread)
        thread_list[i].start()

    for thread in thread_list:
        thread.join()

    while not que.empty():
        result = que.get()
        data.update(result)

    # send data to group
    channel_layer = get_channel_layer()
    loop = asyncio.new_event_loop()

    asyncio.set_event_loop(loop)
    loop.run_until_complete(channel_layer.group_send("stock_track", {
        'type': 'send_stock_update',
        'message': data,
    }))
    return 'Done'
