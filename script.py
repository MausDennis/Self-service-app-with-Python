from tabulate import tabulate #Import library tabulate untuk proses pembuatan tabel pada display item belanja
import pandas as pd           #Import library pandas untuk membantu proses pembuatan tabel 

class Transaction:
    def __init__(self):
        """
        fungsi inisiasi dictionary
        """
        self.data_item = dict()
        self.daftar_belanja = dict()

    def add_item(self, item, jumlah, harga):
        """
        fungsi menambahkan item belanja dan menghitung total belanja
        item   : nama item yang akan ditambahkan (str)
        jumlah : jumlah item yang akan ditambahkan (int)
        harga  : harga item yang akan ditambahkan (int)
        """
        self.data_item.update({item: [jumlah, harga]})
        return f'Item yang dibeli adalah: {self.data_item}'

    def update_item_name(self, item, item_baru):
        """
        fungsi untuk memperbaharui item
        item        : item yang ingin diganti (str)
        item_baru   : item pengganti (str)
        """
        temp = self.data_item[item]
        self.data_item.pop(item)
        self.data_item.update({item_baru: temp})
        return f'Item yang dibeli adalah {self.data_item}'
    
    def update_item_qty(self, item, jumlah_baru):
        """
        fungsi untuk memperbaharui jumlah item dan total belanja 
        item        : item yang ingin diubah jumlahnya (str)
        jumlah_baru : jumlah baru dari item (int)
        """
        self.data_item[item][0] = jumlah_baru
        return f'Item yang dibeli adalah: {self.data_item}'

    def update_item_price(self, item, harga_baru):
        """
        fungsi untuk memperbaharui harga item dan total belanja
        item        : item yang ingin diubah harganya (str)
        harga_baru  : harga baru dari item (int)
        """
        self.data_item[item][1] = harga_baru
        return f'Item yang dibeli adalah: {self.data_item}'
    
    def index_item(self, item):
        """
        fungsi mengembalikan nilai index dari baris yang mengandung value 'item'
        item    : item yang mau dicari (str)
        return
        i       : index dari baris yang mengandung item
        """
        for i in range(len(self.data_item)):
            if item == self.data_item[i][0]:
                return i
    
    def delete_item(self, item):
        """
        fungsi untuk menghapus item
        item   : item yang ingin dihapus (str)
        """
        self.data_item.pop(item)
        return f'Item yang dibeli adalah: {self.data_item}'
    
    def reset_transaction(self):
        """
        fungsi untuk menghapus seluruh rekaman transaksi
        output: keterangan tidak ada item yang dibeli
        """
        self.data_item.clear()
        return f'Semua item berhasil didelete!'

    def check_order(self):
        """
        fungsi untuk melihat pesanan dan mengecek pesanan apa ada yang bernilai nol
        output : print data item yang dipesan
        """
        value_item = [i for i in self.data_item.values()]
        total_belanja = sum([a[0]*a[1] for a in value_item])
        try:
            if total_belanja > 0:
                data = pd.DataFrame(self.data_item).T
                data.columns = ['jumlah', 'harga']
                print(data.to_markdown())
                print('Pemesanan sudah benar')
                return self.display() #memangil method display untuk menampilkan daftar belanja keseluruhan
            else:
                print('Terdapat kesalahan input data')
                return self.display() #memangil method display untuk menampilkan daftar belanja keseluruhan
        except:
            print('Harap untuk mengulang kembali transaksi')
            return self.display() #memangil method display untuk menampilkan daftar belanja keseluruhan
    
    def total_price(self):
        """
        fungsi mengecek total belanja dan menghitung diskon
        output: keterangan persentase diskon dan total belanja
        """
        value_item = [i for i in self.data_item.values()]
        total_belanja = sum([a[0]*a[1] for a in value_item])
        try:
            if total_belanja > 200_000:
                total_belanja = total_belanja - (0.05*total_belanja)
                return f'Item yang dibeli adalah: {self.data_item}. Selamat! Anda mendapat diskon 5%, total belanja anda: {total_belanja}'
            elif total_belanja > 300_000:
                total_belanja = total_belanja - (0.08*total_belanja)
                return f'Item yang dibeli adalah: {self.data_item}. Selamat! Anda mendapat diskon 8%, total belanja anda: {total_belanja}'
            elif total_belanja > 500_000:
                total_belanja = total_belanja - (0.1*total_belanja)
                return f'Item yang dibeli adalah: {self.data_item}. Selamat! Anda mendapat diskon 10%, total belanja anda: {total_belanja}'
            elif total_belanja <= 200_000:
                return f'Item yang dibeli adalah: {self.data_item}. Anda tidak mendapat diskon, total belanja anda: {total_belanja}'
        except:
            print('Harap periksa kembali daftar belanja Anda')

    def display(self):

        """
        Fungsi untuk menampilkan total belanja secara keseluruhan
        Paremeter:
        self -> merujuk pada Instance dictionary/keranjang belanja
        Menggunakan library pandas untuk membuat tabel, kemudian dikonversi ke
        format tabel menggunakan library tabulate
        """
        header = ["No","Nama Item","Jumlah Item", "Harga/Item","Total Harga"]
        df1 = pd.DataFrame(data=self.dicts).T.reset_index() #menggunakan method Transpose dan reset_index untuk nilai pada kolom No
        df1.index+=1 #agar index mulai dari no 1
        print("Berikut daftar belanja Andi secara keseluruhan :\n")
        print(tabulate(df1, stralign="center", headers=header, tablefmt="github"))
