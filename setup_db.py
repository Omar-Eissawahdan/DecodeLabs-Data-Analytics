import pandas as pd
import sqlite3

# مسار ملف الإكسيل بتاعك
df = pd.read_excel(r'c:\Users\MG\Downloads\Decode Lab\Data Decode Lab.xlsx')

# إنشاء قاعدة البيانات
conn = sqlite3.connect('sales_database.db')
df.to_sql('Sales', conn, index=False)
print("Database created successfully!")