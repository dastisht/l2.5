n = ["Bob1", "Bob2", "Bob3"]
r = [100, 200, 150]
b = ["10.25%", "5%", "12.5%"]
result = {n: r * float(bonus.strip('%')) / 100 for n, r, bonus in zip(n, r, b)}
print(result)
