def sum67(nums):
    state=0
    s=0
    for n in nums:
        if state == 0:
            if n == 6:
                state=1
            else:
                s+=n
        else:
            if n == 7:
                state=0
    return s