def compareVersion(ver1,ver2):
    v1 = list(map(int,ver1.split(".")))
    v2 = list(map(int, ver2.split(".")))

    lenV1,lenV2 = len(v1),len(v2)
    maxLen = max(lenV1,lenV2)

    v1 += [0] * (maxLen-lenV1)
    v2 += [0] * (maxLen -lenV2)

    for rev1, rev2 in zip(v1,v2):
        if rev1 < rev2:
            return -1
        elif rev1 > rev2:
            return 1
    return 0

ver1 = "0.1"
ver2 = "1.1"
print(compareVersion(ver1,ver2))
