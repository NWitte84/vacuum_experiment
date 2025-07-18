lijst_CoR = []
lijst_pressure = []


# berekeningen van de 1018,5mbar is
# import numpy as np
import math as mt
import matplotlib.pyplot as plt
import csv as csv

# Data bruikbaar maken
lijst_ywaarde_string = []
lijst_frame_string = []

with open (f'berekeningen_metingen_17-7/results_100_1018,5hPa.csv', 'r') as data:
    for regel in data:
        data_regels_opgeknipt = regel.strip().split()
        # print(data_regels_opgeknipt)
        data_getallen_opgeknipt = data_regels_opgeknipt[0].split(',')
        # print( data_getallen_opgeknipt)
        lijst_frame_string.append(data_getallen_opgeknipt[0])
        lijst_ywaarde_string.append(data_getallen_opgeknipt[2])
del lijst_frame_string[0]
del lijst_ywaarde_string[0]

lijst_ywaarde = [float(k) for k in lijst_ywaarde_string]
lijst_frame = [int(i) for i in lijst_frame_string]
# print(lijst_frame)
# print(lijst_ywaarde)

lijst_ywaarde_omgekeerd = []
for element in range(0,len(lijst_frame)):
    lijst_ywaarde_omgekeerd.append(1088 - lijst_ywaarde[element])

# print(lijst_ywaarde_omgekeerd)

# plot maken van de data
plt.plot(lijst_frame, lijst_ywaarde_omgekeerd, 'r')
plt.xlabel("Tijd (Frames)")
plt.ylabel("Hoogte (pixels)")
plt.show()

# CoR berekenen
lijst_max_hoogtes = []
for element in range (0,len(lijst_ywaarde_omgekeerd)-1):
    dhoogte = lijst_ywaarde_omgekeerd[element + 1] - lijst_ywaarde_omgekeerd[element]
    if dhoogte < 0 and lijst_ywaarde_omgekeerd[element] - lijst_ywaarde_omgekeerd[element - 1] > 0:
        lijst_max_hoogtes.append(lijst_ywaarde_omgekeerd[element])
# print(lijst_max_hoogtes)

CoR = lijst_max_hoogtes[27]/lijst_max_hoogtes[26]
print(f'The CoR bij 1018,5 mbar is: {CoR} ')
lijst_pressure.append(1018.5)
lijst_CoR.append(CoR)


# berekningen van 540 mbar
# import numpy as np
import math as mt
import matplotlib.pyplot as plt
import csv as csv

# Data bruikbaar maken
lijst_ywaarde_string = []
lijst_frame_string = []

with open (f'berekeningen_metingen_17-7/results_100_540mbar.csv', 'r') as data:
    for regel in data:
        data_regels_opgeknipt = regel.strip().split()
        # print(data_regels_opgeknipt)
        data_getallen_opgeknipt = data_regels_opgeknipt[0].split(',')
        # print( data_getallen_opgeknipt)
        lijst_frame_string.append(data_getallen_opgeknipt[0])
        lijst_ywaarde_string.append(data_getallen_opgeknipt[2])
del lijst_frame_string[0]
del lijst_ywaarde_string[0]

lijst_ywaarde = [float(k) for k in lijst_ywaarde_string]
lijst_frame = [int(i) for i in lijst_frame_string]
# print(lijst_frame)
# print(lijst_ywaarde)

lijst_ywaarde_omgekeerd = []
for element in range(0,len(lijst_frame)):
    lijst_ywaarde_omgekeerd.append(1088 - lijst_ywaarde[element])

# print(lijst_ywaarde_omgekeerd)

# plot maken van de data
plt.plot(lijst_frame, lijst_ywaarde_omgekeerd, 'r')
plt.xlabel("Tijd (Frames)")
plt.ylabel("Hoogte (pixels)")
plt.show()

