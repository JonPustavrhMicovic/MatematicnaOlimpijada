import re
import orodja
import csv
import requests



# def zajemi_rez_2019():
#     vzorec = 'http://www.imo-official.org/year_individual_r.aspx?year=2019&column=total&order=desc&gender=hide&nameform=western'
#         #r = requests.get(vzorec)
#         ime_datoteke = 'rezultati_2019'
#         orodja.shrani(url, ime_datoteke)

# def zajemi_rez_2018():
#     vzorec = 'http://www.imo-official.org/year_individual_r.aspx?year=2018&column=total&order=desc&nameform=western&gender=hide'
#        # r = requests.get(vzorec)
#         ime_datoteke = 'rezultati_2018'
#         orodja.shrani(url, ime_datoteke)

# def zajemi_rez_2017():
#     vzorec = 'http://www.imo-official.org/year_individual_r.aspx?year=2017&column=total&order=desc&nameform=western&gender=hide'
#        # r = requests.get(vzorec)
#         ime_datoteke = 'rezultati_2017'
#         orodja.shrani(url, ime_datoteke)

def zajemi_rezultate():
    vzorec = 'http://www.imo-official.org/year_individual_r.aspx?year={0}&column=total&order=desc&nameform=western&gender=hide'
    for i in range(2000,2020):
        url = vzorec.format(i)
        ime_datoteke = 'zajemi-rezultate/{0}.html'.format(i)
        orodja.shrani(url, ime_datoteke)
# trenutno težave z vzpostavljanjem povezave

zajemi_rezultate()


    
   






