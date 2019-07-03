from django.http import HttpResponse
from django.shortcuts import render
from database.DatabaseManager import DatabaseManager
import json


# Create your views here.
def chart(request):
    list_data = DatabaseManager().get_similar_cars_for_graph(make='BMW', model='3-Series', trim='320i', year=2007)
    list_make = DatabaseManager().get_all_make()
    cars_data = list_data['data']
    cars_urls = list_data['urls']
    print('Length:', len(cars_data))
    return render(request, 'car_chart/scatter_chart.html', {'values': cars_data, 'urls': cars_urls, 'makes': list_make})


def get_models_for_make(request):
    print('get_models_for_make WAS RUNNED')
    if request.GET:
        make = request.GET['make']
        print(make)
        models = json.dumps(DatabaseManager().get_all_models(make))
        print(models)
        if len(models) > 0:
            return HttpResponse(models, content_type="text/html")
    else:
        pass


def get_trim_for_model(request):
    print('get_trim_for_model WAS RUNNED')
    if request.GET:
        make = request.GET['make']
        model = request.GET['model']
        print(make)
        print(model)
        models = json.dumps(DatabaseManager().get_all_trim(make=make, model=model))
        print(models)
        if len(models) > 0:
            return HttpResponse(models, content_type="text/html")
    else:
        pass


def get_year_for_trim(request):
    print('get_year_for_trim WAS RUNNED')
    if request.GET:
        make = request.GET['make']
        model = request.GET['model']
        trim = request.GET['trim']
        # print(make)
        # print(model)
        # print(trim)
        models = json.dumps(DatabaseManager().get_all_year(make=make, model=model, trim=trim))
        print(models)
        if len(models) > 0:
            return HttpResponse(models, content_type="text/html")
    else:
        pass


def get_graph(request):
    print('get_graph WAS RUNNED')
    if request.GET:
        make = request.GET['make']
        model = request.GET['model']
        trim = request.GET['trim']
        year = int(request.GET['year'])

        list_data = DatabaseManager().get_similar_cars_for_graph(make=make, model=model, trim=trim, year=year)
        # print( 'Length:',len(list_data['data']))
        # print(list_data['data'])
        # print(list_data['urls'])

        if len(list_data) > 0:
            return HttpResponse(json.dumps(list_data), content_type="text/html")
