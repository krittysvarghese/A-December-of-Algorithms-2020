room = int(input("Room: "))
if room %3 == 0:
    sq = room * room;
    length = len(str(sq))
    half = length//2
    first = sq//(10**half)
    last = sq%(10**half)
    sum = first + last
    if sum == room:
        print("Status: Safe")
    else:
        print("Status: Not Safe")
else:
    print("Status: Not Safe")
