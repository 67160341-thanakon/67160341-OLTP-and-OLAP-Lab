import sqlite3
import pandas as pd
import sys

db_path = sys.argv[1] if len(sys.argv) > 1 else 'data/warehouse.db'
conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM sales", conn)

# ---------------------------------------------------------
# 4.2 Python P1: Pivot province x month + Total margins
# ---------------------------------------------------------
p1 = df.pivot_table(
    index='province',
    columns='month',
    values='amount',
    aggfunc='sum',
    fill_value=0,
    margins=True,
    margins_name='Total'
)
p1.to_csv('pivot_province_month.csv')
print("--- P1: Pivot Province x Month ---")
print(p1)

# ---------------------------------------------------------
# 4.3 Python P2: Filter September -> category x province
# ---------------------------------------------------------
df_sep = df[df['month'] == '2026-09']
p2 = df_sep.pivot_table(
    index='category',
    columns='province',
    values='amount',
    aggfunc='sum',
    fill_value=0
)
p2.to_csv('pivot_september.csv')
print("\n--- P2: Pivot September (Category x Province) ---")
print(p2)

# ---------------------------------------------------------
# 4.4 Assert Grand Total ของ P1 กับ df['amount'].sum()
# ---------------------------------------------------------
grand_total_p1 = p1.loc['Total', 'Total']
grand_total_df = df['amount'].sum()

assert grand_total_p1 == grand_total_df, f"Mismatch: {grand_total_p1} != {grand_total_df}"
print(f"\n[PASS] Assert Success! Grand Total = {grand_total_p1}")

conn.close()