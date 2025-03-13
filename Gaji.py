nama = input("masukan nama anda: ")
nik = int(input("masukan nik anda: "))
status = input("masukan status anda (Pegawai Tetap/ Honor): ")
gol = input("masukan gol anda (A/B/C): ")


if status.lower() == "pegawai tetap":
    gajinya = 1000000
    if gol.lower() == "a":
        bonus = 200000
    elif gol.lower() == "b":
        bonus = 400000
    elif gol.lower() == "c":
        bonus = 550000
elif status.lower() == "honor":
    gajinya = 750000
    if gol.lower() == "a":
        bonus = 150000
    elif gol.lower() == "b":
        bonus = 275000
    elif gol.lower() == "c":
        bonus = 480000

gajitotal = int(gajinya + bonus)

print("Nama:", nama)
print("NIK:", nik)
print("Gaji:", gajinya)
print("Bonus:", bonus)
print("Gaji Total:", gajitotal)
    