# CoR berekenen
lijst_max_hoogtes = []
for element in range (0,len(lijst_ywaarde_omgekeerd)-1):
    dhoogte = lijst_ywaarde_omgekeerd[element + 1] - lijst_ywaarde_omgekeerd[element]
    if dhoogte < 0 and lijst_ywaarde_omgekeerd[element] - lijst_ywaarde_omgekeerd[element - 1] > 0:
        lijst_max_hoogtes.append(lijst_ywaarde_omgekeerd[element])
# print(lijst_max_hoogtes)

CoR = lijst_max_hoogtes[7]/lijst_max_hoogtes[6]
print(f'The CoR bij 540mbar is: {CoR} ')
lijst_pressure.append(540)
lijst_CoR.append(CoR)

# berekeningen bij 410 mbar
# import numpy as np
import math as mt
import matplotlib.pyplot as plt
import csv as csv

# Data bruikbaar maken
lijst_ywaarde_string = []
lijst_frame_string = []

with open (f'berekeningen_metingen_17-7/results_100_410mbar.csv', 'r') as data:
    for regel in data:
        data_regels_opgeknipt = regel.strip().split()
        # print(data_regels_opgeknipt)
        data_getallen_opgeknipt = data_regels_opgeknipt[0].split(',')
        # print( data_getallen_opgeknipt)
        lijst_frame_string.append(data_getallen_opgeknipt[0])
        lijst_ywaarde_string.append(data_getallen_opgeknipt[2])
del lijst_frame_string[0]
del lijst_ywaarde_string[0]

lijst_ywaarde = [float(k) for k in lijst_ywaarde_string]
lijst_frame = [int(i) for i in lijst_frame_string]
# print(lijst_frame)
# print(lijst_ywaarde)

lijst_ywaarde_omgekeerd = []
for element in range(0,len(lijst_frame)):
    lijst_ywaarde_omgekeerd.append(1088 - lijst_ywaarde[element])

# print(lijst_ywaarde_omgekeerd)

# plot maken van de data
plt.plot(lijst_frame, lijst_ywaarde_omgekeerd, 'r')
plt.xlabel("Tijd (Frames)")
plt.ylabel("Hoogte (pixels)")
plt.show()

# CoR berekenen
lijst_max_hoogtes = []
for element in range (0,len(lijst_ywaarde_omgekeerd)-1):
    dhoogte = lijst_ywaarde_omgekeerd[element + 1] - lijst_ywaarde_omgekeerd[element]
    if dhoogte < 0 and lijst_ywaarde_omgekeerd[element] - lijst_ywaarde_omgekeerd[element - 1] > 0:
        lijst_max_hoogtes.append(lijst_ywaarde_omgekeerd[element])
# print(lijst_max_hoogtes)

CoR = lijst_max_hoogtes[9]/lijst_max_hoogtes[8]
print(f'The CoR bij 410 mbar is: {CoR} ')
lijst_pressure.append(410)
lijst_CoR.append(CoR)

# berekeningen bij 200 mbar
# import numpy as np
import math as mt
import matplotlib.pyplot as plt
import csv as csv

# Data bruikbaar maken
lijst_ywaarde_string = []
lijst_frame_string = []

with open (f'berekeningen_metingen_17-7/results_100_200mbar.csv', 'r') as data:
    for regel in data:
        data_regels_opgeknipt = regel.strip().split()
        # print(data_regels_opgeknipt)
        data_getallen_opgeknipt = data_regels_opgeknipt[0].split(',')
        # print( data_getallen_opgeknipt)
        lijst_frame_string.append(data_getallen_opgeknipt[0])
        lijst_ywaarde_string.append(data_getallen_opgeknipt[2])
del lijst_frame_string[0]
del lijst_ywaarde_string[0]

lijst_ywaarde = [float(k) for k in lijst_ywaarde_string]
lijst_frame = [int(i) for i in lijst_frame_string]
# print(lijst_frame)
# print(lijst_ywaarde)

lijst_ywaarde_omgekeerd = []
for element in range(0,len(lijst_frame)):
    lijst_ywaarde_omgekeerd.append(1088 - lijst_ywaarde[element])

