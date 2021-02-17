import matplotlib.pyplot as plt

principal = 10000
interest_rate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interest_rate

plt.plot(values)
plt.title('5% Growth, Compounded Annually')
plt.xlabel('Years of Compounding')
plt.ylabel('Value of Principla ($)')
plt.savefig('5%-Growth-Compounded-Annually')
plt.show()
