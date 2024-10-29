import pandas as pd
import random
import matplotlib.pyplot as plt
students_grades = {
    "name": ["Анна", "Иван", "Мария", "Сергей", "Ольга", "Петр", "Елена", "Алексей", "Наталья", "Дмитрий"],
    "химия": random.sample(range(1, 101), 10),
    "физика": random.sample(range(1, 101), 10),
    "математика": [1,45,47,54,65,99,37,23,54,100],
    "биология": random.sample(range(1, 101), 10),
    "информатика": random.sample(range(1, 101), 10)
}

df = pd.DataFrame(students_grades)
print(df)
for i in df.columns[1:]:
    print(f'Средняя оценка по {i} = {df[i].mean()}')

for i in df.columns[1:]:
    print(f'Медиана по {i} = {df[i].median()}')

df.boxplot(column='математика')
plt.show()

Q1 = df['математика'].quantile(0.25)
Q3 = df['математика'].quantile(0.75)

IQR = Q3 - Q1
downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df['математика'] > downside) & (df['математика'] < upside)]
df_new.boxplot(column='математика')
plt.show()