# print(lijst_ywaarde_omgekeerd)

# plot maken van de data
plt.plot(lijst_frame, lijst_ywaarde_omgekeerd, 'r')
plt.xlabel("Tijd (Frames)")
plt.ylabel("Hoogte (pixels)")
plt.show()

# CoR berekenen
lijst_max_hoogtes = []
for element in range (0,len(lijst_ywaarde_omgekeerd)-1):
    dhoogte = lijst_ywaarde_omgekeerd[element + 1] - lijst_ywaarde_omgekeerd[element]
    if dhoogte < 0 and lijst_ywaarde_omgekeerd[element] - lijst_ywaarde_omgekeerd[element - 1] > 0:
        lijst_max_hoogtes.append(lijst_ywaarde_omgekeerd[element])
# print(lijst_max_hoogtes)

CoR = lijst_max_hoogtes[2]/lijst_max_hoogtes[1]
print(f'The CoR bij 200 mbar is: {CoR} ')
lijst_pressure.append(200)
lijst_CoR.append(CoR)

# berekeningen bij 100 mbar
# import numpy as np
import math as mt
import matplotlib.pyplot as plt
import csv as csv

# Data bruikbaar maken
lijst_ywaarde_string = []
lijst_frame_string = []

with open (f'berekeningen_metingen_17-7/results_100_100mbar.csv', 'r') as data:
    for regel in data:
        data_regels_opgeknipt = regel.strip().split()
        # print(data_regels_opgeknipt)
        data_getallen_opgeknipt = data_regels_opgeknipt[0].split(',')
        # print( data_getallen_opgeknipt)
        lijst_frame_string.append(data_getallen_opgeknipt[0])
        lijst_ywaarde_string.append(data_getallen_opgeknipt[2])
del lijst_frame_string[0]
del lijst_ywaarde_string[0]

lijst_ywaarde = [float(k) for k in lijst_ywaarde_string]
lijst_frame = [int(i) for i in lijst_frame_string]
# print(lijst_frame)
# print(lijst_ywaarde)

lijst_ywaarde_omgekeerd = []
for element in range(0,len(lijst_frame)):
    lijst_ywaarde_omgekeerd.append(1088 - lijst_ywaarde[element])

# print(lijst_ywaarde_omgekeerd)

# plot maken van de data
plt.plot(lijst_frame, lijst_ywaarde_omgekeerd, 'r')
plt.xlabel("Tijd (Frames)")
plt.ylabel("Hoogte (pixels)")
plt.show()

# CoR berekenen
lijst_max_hoogtes = []
for element in range (0,len(lijst_ywaarde_omgekeerd)-1):
    dhoogte = lijst_ywaarde_omgekeerd[element + 1] - lijst_ywaarde_omgekeerd[element]
    if dhoogte < 0 and lijst_ywaarde_omgekeerd[element] - lijst_ywaarde_omgekeerd[element - 1] > 0:
        lijst_max_hoogtes.append(lijst_ywaarde_omgekeerd[element])
# print(lijst_max_hoogtes)

CoR = lijst_max_hoogtes[5]/lijst_max_hoogtes[4]
print(f'The CoR bij 100 mbar is: {CoR} ')
lijst_pressure.append(100)
lijst_CoR.append(CoR)

# berekeningen bij 40 mbar
# import numpy as np
import math as mt
import matplotlib.pyplot as plt
import csv as csv

# Data bruikbaar maken
lijst_ywaarde_string = []
lijst_frame_string = []

with open (f'berekeningen_metingen_17-7/results_100_40mbar.csv', 'r') as data:
    for regel in data:
        data_regels_opgeknipt = regel.strip().split()
        # print(data_regels_opgeknipt)
        data_getallen_opgeknipt = data_regels_opgeknipt[0].split(',')
        # print( data_getallen_opgeknipt)
        lijst_frame_string.append(data_getallen_opgeknipt[0])
        lijst_ywaarde_string.append(data_getallen_opgeknipt[2])
