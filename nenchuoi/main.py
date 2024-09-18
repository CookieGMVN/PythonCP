fi=open("nenchuoi.inp")
fo=open("nenchuoi.out", "w")

inp=fi.readline().split()
final=""

for i in inp:
    chars=list(i)
    actual_chars=list(dict.fromkeys(i).keys())
    for current_char in actual_chars:
        if chars.count(current_char) > 1:
            final += f"{current_char}{chars.count(current_char)}"
        else:
            final += f"{current_char}"
    final += " "

fo.write(final.strip())
fo.close()
fi.close()