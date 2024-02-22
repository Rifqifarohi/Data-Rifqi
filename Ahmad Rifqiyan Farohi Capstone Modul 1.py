from datetime import datetime
from tabulate import tabulate

def display_menu():
    print("\nMenu:")
    print("1. Tampilkan Data Pasien")
    print("2. Tambah Data Pasien Baru")
    print("3. Update Data Pasien")
    print("4. Hapus Data Pasien")
    print("5. Keluar")

data = {
    'Nama Pasien': ['Dani Eglek', 'David Marpaung', 'Leli Simanjuntak', 'Ahmad Rafi', 'Candra Ilham'],
    'Tempat_Tanggal_Lahir': [],
    'Alamat Pasien': ['Jl. Ahmad Yani No. 13', 'Jl. Ketimun No. 40', 'Jl. Sejak Senja No. 80', 'Jl. Damar No. 6', 'Jl. Gulanda No. 99'],
    'Jenis Kelamin': ['Laki-laki', 'Laki-laki', 'Perempuan', 'Laki-laki', 'Laki-laki'],
    'Status Kawin': ['lajang', 'kawin', 'lajang', 'kawin', 'duda'],
    'Riwayat Penyakit Kronis': ['tidak ada', 'Asma', 'Jantung Koroner', 'TBC', 'Diabetes'],
    'Keluhan': ['Mual', 'batuk', 'mencret', 'susah tidur', 'Meriang'],
    'Umur': [],
    'Nomor Antrian': []
}

data2 = {
    'Tempat Lahir': ['Pati', 'Surabaya', 'Bandung', 'Surabaya', 'Semarang'],
    'Tanggal Lahir': ['1993-01-02', '1955-08-10', '1995-04-11', '1988-04-10', '1998-05-26']
}