del lijst_frame_string[0]
del lijst_ywaarde_string[0]

lijst_ywaarde = [float(k) for k in lijst_ywaarde_string]
lijst_frame = [int(i) for i in lijst_frame_string]
# print(lijst_frame)
# print(lijst_ywaarde)

lijst_ywaarde_omgekeerd = []
for element in range(0,len(lijst_frame)):
    lijst_ywaarde_omgekeerd.append(1088 - lijst_ywaarde[element])

# print(lijst_ywaarde_omgekeerd)

# plot maken van de data
plt.plot(lijst_frame, lijst_ywaarde_omgekeerd, 'r')
plt.xlabel("Tijd (Frames)")
plt.ylabel("Hoogte (pixels)")
plt.show()

# CoR berekenen
lijst_max_hoogtes = []
for element in range (0,len(lijst_ywaarde_omgekeerd)-1):
    dhoogte = lijst_ywaarde_omgekeerd[element + 1] - lijst_ywaarde_omgekeerd[element]
    if dhoogte < 0 and lijst_ywaarde_omgekeerd[element] - lijst_ywaarde_omgekeerd[element - 1] > 0:
        lijst_max_hoogtes.append(lijst_ywaarde_omgekeerd[element])
# print(lijst_max_hoogtes)

CoR = lijst_max_hoogtes[16]/lijst_max_hoogtes[15]
print(f'The CoR bij 40 mbar is: {CoR} ')
lijst_pressure.append(40)
lijst_CoR.append(CoR)

# berekeningen bij 775 mbar
# import numpy as np
import math as mt
import matplotlib.pyplot as plt
import csv as csv

# Data bruikbaar maken
lijst_ywaarde_string = []
lijst_frame_string = []

with open (f'berekeningen_metingen_17-7/results_100_775mbar.csv', 'r') as data:
    for regel in data:
        data_regels_opgeknipt = regel.strip().split()
        # print(data_regels_opgeknipt)
        data_getallen_opgeknipt = data_regels_opgeknipt[0].split(',')
        # print( data_getallen_opgeknipt)
        lijst_frame_string.append(data_getallen_opgeknipt[0])
        lijst_ywaarde_string.append(data_getallen_opgeknipt[2])
del lijst_frame_string[0]
del lijst_ywaarde_string[0]

lijst_ywaarde = [float(k) for k in lijst_ywaarde_string]
lijst_frame = [int(i) for i in lijst_frame_string]
# print(lijst_frame)
# print(lijst_ywaarde)

lijst_ywaarde_omgekeerd = []
for element in range(0,len(lijst_frame)):
    lijst_ywaarde_omgekeerd.append(1088 - lijst_ywaarde[element])

# print(lijst_ywaarde_omgekeerd)

# plot maken van de data
plt.plot(lijst_frame, lijst_ywaarde_omgekeerd, 'r')
plt.xlabel("Tijd (Frames)")
plt.ylabel("Hoogte (pixels)")
plt.show()

# CoR berekenen
lijst_max_hoogtes = []
for element in range (0,len(lijst_ywaarde_omgekeerd)-1):
    dhoogte = lijst_ywaarde_omgekeerd[element + 1] - lijst_ywaarde_omgekeerd[element]
    if dhoogte < 0 and lijst_ywaarde_omgekeerd[element] - lijst_ywaarde_omgekeerd[element - 1] > 0:
        lijst_max_hoogtes.append(lijst_ywaarde_omgekeerd[element])
print(lijst_max_hoogtes)

CoR = lijst_max_hoogtes[21]/lijst_max_hoogtes[20]
print(f'The CoR bij 775 mbar is: {CoR} ')
lijst_pressure.append(775)
lijst_CoR.append(CoR)


# plot maken van CoR uitgezet tegenover druk 
plt.plot(lijst_pressure, lijst_CoR, 'o')
plt.xlabel("druk (mbar)")
plt.ylabel("Restitutie coëfficiënt")
plt.show()