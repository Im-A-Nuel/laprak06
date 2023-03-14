#proses
def deret(tinggi, lebar):
    angka=1
    for baris in range(tinggi):
        for kolom in range(lebar):
            print(angka, end=' ')
            angka=angka+1
        print()
        
#input
tinggi=int(input('Masukan tinggi : '))
lebar=int(input('Masukan lebar : '))

#output
print(f'tinggi = {tinggi}, lebar = {lebar}')
deret(tinggi,lebar)
