def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    amount_of_month = 1
    first = savingperMonth
    savingperMonth = 0
    if startPriceOld >= startPriceNew:
        return [0,startPriceOld - startPriceNew]
    while True:
        if amount_of_month % 2 == 0:
            percentLossByMonth += 0.5
        reload_cos_old_car = startPriceOld * percentLossByMonth / 100
        startPriceOld = startPriceOld - reload_cos_old_car
        reload_cost_new_car = startPriceNew * percentLossByMonth / 100
        startPriceNew = startPriceNew - reload_cost_new_car
        amount_of_month += 1
        savingperMonth += first
        if (startPriceOld + savingperMonth) - startPriceNew > 0:
            break

    return [amount_of_month -1, round((startPriceOld + savingperMonth) - startPriceNew, 0)]
if __name__ == "__main__":
    print(nbMonths(2000, 8000, 1000, 1.5))