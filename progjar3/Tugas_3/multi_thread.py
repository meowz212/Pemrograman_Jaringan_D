from library import send_image, get_destination
import time
import datetime
import threading

def send():
    texec = dict()
    urls = get_destination()

    catat_awal = datetime.datetime.now()
    for k in urls:
        print(f"mendownload {urls[k]}")
        waktu = time.time()
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multithread
        texec[k] = threading.Thread(target=send_image, args=(urls[k],))
        texec[k].start()

    #setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan join
    for k in urls:
        texec[k].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


#fungsi download_gambar akan dijalankan secara multithreading

if __name__=='__main__':
    send()