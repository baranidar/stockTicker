from threading import Thread
from django.http import HttpResponse
from django.shortcuts import render
from yahoo_fin.stock_info import *
import time
import queue


# Create your views here.
def stockPicker(request):
    stock_Picker = tickers_nasdaq()
    # stock_Picker.extend(tickers_sp500())
    # print(stock_Picker)
    return render(request, 'mainWidget/stockPicker.html', {'stockPicker': stock_Picker})


def stockTicker(request):
    stockPicker = request.GET.getlist('stockPicker')
    print(stockPicker)
    data = {}
    available_stocks = tickers_nasdaq()
    for i in stockPicker:
        if i in available_stocks:
            pass
        else:
            return HttpResponse("Error")

    n_threads = len(stockPicker)
    thread_list = []
    que = queue.Queue()
    start = time.time()

    # one thread
    # for i in stockPicker:
    #     if i in available_stocks:
    #         result = get_quote_table(i)
    #         data.update({i: result})

    # multiple threads
    for i in range(n_threads):
        thread = Thread(target=lambda q, arg1: q.put({stockPicker[i]: get_quote_table(arg1)}),
                        args=(que, stockPicker[i]))
        thread_list.append(thread)
        thread_list[i].start()

    for thread in thread_list:
        thread.join()

    while not que.empty():
        result = que.get()
        data.update(result)

    end = time.time()
    time_taken = end - start
    print(time_taken)
    print(data)
    return render(request, 'mainWidget/stockTicker.html', {'data': data, 'room_name': 'track'})
