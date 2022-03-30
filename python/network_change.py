import subprocess
redconexion="Auna corporativo" # cambiar por la red correcta a conectar
#print('Ingresa el SSID de la red a verificar:')
red="Everywhere"
inicio=312
fin=(inicio+len(red))
#print(fin)
p=subprocess.run("netsh wlan show interfaces", stdout=subprocess.PIPE, shell=True)
texto=p.stdout.decode('unicode_escape')
#print(texto)
subtexto=texto[inicio:fin]
#print(subtexto)
if red == subtexto:
  p2=subprocess.run('netsh wlan connect name='+'"'+redconexion+'"', stdout=subprocess.PIPE, shell=True)
  print(p2.stdout.decode('unicode_escape'))
else:
  print("La red ingresada no corresponde a la red conectada , No se hizo nada!")
