import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading dataset...")
file_path = r'c:\Users\MG\Downloads\Decode Lab\Data Decode Lab.xlsx'

df = pd.read_excel(file_path)

print("\n--- Basic Statistics ---")
stats = df[['UnitPrice', 'Quantity', 'TotalPrice']].describe()
print(stats)

corr_value = df['UnitPrice'].corr(df['Quantity'])
print(f"\nPearson Correlation (Price vs Quantity): {corr_value:.4f}")

print("\nPlotting data...")
plt.style.use('dark_background')
fig = plt.figure(figsize=(14, 8))

ax1 = fig.add_subplot(221)
sns.boxplot(x=df['TotalPrice'], color='skyblue', ax=ax1)
ax1.set_title('Outliers in Total Price')

ax2 = fig.add_subplot(222)
sns.scatterplot(data=df, x='Quantity', y='UnitPrice', alpha=0.6, color='coral', ax=ax2)
ax2.set_title('Price vs Quantity Correlation')
ax3 = fig.add_subplot(212)
product_sales = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
sns.barplot(x=product_sales.index, y=product_sales.values, palette='viridis', ax=ax3)
ax3.set_title('Total Quantity Sold per Product')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()