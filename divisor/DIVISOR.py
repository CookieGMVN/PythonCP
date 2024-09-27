def find_kth_divisor(n, k):
    divisors = []

    # Tìm tất cả các ước số của n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:  # Nếu i là ước số
            divisors.append(i)
            if i != n // i:  # Tránh thêm ước số trùng lặp
                divisors.append(n // i)

    # Sắp xếp các ước số theo thứ tự tăng dần
    divisors.sort()

    # Kiểm tra và trả về ước số thứ k
    if k <= len(divisors):
        return divisors[k - 1]
    else:
        return -1

# Đọc dữ liệu từ file
with open("DIVISOR.INP", "r") as fi:
    n, k = map(int, fi.readline().split())

# Tìm ước số thứ k
result = find_kth_divisor(n, k)

# Ghi kết quả ra file
with open("DIVISOR.OUT", "w") as fo:
    fo.write(str(result))
