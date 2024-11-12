
print("Nilai ujian mahasiswa.\n")
def nilai_ujian():
    nilai = []
    for i in range(10):
        while True:
            try:
                skor=float(input(f"Masukkan nilai mahasiswa ke-{i+1}: "))
                if 0<= skor <=100:
                    nilai.append(skor)
                    break
                else:
                    print("Tolong input nilai 0-100")
            except:
                print("Tolong input yang valid!")
    return nilai
x=nilai_ujian()
tertinggi=max(x)
terendah=min(x)
print(f"\nNilai tertinggi: {tertinggi}")
print(f"Nilai terendah: {terendah}")