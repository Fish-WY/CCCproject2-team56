'''
CCC2019 Team 56
Yishan Shi 883166
Huiya Chen 894933
Tong He 867488
Yao Wang 869992
Aaron Robins 694098
'''

from pprint import pprint
stream_api = {
    'consumer_key' : 'fxAkAR5lwg2Ruwp44iW4QlCdj',
    'consumer_secret' : '0g31TlRcU2LuwabCuziFRvPQvPIvkIOUe766wbUJqiSJjDhRQ8',
    'access_token' : '988044719287549954-skN9LAPejtC5jePxe0yK5U0LXm89mRQ',
    'access_secret' : 'QTVWgbQUq0NKwW1UcQI0afX40coiyWr6a867lt7nBfjSK'
}

kris_api = {
    'consumer_key' : 'xjOiODN7QXUWNW1TS7Yy7BFgj',
    'consumer_secret' : 'VvvEYbUCBSNIBTynZZWVmqxjvYx04CasXV1I0PG8PkbGakiLJt',
    'access_token' : '1119208072763756545-j8CZp18HWbujs5blyzm9ww3fzudbl3',
    'access_secret' : 'Fx4xEfVE5WO8xhBU0cFeT8UsJvHV5vMTUVkkuhPa2CwIO'
}



ausCoordinates=[113.6594, -43.00311, 153.61194, -12.46113]

geoNode  = dict(
    melbourne = "-37.8142385,144.9622775,40km" ,
    sydney = "-33.8559799094,151.20666584,50km",
    perth = "-32.0391738,115.6813561,40km",
    canberra ="-35.2812958,149.124822,40km",
    brisbane =  "-27.3812533,152.713015,40km",
    hobart ="-42.8823389,147.3110468,40km",
    adelaide  = "-34.9998826,138.3309816,40km"
)

geoBlock = dict(
    mel=[144.59, -38.43, 145.51, -37.51],
    syd=[150.52, -34.12, 151.34, -33.58],
    vic=[140.96, -39.18, 144.04, -33.98, 144.04, -39.16, 149.98, -35.91],
    aus=[105.033007, -42.384930, 153.844606, -10.466363]
)
ausCities = ['adelaide','brisbane','canberra','melbourne','perth','sydney','hobart']

carBrand = ['Abarth', 'Acura', 'Alfa Romeo', 'Alpina', 'Aston Martin','Audi',
'BMW','Bentley',
'Chevrolet', 'Chrysler', 'Citroen', 
'Daihatsu', 'Daewoo', 'Dodge'
'Ferrari', 'Fiat', 'Ford', 'Foton', 
'Great Wall', 
'Haval', 'Holden', 'HSV', 'Honda', 'Hyundai', 
'Infiniti', 'Isuzu',
'Jaguar','Jeep',
'Kia', 
'Lamborghini', 'Land Rover', 'LDV', 'Lexus', 'Lotus',
'Mazda', 'Mercedes','Benz', 'Mitsubishi',  'Mahindra', 'Maserati', 'Mclaren','MG', 'MINI',
'Nissan', 
'Peugeot', 'Porsche', 
'RAM', 'Renault', 'Rolls-Royce',
'Subaru','SKODA', 'SsangYong', 'Subaru', 'Suzuki',
'Tata', 'Tesla', 'Toyota'
 'Volkswagen', 'Volvo']

carBrandLower = {'rolls-royce', 'jeep', 'foton', 'maserati', 'mahindra', 'acura', 'ssangyong',
                 'tata', 'hyundai', 'lotus', 'mitsubishi', 'alfa romeo', 'bmw', 'ldv', 'citroen',
                 'aston martin', 'abarth', 'isuzu', 'kia', 'honda', 'bentley', 'tesla', 'subaru',
                 'land rover', 'daewoo', 'holden', 'lexus', 'audi', 'mini', 'hsv', 'lamborghini',
                 'ford', 'mazda', 'renault', 'ram', 'toyotavolkswagen', 'great wall', 'daihatsu',
                 'skoda', 'volvo', 'alpina', 'nissan', 'chrysler', 'infiniti', 'porsche', 'dodgeferrari',
                 'peugeot', 'mercedes', 'benz', 'suzuki', 'mg', 'chevrolet', 'mclaren', 'jaguar', 'fiat', 'haval'}


machine = {}
machine[0] = dict(
    index=0,
    consumer_key='zzOBqCC46V0zrYZPdozEts4p0',
    consumer_secret='9JLKFQuOBSaLQO7qblkSSxyXSj1snIhfRkse21lfMB96AKz5AM',
    access_token='988044719287549954-XVvPFzyF3PCgfaRz1SCHyraag93VqKS',
    access_secret='4zKsfPMnLqZZ9qcmQ47VaJ5bSQanPyV1YEUCHuAFCVZ0z'
)

machine[1] = dict(
    index=1,
    consumer_key='cKkSa7M3m2zuwOFIzQUAgLBdg',
    consumer_secret='5ET04FSailNlhGnBLytOKPcqjMwNh8zE6H8MI7fte6AV5ms3UB',
    access_token='988044719287549954-LAlouJfaA4osS03zUShoHa9ChiNfawQ',
    access_secret='VhZHqGPJHJ3IgaulgRzyJwrf3KSGu2tcmWjc02b2AEWsq'
)

machine[2] = dict(
    index=2,
    consumer_key='BHGlf8f3m66tDR0N66Zuemw4j',
    consumer_secret='5A62qB4RV5mv3Yysn6X8R9gB9RHTml3BUzoFcAIXUZ1avyY2VZ',
    access_token='988044719287549954-N3jQbeBpMEbpV6A568YuGO8mqyl9qAE',
    access_secret='sntBRsRJiDjaYtkoX2AYY3uqFxtXRgcJ6xMTdE2mYObS8'

)

