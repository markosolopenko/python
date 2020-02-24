# Converting hours, minutes and seconds to milliseconds
def past(hours, minutes, seconds):
    return (hours * 3600 + minutes * 60 + seconds) * 1000
print(past(0,1,1))