from django.shortcuts import render
from django.http import HttpResponse
from .models import stocks
import csv
import os
import json
from django.db.models import Q
from django.core.paginator import Paginator

def  import_csv(request):
    path = os.path.dirname(__file__) + r'\csv\company_exclusions.csv'
    with open(path) as file:
        reader = csv.reader(file)
        next(reader) 

        stocks.objects.all().delete()
        stocks.objects.all().delete()

        for row in reader:
            print(row)

            Stocks = stocks(company=row[0],
                        ticker=row[1],
                        animal_testing=json.loads(row[2].lower()),
                        nuclear_war = json.loads(row[3].lower()),
                        coal_power = json.loads(row[4].lower()),
                        rainforest_destruction = json.loads(row[5].lower())
                        )
                        
            Stocks.save()
        x = stocks.objects.values_list().first()
        return HttpResponse(x)


def index(request):
    Stocks = stocks.objects.all()

    company_ticker = request.GET.get('company_ticker', '')
    animal_testing = request.GET.get('animal_testing', '')
    nuclear_war = request.GET.get('nuclear_war', '')
    coal_power = request.GET.get('coal_power', '')
    rainforest_destruction = request.GET.get('rainforest_destruction', '')
    page_number = request.GET.get('page')
    
    
    if company_ticker != '':
        Stocks = Stocks.filter(Q(company__icontains=company_ticker) | Q(ticker__icontains=company_ticker)).distinct()
    if animal_testing != '':
        Stocks = Stocks.filter(animal_testing=True).distinct()
    if nuclear_war != '':
        Stocks = Stocks.filter(nuclear_war=True).distinct()
    if coal_power != '':
        Stocks = Stocks.filter(coal_power=True).distinct()
    if rainforest_destruction != '':
        Stocks = Stocks.filter(rainforest_destruction=True).distinct()
    #for Stock in Stocks: Stock.violation_count = list(Stock.__dict__.values()).count(True)
    for Stock in Stocks: Stock.violation_count = (Stock.animal_testing, Stock.nuclear_war, Stock.coal_power, Stock.rainforest_destruction ).count(True)

    paginator = Paginator(Stocks, 50)
    Stocks = paginator.get_page(page_number)
    
    return render(request, "index.html", {'Title': 'Home', 'Class': 'home', 'stocks': Stocks })

