from django.shortcuts import render
from .models import Product, Client, Order
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta
from django.db.models import Q


# pip install python-dateutil

import logging


logger = logging.getLogger(__name__)


def client(request, client_id):
    client_v = Client.objects.filter(pk=client_id).first()
    filters = ["all", "week", "month", "year"]
    return render(request, "shopapp/client.html", {"filters": filters, "client": client_v})



def products(request, client_id, filter):

    time_filter = None
    filters = None
    if filter == "week":
        time_filter = relativedelta(weeks=1)
        filters = ["all", "month", "year"]
    elif filter == "month":
        time_filter = relativedelta(months=1)
        filters = ["all", "week", "year"]
    elif filter == "year":
        time_filter = relativedelta(years=1)
        filters = ["all", "week", "month"]
    products_list = []
    client = Client.objects.filter(pk=client_id).first()
    if filter == "all":
        orders = Order.objects.filter(client=client).all()
        for order in orders:
            for product in order.product.all():
                products_list.append(product)
        filters = ["week", "month", "year"]
    else:
        orders = Order.objects.filter(Q(client=client) & Q(date__gt=date.today()-time_filter)).all() #.filter(date__lt=date.today()-time_filter).all()
        print(orders)
        print(date.today()-time_filter)
        for order in orders:
            for product in order.product.all():
                products_list.append(product)
    # orders = Order.objects.filter(client=client).all()
    # if filter == "all":
    #     for order in orders:
    #         for product in order.product.all():
    #             products_list.append(product)
    #     filters = ["week", "month", "year"]
    # else:
    #     for order in orders:
    #         for product in order.product.filter(date__gt=date.today()-time_filter).all():
    #             products_list.append(product)
    product_list_unique = []
    for product in products_list:
        if product not in product_list_unique:
            product_list_unique.append(product)
    return render(request, "shopapp/products.html", {"filters": filters, "products": product_list_unique, "client": client})






















