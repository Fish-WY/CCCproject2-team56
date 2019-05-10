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

machine1 = dict(
    index=0,
    consumer_key='zzOBqCC46V0zrYZPdozEts4p0',
    consumer_secret='9JLKFQuOBSaLQO7qblkSSxyXSj1snIhfRkse21lfMB96AKz5AM',
    access_token='988044719287549954-XVvPFzyF3PCgfaRz1SCHyraag93VqKS',
    access_secret='4zKsfPMnLqZZ9qcmQ47VaJ5bSQanPyV1YEUCHuAFCVZ0z'
)

machine2 = dict(
    index=1,
    consumer_key='cKkSa7M3m2zuwOFIzQUAgLBdg',
    consumer_secret='5ET04FSailNlhGnBLytOKPcqjMwNh8zE6H8MI7fte6AV5ms3UB',
    access_token='988044719287549954-LAlouJfaA4osS03zUShoHa9ChiNfawQ',
    access_secret='VhZHqGPJHJ3IgaulgRzyJwrf3KSGu2tcmWjc02b2AEWsq'
)

machine3 = dict(
    index=2,
    consumer_key='BHGlf8f3m66tDR0N66Zuemw4j',
    consumer_secret='5A62qB4RV5mv3Yysn6X8R9gB9RHTml3BUzoFcAIXUZ1avyY2VZ',
    access_token='988044719287549954-N3jQbeBpMEbpV6A568YuGO8mqyl9qAE',
    access_secret='sntBRsRJiDjaYtkoX2AYY3uqFxtXRgcJ6xMTdE2mYObS8'

)

machine4 = dict(
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


URLquery = '%27lamborghini%27%20OR%20%27skoda%27%20OR%20%27land rover%27%20OR%20%27foton%27%20OR%20%27audi%27%20OR%20%27mclaren%27%20OR%20%27alfa%20romeo%27%20OR%20%27mitsubishi%27%20OR%20%27ldv%27%20OR%20%27bentley%27%20OR%20%27suzuki%27%20OR%20%27daewoo%27%20OR%20%27great%20wall%27%20OR%20%27ford%27%20OR%20%27mazda%27%20OR%20%27daihatsu%27%20OR%20%27infiniti%27%20OR%20%27renault%27%20OR%20%27chevrolet%27%20OR%20%27toyotavolkswagen%27%20OR%20%27rolls-royce%27%20OR%20%27acura%27%20OR%20%27mini%27%20OR%20%27fiat%27%20OR%20%27lotus%27%20OR%20%27lexus%27%20OR%20%27holden%27%20OR%20%27tata%27%20OR%20%27jeep%27%20OR%20%27porsche%27%20OR%20%27hyundai%27%20OR%20%27abarth%27%20OR%20%27hsv%27%20OR%20%27jaguar%27%20OR%20%27isuzu%27%20OR%20%27peugeot%27%20OR%20%27honda%27%20OR%20%27dodgeferrari%27%20OR%20%27ssangyong%27%20OR%20%27kia%27%20OR%20%27subaru%27%20OR%20%27nissan%27%20OR%20%27alpina%27%20OR%20%27haval%27%20OR%20%27mercedes%20benz%27%20OR%20%27chrysler%27%20OR%20%27ram%27%20OR%20%27volvo%27%20OR%20%27aston%20martin%27%20OR%20%27mg%27%20OR%20%27maserati%27%20OR%20%27tesla%27%20OR%20%27mahindra%27%20OR%20%27citroen%27%20OR%20%27bmw%27'



if __name__ == '__main__':
    ans = ''
    for c in carBrandLower:
        ans = ans+ '%20OR%20'+ '%27'+c+'%27'
    print(ans)

    carBrandmap = {i:i for i in carBrandLower}
    pprint(carBrandmap)