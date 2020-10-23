def birthdayCakeCandles(candles):
    tallest_candle = max(candles)
    print(tallest_candle)
    total_talest_candles = 0
    for candle in candles:
        if candle == tallest_candle:
            total_talest_candles+=1
    return total_talest_candles




candles_count = int(input().strip())

candles = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(candles)
