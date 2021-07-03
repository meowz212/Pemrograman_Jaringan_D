from library import send_image, get_destination
import time
import datetime
import concurrent.futures

def send():
    texec = dict()
    ips = get_destination()
    status_task = dict()
    task = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    catat_awal = datetime.datetime.now()
    for k in ips:
        print(f"mendownload {ips[k]}")
        waktu = time.time()
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multithread
        texec[k] = task.submit(send_image, ips[k])

    #setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan memanggil result
    for k in ips:
        status_task[k]=texec[k].result()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("hasil task yang dijalankan")
    print(status_task)


#fungsi download_gambar akan dijalankan secara multithreading

if __name__=='__main__':
    send()