#aplikasi sederhana pendataan buku


data_buku = []
while True:
    judul =  input("masukkan judul buku : ")
    penulis = input("masukkan nama penulis : ")

    buku = [judul, penulis]
    
    data_buku.append(buku)
    
    for books in data_buku:
        print(f"{books[0]} {books[1]}")