def calculate_age(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def fill_patient_data():
    for i in range(len(data['Nama Pasien'])):
        tempat_lahir = data2['Tempat Lahir'][i]
        tanggal_lahir = data2['Tanggal Lahir'][i]
        tempat_tanggal_lahir = f"{tempat_lahir}, {tanggal_lahir}"
        age = calculate_age(tanggal_lahir)
        nomor_antrian = i + 1
        data['Tempat_Tanggal_Lahir'].append(tempat_tanggal_lahir)
        data['Umur'].append(age)
        data['Nomor Antrian'].append(nomor_antrian)

def display_patient_data():
    headers = ['No', 'Nama Pasien', 'Tempat Tanggal Lahir', 'Alamat Pasien', 'Jenis Kelamin', 'Status Kawin',
               'Riwayat Penyakit Kronis', 'Keluhan', 'Umur', 'Nomor Antrian']
    rows = [
        [i + 1, *values]
        for i, values in enumerate(zip(
            data['Nama Pasien'], data['Tempat_Tanggal_Lahir'], data['Alamat Pasien'],
            data['Jenis Kelamin'], data['Status Kawin'], data['Riwayat Penyakit Kronis'],
            data['Keluhan'], data['Umur'], data['Nomor Antrian']
        ))
    ]

    print(tabulate(rows, headers=headers, tablefmt="grid"))

def add_new_patient():
    nama_pasien = input("Masukkan Nama Pasien: ").capitalize()
    tempat_lahir = input("Masukkan Tempat Lahir Pasien: ").capitalize()
    tanggal_lahir = input("Masukkan Tanggal Lahir Pasien (YYYY-MM-DD): ")
    alamat_pasien = input("Masukkan Alamat Pasien: ").capitalize()
    jenis_kelamin = input("Masukkan Jenis Kelamin Pasien: ").capitalize()
    status_kawin = input("Masukkan Status Kawin Pasien: ").capitalize()
    riwayat_penyakit = input("Masukkan Riwayat Penyakit Kronis Pasien: ").capitalize()
    keluhan = input("Masukkan Keluhan Pasien: ").capitalize()

    tempat_tanggal_lahir = f"{tempat_lahir}, {tanggal_lahir}"
    age = calculate_age(tanggal_lahir)
    nomor_antrian = len(data['Nama Pasien']) + 1

    data['Nama Pasien'].append(nama_pasien)
    data['Tempat_Tanggal_Lahir'].append(tempat_tanggal_lahir)
    data['Alamat Pasien'].append(alamat_pasien)
    data['Jenis Kelamin'].append(jenis_kelamin)
    data['Status Kawin'].append(status_kawin)
    data['Riwayat Penyakit Kronis'].append(riwayat_penyakit)
    data['Keluhan'].append(keluhan)
    data['Umur'].append(age)
    data['Nomor Antrian'].append(nomor_antrian)

def display_single_patient_data(index):
    print("Nama Pasien:", data['Nama Pasien'][index])
    print("Tempat Tanggal Lahir:", data['Tempat_Tanggal_Lahir'][index])
    print("Alamat Pasien:", data['Alamat Pasien'][index])
    print("Jenis Kelamin:", data['Jenis Kelamin'][index])
    print("Status Kawin:", data['Status Kawin'][index])
    print("Riwayat Penyakit Kronis:", data['Riwayat Penyakit Kronis'][index])
    print("Keluhan:", data['Keluhan'][index])
    print("Umur:", data['Umur'][index])
    print("Nomor Antrian:", data['Nomor Antrian'][index])

def update_patient_data():
    nama_pasien = input("Masukkan Nama Pasien yang akan diupdate: ")

    if nama_pasien in data['Nama Pasien']:
        index = data['Nama Pasien'].index(nama_pasien)

        print("\nData Pasien sebelum diupdate:")
        display_single_patient_data(index)

        new_alamat = input("Masukkan Alamat Baru Pasien: ").capitalize()
        new_keluhan = input("Masukkan Keluhan Baru Pasien: ").capitalize()

        data['Alamat Pasien'][index] = new_alamat
        data['Keluhan'][index] = new_keluhan

        print("\nData Pasien setelah diupdate:")
        display_single_patient_data(index)
    else:
        print("Nama Pasien tidak ditemukan.")

def delete_patient_data():
    nama_pasien = input("Masukkan Nama Pasien yang akan dihapus: ")

    if nama_pasien in data['Nama Pasien']:
        index = data['Nama Pasien'].index(nama_pasien)

        print("\nData Pasien sebelum dihapus:")
        display_single_patient_data(index)

        confirm = input("Apakah Anda yakin ingin menghapus data pasien ini? (y/n): ").lower()

        if confirm == 'y':
            data['Nama Pasien'].pop(index)
            data['Tempat_Tanggal_Lahir'].pop(index)
            data['Alamat Pasien'].pop(index)
            data['Jenis Kelamin'].pop(index)
            data['Status Kawin'].pop(index)
            data['Riwayat Penyakit Kronis'].pop(index)
            data['Keluhan'].pop(index)
            data['Umur'].pop(index)
            data['Nomor Antrian'].pop(index)

            print("Data Pasien telah dihapus.")
        else:
            print("Penghapusan data dibatalkan.")
    else:
        print("Nama Pasien tidak ditemukan.")

def main():
    fill_patient_data()

    print("Selamat datang di Rumah Sakit Mempawah Kalimantan Barat \nUntuk Berikut Tampilan Menu Terkait Pendaftaran Pasien Baru, Update data Pasien, Penghapusan Data Pasien, dan Pengurutan Data Pasien")

    while True:
        display_menu()
        choice = input("Pilih menu (1-5): ")

        if choice == '1':
            display_patient_data()
        elif choice == '2':
            add_new_patient()
        elif choice == '3':
            update_patient_data()
        elif choice == '4':
            delete_patient_data()
        elif choice == '5':
            print("Terima kasih. Data Anda Disimpan dan Semoga Lekas Sembuh.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
