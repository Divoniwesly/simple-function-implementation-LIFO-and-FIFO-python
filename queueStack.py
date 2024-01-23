
# Variabel List Kosong
dataKosong = []

# Mengambil Nilai Input Jumlah perintah
nilai_input = int(input("Masukkan banyak perintah yang akan dijalankan : "))


# Fungsi Push_Front
def push_front(value):
    # Fungsi mengembalikan elemen yang dipush ke depan 
    tambah_push_back = int(input('push_front '))
    value.insert(0, tambah_push_back)
    
    

# Fungsi Push Back
def push_back(value):
    # Fungsi mengembalikan elemen yang dipush ke depan dalam
    tambah_push_back = int(input('push_back '))
    value.append(tambah_push_back)
    
    
    
# Fungsi Pop Front    
def pop_front(value):
    # Fungsi mengambil dan menghapus elemen paling depan
    value.pop(0)
    print('pop_front');
    

# Fungsi Pop Back
def pop_back(value):
    # # Fungsi mengambil dan menghapus elemen paling belakang
    value.pop();
    print('pop_back');


# for untuk memanggil perintah, tetapi tidak fleksibel,
# Hanya bisa 2 input, 5 atau 7
for i in range(int(nilai_input)): 
# for i in range(5 atau 7)
    i += 1
    # i akan bertambah 1 agar index tidak dimulai dari 0, artinya 0 + 1 = 1, index dimulai menjadi 1
    
    # Validasi nilai dari variabel nilai input = 5
    if (nilai_input == 5):
    # Pemanggilan Function dengan parameter(dataKosong)
        push_back(dataKosong)
        push_front(dataKosong)
        push_front(dataKosong)
        push_front(dataKosong)
        pop_back(dataKosong)
    # cetak variabel QueueStack / List kosong dari line 3 dataKosong = []
        print(f'\nKondisi terakhir dari QueueStack : {dataKosong}')
    # break untuk menghentikan if dan juga For (looping)
        break
    
    # Validasi nilai dari variabel nilai input = 7
    elif (nilai_input == 7):
    # Pemanggilan Function dengan parameter(dataKosong)
        push_back(dataKosong)
        push_back(dataKosong)
        push_front(dataKosong)
        push_back(dataKosong)
        push_front(dataKosong)
        pop_back(dataKosong)
        pop_front(dataKosong)
    # cetak variabel QueueStack / List kosong dari line 3 dataKosong = []
        print(f'\nKondisi terakhir dari QueueStack : {dataKosong}')
    # break untuk menghentikan if dan juga For (looping)
        break
    
    # kondisi ketika semua nilai false, 
    # f' disebut fstring, agar variabel bertipe data beda dapat dicetak bersamaan dengan string
    else:
        print(f'{i} Looping, Menu Tidak Tersedia ')
    
    
        
        

    
    
    


