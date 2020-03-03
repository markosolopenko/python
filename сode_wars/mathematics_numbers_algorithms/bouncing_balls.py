

def bouncing_ball(h: float, bounce: float, window: float) -> int:
    if h > 1 and 1 > bounce > 0 and window < h:
        count = 0
        while h > window:
            count += 1
            h *= bounce
            if h > window:
                count += 1
        return count
    return -1


if __name__ == "__main__":
    print(bouncing_ball(3, 0.66, 1.5))
