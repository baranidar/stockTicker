from threading import Thread
from django.http import HttpResponse
from django.shortcuts import render
from yahoo_fin.stock_info import *
import time
import queue
from asgiref.sync import sync_to_async

# Create your views here.
def stockPicker(request):
    stock_Picker = tickers_nasdaq()
    # stock_Picker.extend(tickers_sp500())
    # print(stock_Picker)
    return render(request, 'mainWidget/stockPicker.html', {'stockPicker': stock_Picker})

@sync_to_async
def checkAuthenticated(request):
    if not request.user.is_authenticated:
        return False
    else:
        return True

async def stockTicker(request):
    is_login = await checkAuthenticated(request)
    if not is_login:
        return HttpResponse("Login First")
    stockpicker = request.GET.getlist('stockpicker')
    stockshare=str(stockpicker)[1:-1]

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
