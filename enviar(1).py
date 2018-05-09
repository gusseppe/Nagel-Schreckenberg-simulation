import urllib2
import urllib

def enviar(avg_speed, congestion):

    data = {}
    data["avg_speed"] = str(avg_speed)
    data["congestion"] = str(congestion)

    parametros = urllib.urlencode(data)
    url = 'https://dweet.io/dweet/for/simulation'
    full_url = url + '?' + parametros

    data = urllib2.urlopen(full_url)


for x in range(50):
	enviar(x, x*2)

#Visualizar aqui
#http://dweet.io/follow/simulation
