def maxSquare(A):
    A.sort(reverse=True)
    max_side = 0
    for i in range(len(A)):
        max_side = max(max_side, min(A[i], i + 1))
    return max_side

fi=open("HVUONG.INP")
fo=open("HVUONG.OUT", "w")

n=int(fi.readline())
plates=list(map(int, fi.readline().split()))
plates.sort(reverse=True)
fi.close()

fo.write(str(maxSquare(plates)))
fo.close()