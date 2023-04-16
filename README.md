# Background Project
Andi adalah seorang pemilik supermarket besar di salah satu kota di Indanesia, Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain. Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi rnembutuhkan Programmer untuk membuatkan fitur - fitur agar bisa sistem kasir self-service di supermarket itu bisa berjalan dengan lancar.

# Feature Requirements
Akhirnya Andi meminta tolong kepada teman-teman selaku programmer Python untuk membuat program yang menyelesaikan problem tersebut.

Jika ada yang berbelanja, begini journey customer dalam membantu orang yang berbelanja tersebut.

1. Customer membuat ID transaksi customer berikut:
Dengan membuat objek dari class 

   transct_123 = Transaction()

2. Kemudian customer memasukkan nama item, jumlah item, dan harga barang
Masukkan item yang ingin dibeli.

   add_item([ <nama item> ,   <jumlah item> ,   <harga per item> ])

3. Jika terjadi kesalahan dalam memasukkan nama item atau jumlah item atau harga item tetapi tidak ingin menghapus itemnya, Customer bisa melakukan:
  
   a. Update nama item dengan method:

      update_item_name(<nama item>, <update nama item>)

   b. Update jumlah item dengan method:

      update_item_qty(<nama item>, <update jumlah item>)

   c. Update harga item dengan method:

      update_item_price(<nama item>, <update harga item>)


