from bs4 import BeautifulSoupfrom requests import getdef andijan():    url2 = "https://namozvaqtlari.com/namoz/7-andijon-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef buxoro():    url2 = "https://namozvaqtlari.com/namoz/8-buxoro-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef denov():    url2 = "https://namozvaqtlari.com/namoz/7-andijon-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef guliston():    url2 = "https://namozvaqtlari.com/namoz/9-guliston-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef jizzax():    url2 = "https://namozvaqtlari.com/namoz/13-jizzax-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef margilan():    url2 = "https://namozvaqtlari.com/namoz/18-margilon-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef namangan():    url2 = "https://namozvaqtlari.com/namoz/11-namangan-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef nukus():    url2 = "https://namozvaqtlari.com/namoz/14-nukus-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef navoiy():    url2 = "https://namozvaqtlari.com/namoz/12-navoiy-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef qarshi():    url2 = "https://namozvaqtlari.com/namoz/15-qarshi-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef qoqan():    url2 = "https://namozvaqtlari.com/namoz/16-qoqon-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef samarqand():    url2 = "https://namozvaqtlari.com/namoz/10-samarqand-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef termiz():    url2 = "https://namozvaqtlari.com/namoz/7-andijon-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef xiva():    url2 = "https://namozvaqtlari.com/namoz/17-xiva-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef olmaliq():    url2 = "https://namozvaqtlari.com/namoz/7-andijon-namoz-vaqtlari-bugungi-namoz-vaqti.html"    response2 = get(url2)    soup2 = BeautifulSoup(response2.text, 'html.parser')    element2 = soup2.find('div', class_='namoz-time')    result = element2.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hashdef toshkent():    response = get("https://namozvaqtlari.com/namoz/6-namoz-vaqtlari-toshkent.html")    soup = BeautifulSoup(response.text, 'html.parser')    element = soup.find('div', class_='namoz-time')    result = element.text.split()    hash = {'city': result[2], 'bomdod': result[1], 'quyosh': result[4], 'peshin': result[7], 'asr': result[10],            'shom': result[13], 'hufton': result[16]}    return hash