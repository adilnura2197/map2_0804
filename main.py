#6
roy = ["Ali", "Vali", "Hasan"]
print(f"Ro'yxat: {roy}")

natija = list(map(lambda x: "Mr. " + x, roy))
print(natija)


#7
roy = [100, 200, 300]
print(f"Ro'yxat: {roy}")

natija = list(map(lambda el: str(el), roy))
print(natija)


#8
roy = ["1", "2", "3", "4"]
print(f"Ro'yxat: {roy}")

natija = list(map(lambda el: int(el), roy))
print(natija)


#9
roy = [5, 10, 15, 20]
print(f"Ro'yxat: {roy}")

natiaja = list(map(lambda el: el / 3, roy))
print(natiaja)


#10
roy = ["hello", "world"]
print(f"Ro'yxat: {roy}")

natija = list(map(lambda el: el + '!', roy))
print(natija)