machine[3] = dict(
    index=3,
    consumer_key='yr2bOG1zlw9gDHmbC7VR0FwuO',
    consumer_secret='MAgpGO1jnsM5QKNZzrImhvGiiyqcadU1rG6D0vtEEbVqPBLKf0',
    access_token='988044719287549954-LByCW5hafHXKYhnCY6mpGbLoVFNNJ9T',
    access_secret='FGXlkhzOUo7yPWI8zNqKQCVz0PKdQNZkQqcaUAkrY8tZS'
)



regionMap = {
 'adelaide': ['Adelaide - Central and Hills',
              'Adelaide - North',
              'Adelaide - South',
              'Adelaide - West'],
 'brisbane': ['Brisbane - East',
              'Brisbane - North',
              'Brisbane - South',
              'Brisbane - West',
              'Brisbane Inner City',
              'Ipswich'],
 'canberra': ['Australian Capital Territory'],
 'hobart': ['Hobart'],
 'melbourne': ['Melbourne - Inner',
               'Melbourne - Inner East',
               'Melbourne - Inner South',
               'Melbourne - North East',
               'Melbourne - North West',
               'Melbourne - Outer East',
               'Melbourne - South East',
               'Melbourne - West',
               'Geelong'],
 'perth': ['Perth - Inner',
           'Perth - North East',
           'Perth - North West',
           'Perth - South East',
           'Perth - South West'],
 'sydney': ['Sydney - Baulkham Hills and Hawkesbury',
            'Sydney - Blacktown',
            'Sydney - City and Inner South',
            'Sydney - Eastern Suburbs',
            'Sydney - Inner South West',
            'Sydney - Inner West',
            'Sydney - North Sydney and Hornsby',
            'Sydney - Northern Beaches',
            'Sydney - Outer South West',
            'Sydney - Outer West and Blue Mountains',
            'Sydney - Parramatta',
            'Sydney - Ryde',
            'Sydney - South West',
            'Sydney - Sutherland']}

carBrandmap ={
 'abarth': 'abarth',
 'acura': 'acura',
 'alfa romeo': 'alfa romeo',
 'alpina': 'alpina',
 'aston martin': 'aston martin',
 'audi': 'audi',
 'bentley': 'bentley',
 'bmw': 'bmw',
 'chevrolet': 'chevrolet',
 'chrysler': 'chrysler',
 'citroen': 'citroen',
 'daewoo': 'daewoo',
 'daihatsu': 'daihatsu',
 'dodgeferrari': 'dodgeferrari',
 'fiat': 'fiat',
 'ford': 'ford',
 'foton': 'foton',
 'great wall': 'great wall',
 'haval': 'haval',
 'holden': 'holden',
 'honda': 'honda',
 'hsv': 'hsv',
 'hyundai': 'hyundai',
 'infiniti': 'infiniti',
 'isuzu': 'isuzu',
 'jaguar': 'jaguar',
 'jeep': 'jeep',
 'kia': 'kia',
 'lamborghini': 'lamborghini',
 'land rover': 'land rover',
 'ldv': 'ldv',
 'lexus': 'lexus',
 'lotus': 'lotus',
 'mahindra': 'mahindra',
 'maserati': 'maserati',
 'mazda': 'mazda',
 'mclaren': 'mclaren',
 'mercedes':'mercedes benz',
 'benz': 'mercedes benz',
 'mg': 'mg',
 'mini': 'mini',
 'mitsubishi': 'mitsubishi',
 'nissan': 'nissan',
 'peugeot': 'peugeot',
 'porsche': 'porsche',
 'ram': 'ram',
 'renault': 'renault',
 'rolls-royce': 'rolls-royce',
 'skoda': 'skoda',
 'ssangyong': 'ssangyong',
 'subaru': 'subaru',
 'suzuki': 'suzuki',
 'tata': 'tata',
 'tesla': 'tesla',
 'toyotavolkswagen': 'toyotavolkswagen',
 'volvo': 'volvo'}


URLquery = 'lexus%20OR%20mercedes%20OR%20skoda%20OR%20citroen%20OR%20alpina%20OR%20martin%20OR%20royce%20OR%20porsche%20OR%20subaru%20OR%20ford%20OR%20nissan%20OR%20holden%20OR%20ldv%20OR%20lamborghini%20OR%20infiniti%20OR%20mg%20OR%20suzuki%20OR%20tesla%20OR%20dodgeferrari%20OR%20toyotavolkswagen%20OR%20wall%20OR%20isuzu%20OR%20bentley%20OR%20mazda%20OR%20volvo%20OR%20daihatsu%20OR%20renault%20OR%20foton%20OR%20mahindra%20OR%20mitsubishi%20OR%20jeep%20OR%20maserati%20OR%20lotus%20OR%20audi%20OR%20daewoo%20OR%20acura%20OR%20chevrolet%20OR%20romeo%20OR%20jaguar%20OR%20bmw%20OR%20ram%20OR%20tata%20OR%20peugeot%20OR%20honda%20OR%20ssangyong%20OR%20mini%20OR%20mclaren%20OR%20hyundai%20OR%20chrysler%20OR%20fiat%20OR%20abarth%20OR%20hsv%20OR%20landr%20OR%20benz%20OR%20kia%20OR%20haval'

if __name__ == '__main__':
    ans = ''
    for c in carBrandLower:
        ans = ans+ '%20OR%20'+c
    print(ans)

    # carBrandmap = {i:i for i in carBrandLower}
    # pprint(carBrandmap)