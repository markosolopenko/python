def sjf(jobs, index):
    interested_number = jobs[index]
    count = 0
    for a in jobs[index:]:
        if a < interested_number:
            count += a
    for c in jobs[:index+1]:
        if c <= interested_number:
            count += c
    return count



if __name__ == '__main__':
    print(sjf([3,10,20,1,2], 0))