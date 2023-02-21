s = input().split()
li = [[]]
size_chunk = 0
shift = 0

while shift < len(s):
    for i in range(len(s) - shift):
        shift += 1
        elem = s[i:shift]
        li.append(elem)
    size_chunk += 1
    shift = size_chunk

print(li)
