# Все импорты в начале файла
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Загрузка датасета
df = pd.read_csv('/Users/kirillstepanuik/Documents/BostonHousing.csv')

# 2. Преобразование столбца tax в pricing (tax * 10000) с использованием map
df['pricing'] = df['tax'].map(lambda x: x * 10000)

# 3. Проверка информации о датасете: типы данных, пропуски, категориальные признаки
print("Информация о датасете:")
print(df.info())
print("\nПропущенные значения:")
print(df.isnull().sum())

# Проверка категориальных признаков
# Столбец 'chas' является бинарным (0/1), что делает его пригодным для регрессии без дополнительного кодирования
print("\nУникальные значения в 'chas':", df['chas'].unique())

# 4. Обработка пропусков (если есть)
# Например, для столбца 'rm' (если есть пропуски) заменим их медианным значением
if df['rm'].isnull().any():
    df['rm'] = df['rm'].fillna(df['rm'].median())
    print("\nПропущенные значения в 'rm' заменены медианой.")
print("\nПропущенные значения после обработки:")
print(df.isnull().sum())

# 5. Подготовка признаков и целевой переменной
# Исключаем 'pricing' (целевая переменная), 'tax' (уже преобразован в pricing) и 'medv' (если есть)
X = df.drop(['pricing', 'tax'], axis=1)
if 'medv' in df.columns:
    X = X.drop('medv', axis=1)
y = df['pricing']

# 6. Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Масштабирование признаков
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 8. Обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# 9. Предсказания
y_pred = model.predict(X_test_scaled)

# 10. Оценка модели
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nМетрики модели:")
print(f"Среднеквадратичная ошибка (MSE): {mse:.2f}")
print(f"Корень из среднеквадратичной ошибки (RMSE): {rmse:.2f}")
print(f"Коэффициент детерминации (R²): {r2:.2f}")

# 11. Важность признаков (коэффициенты модели)
feature_importance = pd.DataFrame({
    'Признак': X.columns,
    'Коэффициент': model.coef_
})
feature_importance = feature_importance.sort_values(by='Коэффициент', key=abs, ascending=False)

print("\nВажность признаков:")
print(feature_importance)

# 12. Визуализация фактических и предсказанных цен
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Фактическая стоимость')
plt.ylabel('Предсказанная стоимость')
plt.title('Фактическая vs Предсказанная стоимость домов')
plt.tight_layout()

# Сохранение графика
plt.savefig('/Users/kirillstepanuik/PyProject/lab_5/actual_vs_predicted_pricing.png')
plt.show()