def separator(num):
    amount = []
    if num < 1000:
        amount.insert(0, str(num))
    else:
        while num > 0:
            result = num % 1000
            num //= 1000
            amount.insert(0, str(result).zfill(3))
            if num < 100 and num != 0:
                result = num % 1000
                amount.insert(0, str(result))
                break

    return ','.join(amount)
