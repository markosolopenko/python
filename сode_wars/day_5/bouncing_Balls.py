def bouncingBall(h: float, bounce: float, window: float) -> int:
    if h > 1 and bounce > 0 and bounce < 1 and window < h:
        count = 0
        while h > window:
            count += 1
            h *= bounce
            if h > window:
                count+=1
        return count
    return -1

if __name__ == "__main__":
    print(bouncingBall(3, 0.66, 1.5))
