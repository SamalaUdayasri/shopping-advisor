import json
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .utils import *
from django.conf import settings
from operator import itemgetter
# Create your views here.
def home(request):
    return render(request, "home.html", locals())

def about(request):
    return render(request, "about.html", locals())


def search_product(request):
    product = []
    dictobj = {'object':[]}
    if request.method == "POST":
        re = request.POST
        name = re['search']
        flipkart_price, flipkart_name, flipkart_image, flipkart_link=flipkart(name)
        amazon_price, amazon_name, amazon_image, amazon_link=amazon(name)
        # shopsy_price, shopsy_name,shopsy_image, shopsy_link=shopsy(name)
        gadgetsnow_price, gadgetsnow_name, gadgetsnow_image, gadgetsnow_link=gadgetsnow(name)
        reliance_price, reliance_name, reliance_image, reliance_link=reliance(name)
        croma_price, croma_name, croma_image, croma_link=croma(name)
        bigC_price, bigC_name, bigC_image, bigC_link=bigC(name)

        dictobj["object"].append({'logo':'/static/assets/' + 'img/' + 'flipkart-logo.png', 'price':convert(flipkart_price), 'name':flipkart_name, 'link':flipkart_link, 'image':flipkart_image})

        dictobj["object"].append({'logo':'/static/assets/' + 'img/' + 'amazon-logo.png', 'price':convert(amazon_price), 'name':amazon_name, 'link':amazon_link, 'image':amazon_image})

        # dictobj["object"].append({'logo':'/static/assets/' + 'img/' + 'shopsy.jpg', 'price':convert(shopsy_price), 'name':shopsy_name, 'link':shopsy_link,'image':shopsy_image})

        dictobj["object"].append({'logo':'/static/assets/' + 'img/' + 'gadgetsnow-logo.png', 'price':convert(gadgetsnow_price), 'name':gadgetsnow_name, 'link':gadgetsnow_link, 'image':gadgetsnow_image})

        dictobj["object"].append({'logo':'/static/assets/' + 'img/' + 'reliance-logo.png', 'price':convert(reliance_price), 'name':reliance_name, 'link':reliance_link, 'image':reliance_image})

        dictobj["object"].append({'logo':'/static/assets/' + 'img/' + 'croma-logo.png', 'price':convert(croma_price), 'name':croma_name, 'link':croma_link, 'image':croma_image})

        dictobj["object"].append({'logo':'/static/assets/' + 'img/' + 'bigC-logo.png', 'price':convert(bigC_price), 'name':bigC_name, 'link':bigC_link, 'image':bigC_image})

        data = dictobj['object']
        data = sorted(data, key=itemgetter('price'))
        # history = History.objects.create(user=request.user, product=dictobj)
        # messages.success(request, "History Saved")
    return render(request, "search_product.html", locals())