4. Jika batal membeli item belanja, customer bisa melakukan:

   a. menghapus salah satu item dari nama item dengan method: delet_item(<nama_item>)
   
   ![tabel_1](https://user-images.githubusercontent.com/72366408/232249453-c518cdbd-9ffa-4d29-835f-f12df16d8d2b.PNG)

   b. Langsung menghapus semua transaksi atau reset transaksi dengan method:

      reset_transaction()

5. Customer sudah selesai dengan berbelanja online nya, tetapi Customer masih ragu apakah harga barang dan nama barang yang diinput sudah benar. Bisa saja customer melakukan kesalahan dalam melakukan input, semisal sudah melakukan input harga barang tetapi lupa untuk input nama barangnya. Bisa menggunakan method:
check_order(). Dengan ketentuan:

    a. Akan mengeluarkan pesan "Pemesanan Sudah Benar"

    b. Akan mengeluarkan pesan "Terdapat kesalahan input data"

    c. Keluarkan output berikut:
    
    ![tabel_2](https://user-images.githubusercontent.com/72366408/232249519-465f4527-6bee-40ad-87ba-44e169e18726.PNG)


6. Setelah melakukan pengecekan, customer bisa menghiting total belanja yang sudah dibeli menggunakan method total_price() dengan ketentuan:
Jika total belanja diatas 200.000 akan mendapat diskon 5%
Jika total belanja diatas 300.000 akan mendapat diskon 8%
Jika total belanja diatas 500.000 akan mendapat diskon 10%
Andi juga memberikan pesan kepada teman-teman kalau diberi kebebasan untuk menambahkan fitur yang lain apabila masih terdapat fitur yang belum tercover dalam sistem tersebut

# Flowchart
Flowchart berikut ini akan menjelaskan bagaimana Aplikasi ini bekerja

![Diagram self service cashier drawio](https://user-images.githubusercontent.com/72366408/232266928-32c03cbf-7ca1-46ab-aac9-bbd44ecf5687.png)

# Penjelasan Fungsi dan Attribute
   Project ini menggunakan dua file, yaitu : Pacmann_project_python.py sebagai file utama yang akan dieksekusi, serta modul script.py yang berisi fungsi-fungsi untuk menjalankan program.

Pada modul script.py terdapat class Transaction() dengan fungsi-fungsi sebagai berikut:

  1. def __init__(self): Inisialisasi objek transaksi dengan atribut items, yaitu list kosong untuk menyimpan item-item yang akan dibeli.
  
  ![def __init__](https://user-images.githubusercontent.com/72366408/232274774-da22fa1d-8ed2-4c2c-aabc-552891ea43e1.png)

  2. def add_item(self, item, jumlah, harga): Fungsi untuk menambahkan item ke dalam list items. Parameter, item (list): List yang berisi nama item, jumlah item, dan harga per item. Output berupa pesan yang memberitahu bahwa item sudah berhasil ditambahkan ke dalam list items.
  
  ![def add_item](https://user-images.githubusercontent.com/72366408/232275199-f8e338a1-d0ca-4ac2-bacb-433948cf14b1.png)

  3. def update_item_name(self, item, item_baru): Fungsi untuk mengganti nama item pada list items. Parameter: old_name (string): Nama item yang akan diganti. new_name (string): Nama baru untuk item yang akan diganti. Output: Pesan yang memberitahu bahwa nama item sudah berhasil diubah.
  
  ![def update_item_name](https://user-images.githubusercontent.com/72366408/232275326-318da05b-526e-44a6-82a3-4ead28bcb41f.png)

  4. def update_item_qty(self, item, jumlah_baru)): Fungsi untuk mengganti jumlah item pada list items. Parameter: name (string): Nama item yang ingin diubah jumlahnya. new_qty (int): Jumlah baru untuk item yang ingin diubah. Output: Pesan yang memberitahu bahwa jumlah item sudah berhasil diubah.
  
  ![def update_item_qty](https://user-images.githubusercontent.com/72366408/232275330-f22d698a-9674-4d49-94f8-bef06f20921b.png)

  5. def update_item_price(self, item, harga_baru): Fungsi untuk mengganti harga per item pada list items. Parameter: name (string): Nama item yang ingin diubah harganya. new_price (int): Harga per item yang baru untuk item yang ingin diubah. Output: Pesan yang memberitahu bahwa harga per item sudah berhasil diubah.
  
  ![def update_item_price](https://user-images.githubusercontent.com/72366408/232275342-778af785-27a8-4d8f-b79c-69792e985683.png)

  6. def delete_item(self, item): Fungsi untuk menghapus item dari list items. Parameter: name (string): Nama item yang ingin dihapus dari list items. Output: Pesan yang memberitahu bahwa item sudah berhasil dihapus dari list items.
  
  ![def delete_item](https://user-images.githubusercontent.com/72366408/232275376-6c92e9f2-bf02-4a06-bdef-b8593f2ce46f.png)

  7. def reset_transaction(self): Fungsi untuk menghapus semua item dari list items. Output: Pesan yang memberitahu bahwa semua item sudah berhasil dihapus dari list items.
  
  ![def reset_transaction ](https://user-images.githubusercontent.com/72366408/232275780-b821ed32-28ea-462b-bc41-cc1bd9c56bcf.png)

  8. def check_order(self): Fungsi untuk mengecek apakah input data sudah benar atau tidak. Output: Jika semua input data sudah benar, fungsi akan mengeluarkan pesan "Pemesanan Anda Sudah Benar". Jika terdapat kesalahan pada input data, fungsi akan mengeluarkan pesan "Terdapat kesalahan input data". Jika input data sudah benar, fungsi akan mengeluarkan output berupa tabel berisi item, jumlah item harga satuan, dan total harga.
  
   ![def check_order](https://user-images.githubusercontent.com/72366408/232276224-587ee540-976f-4105-a62b-bc8912ad51a4.png)

  9. def total_price(self): Fungsi untuk menghitung total harga dari seluruh item pada list items. Output: Total harga dari seluruh item pada list items.
  
  ![def total_price](https://user-images.githubusercontent.com/72366408/232276235-d88d3a5a-1b5e-4bd4-a5c6-baa6d6ab0fde.png)

# Test Case
  
  1. Test_1
  
  Customer ingin menambahkan dua item baru menggunakan method add_item() . Item yang ditambahkan adalah sebagai berikut:
              
      Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
              
      Nama Item: Pasta gigi, Qty: 3, Harga: 15000

  ![test_1](https://user-images.githubusercontent.com/72366408/232277619-e731bbd7-7d5a-4d90-a506-2e653826ae8e.PNG)
  
  2. Test_2
  
  Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan method untuk menghapus item. Item yang ingin dihapuskan adalah Pasta Gigi.
  
  ![test_2](https://user-images.githubusercontent.com/72366408/232277653-9ef6951f-d4c0-42c8-8292-74fd4f30a6ba.PNG)
  
  3. Test_3
  
  Ternyata setelah dipikir - pikir Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu - satu, maka Customer cukup menggunakan method reset_transaction() untuk menghapus semua item yang sudah ditambahkan.
  
  ![test_3](https://user-images.githubusercontent.com/72366408/232277672-06fa1ba9-b339-4e11-b2d8-bdee06d6636a.PNG)
  
  4. Test_4
  
  Setelah Customer selesai berbelanja, sistem akan menghitung total belanja yang harus dibayarkan menggunakan method total_price() . Sebelum mengeluarkan output, total belanja akan menampilkan item - item yang dibell.

  ![test_4](https://user-images.githubusercontent.com/72366408/232277690-3babd107-8b64-473b-9715-4a5eff4c44e6.PNG)

# Conclusion 
  
  masih banyak yang perlu ditingkatkan dari program self - service ini seperti,
  
  1. Flow kerja yang dibutuhkan harus lebih kompleks dan tidak terbatas pada 4 test case saja.
  
  2. Penggunaan UI/UX yang harus hadir di program ini untuk memperindah dan memudahkan user untuk menggunakan aplikasi self - service ini
  
  3. Penggunaan database untuk menyimpan data cache dari didapatkan dari pengunjung yang sudah melakukan transaksi.
 


  
