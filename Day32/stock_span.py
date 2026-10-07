def stock_span(prices):
    spans = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        if not stack:
            spans[i] = i + 1
        else:
            spans[i] = i - stack[-1]

        stack.append(i)

    return spans


prices = [100, 80, 60, 70, 60, 75, 85]

result = stock_span(prices)

print("Stock prices:", prices)
print("Stock spans:", result)