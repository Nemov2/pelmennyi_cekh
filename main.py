from my_func import pelmenMashineCount, testoMashineCount, meatMashineCount

print("Введите суточную выроботку готовой продукции: ")
qDay = int(input())

print("Введите длительность смены: ")
t = int(input())

print("Введите массовую долю теста в готовой продукции: ")
testo_part = int(input())

print("Введите производительность пельменного автомата: ")
p_pa = int(input())

print("Введите производительность тестомесильной машины: ")
p_tm = int(input())

print("Введите производительность куттера: ")
p_k = int(input())

print("Количество пельменных автоматов:")
print(pelmenMashineCount(qDay, t, p_pa))
print("Количество тестомесильных машин:")
print(testoMashineCount(qDay, testo_part, p_tm))
print("Количество куттеров:")
print(meatMashineCount(qDay, testo_part, p_k))
