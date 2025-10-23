import tushare as ts

# Set Tushare token
ts.set_token('173a9978576ef5031070621c0e2f9c851b49b5a27f4b10a84b04c414')
# Initialize Tushare Pro API
pro = ts.pro_api()
# Fetch trade calendar data
df = pro.daily(ts_code='002460.SZ', start_date='20250901', end_date='20251001')
print(df)