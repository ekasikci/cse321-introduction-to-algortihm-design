def findFaultyFuse(fuses, l, r):
    while l <= r:
        mid = l + (r - l) // 2
        if fuses[mid] == 0:
            if(fuses[mid - 1] == 1):
                return mid
            r = mid - 1
        else:
            l = mid + 1
    return -1
# Test case
fuses = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
faulty_fuse_index = findFaultyFuse(fuses, 0, len(fuses))
print("Faulty fuse index: ", faulty_fuse_index)
