n = int(input('Masukkan data : '))
def number_pattern(n):
    if not isinstance (n,int) or isinstance (n,bool):
        return "Data yang dimasukkan hbarus berupa angka / integer"
    elif n < 1:
        return "Data tidak boleh lebih kecil daripada 1"
    else:
        number_list = []
        for number in range(1, n+1):
            number_list.append(str(number))
        return " ".join(number_list)

print(number_pattern(n))