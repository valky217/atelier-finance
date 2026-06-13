import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

import csv
import datetime
import math
import os
import random
import time
import requests
import pandas as pd

OUTPUT_DIR = r"d:\KLTN"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

COLLECTED_AT = "2026-06-13 17:44:45"
TICKERS = ["VCB", "TCB", "MBB", "CTG", "FPT", "CMG", "VGI", "HPG", "HSG", "NKG", "VHM", "VIC", "NLG", "DXG"]


# Ngày hôm nay động động
TODAY_STR_API = datetime.date.today().strftime("%d-%m-%Y")
print(f"=== BAT DAU KET NOI NGUON DU LIEU WEB TRUC TIEP (MOC MOI DEN {TODAY_STR_API}) ===")

def safe_save_excel(df_dict, filename):
    """Lưu file Excel an toàn, thông báo lỗi nếu file bị mở khóa bởi phần mềm khác."""
    path = os.path.join(OUTPUT_DIR, filename)
    try:
        with pd.ExcelWriter(path, engine="openpyxl") as writer:
            for sheet_name, df in df_dict.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        print(f"Da ghi file excel {filename}")
    except PermissionError:
        print(f"Loi: Khong the ghi file {filename}. Vui long dong file neu no dang duoc mo bang Excel!")
    except Exception as e:
        print(f"Loi khac khi ghi {filename}: {e}")

def safe_save_csv(df, filename):
    """Lưu file CSV an toàn, thông báo lỗi nếu file bị khóa."""
    path = os.path.join(OUTPUT_DIR, filename)
    try:
        df.to_csv(path, index=False, encoding="utf-8-sig")
        print(f"Da ghi file CSV {filename}")
    except PermissionError:
        print(f"Loi: Khong the ghi file CSV {filename}. Vui long dong file neu no dang duoc mo bang Excel!")
    except Exception as e:
        print(f"Loi khac khi ghi CSV {filename}: {e}")

# ==========================================
# PART 1: industries.csv
# ==========================================
print("Ghi file industries.csv...")
industries_data = [
    ["BANK", "Ngân hàng", "https://vietstock.vn", COLLECTED_AT],
    ["TECH", "Công nghệ thông tin", "https://vietstock.vn", COLLECTED_AT],
    ["STEEL", "Thép & Vật liệu xây dựng", "https://vietstock.vn", COLLECTED_AT],
    ["RE", "Bất động sản", "https://vietstock.vn", COLLECTED_AT]
]
df_ind = pd.DataFrame(industries_data, columns=["ma_nganh", "ten_nganh", "nguon_du_lieu", "ngay_thu_thap"])
safe_save_csv(df_ind, "industries.csv")

# ==========================================
# PART 2: stocks.csv
# ==========================================
print("Ghi file stocks.csv...")
stocks_data = [
    ["VCB", "Ngân hàng TMCP Ngoại thương Việt Nam", "BANK", "HOSE", "https://vietstock.vn", COLLECTED_AT],
    ["TCB", "Ngân hàng TMCP Kỹ thương Việt Nam", "BANK", "HOSE", "https://vietstock.vn", COLLECTED_AT],
    ["MBB", "Ngân hàng TMCP Quân đội", "BANK", "HOSE", "https://vietstock.vn", COLLECTED_AT],
    ["CTG", "Ngân hàng TMCP Công Thương Việt Nam", "BANK", "HOSE", "https://vietstock.vn", COLLECTED_AT],
    ["FPT", "Công ty Cổ phần FPT", "TECH", "HOSE", "https://vietstock.vn", COLLECTED_AT],
    ["CMG", "Công ty Cổ phần Tập đoàn Công nghệ CMC", "TECH", "HOSE", "https://vietstock.vn", COLLECTED_AT],
    ["VGI", "Tổng Công ty Cổ phần Đầu tư Quốc tế Viettel", "TECH", "UPCoM", "https://vietstock.vn", COLLECTED_AT],
    ["HPG", "Công ty Cổ phần Tập đoàn Hòa Phát", "STEEL", "HOSE", "https://vietstock.vn", COLLECTED_AT],
    ["HSG", "Công ty Cổ phần Tập đoàn Hoa Sen", "STEEL", "HOSE", "https://vietstock.vn", COLLECTED_AT],
    ["NKG", "Công ty Cổ phần Thép Nam Kim", "STEEL", "HOSE", "https://vietstock.vn", COLLECTED_AT],
    ["VHM", "Công ty Cổ phần Vinhomes", "RE", "HOSE", "https://vietstock.vn", COLLECTED_AT],
    ["VIC", "Tập đoàn Vingroup", "RE", "HOSE", "https://vietstock.vn", COLLECTED_AT],
    ["NLG", "Công ty Cổ phần Đầu tư Nam Long", "RE", "HOSE", "https://vietstock.vn", COLLECTED_AT],
    ["DXG", "Công ty Cổ phần Tập đoàn Đất Xanh", "RE", "HOSE", "https://vietstock.vn", COLLECTED_AT]
]
df_stk = pd.DataFrame(stocks_data, columns=["ma_co_phieu", "ten_doanh_nghiep", "ma_nganh", "san_giao_dich", "nguon_du_lieu", "ngay_thu_thap"])
safe_save_csv(df_stk, "stocks.csv")

# ==========================================
# PART 3: stock_prices.csv
# ==========================================
print(f"Thu thap gia tu API KB Securities tu 2021 den {TODAY_STR_API}...")
prices_rows = []
headers_kbs = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

for ticker in TICKERS:
    success = False
    retries = 3
    url = f"https://kbbuddywts.kbsec.com.vn/iis-server/investment/stocks/{ticker}/data_day"
    params = {
        "sdate": "01-01-2021",
        "edate": TODAY_STR_API
    }
    
    while retries > 0 and not success:
        try:
            print(f"  Gia {ticker}...")
            r = requests.get(url, params=params, headers=headers_kbs, timeout=10)
            if r.status_code == 200:
                data = r.json()
                if 'data_day' in data:
                    prices = data['data_day']
                    print(f"    Thanh cong! Tai duoc {len(prices)} dong.")
                    for row in prices:
                        t_str = row['t'].split(' ')[0]
                        open_val = int(float(row['o']) * 1000) if 'o' in row else 0
                        high_val = int(float(row['h']) * 1000) if 'h' in row else 0
                        low_val = int(float(row['l']) * 1000) if 'l' in row else 0
                        close_val = int(float(row['c']) * 1000) if 'c' in row else 0
                        adj_close_val = close_val
                        volume_val = int(row['v']) if 'v' in row else 0
                        
                        prices_rows.append([
                            ticker,
                            t_str,
                            open_val,
                            high_val,
                            low_val,
                            close_val,
                            adj_close_val,
                            volume_val,
                            "https://kbbuddywts.kbsec.com.vn",
                            COLLECTED_AT
                        ])
                    success = True
                else:
                    print(f"    Khong tim thay khoa data_day trong JSON, retry...")
                    retries -= 1
                    time.sleep(2)
            else:
                print(f"    Loi status code: {r.status_code}, retry...")
                retries -= 1
                time.sleep(2)
        except Exception as e:
            print(f"    Loi ket noi ticker {ticker}: {type(e).__name__}, retry...")
            retries -= 1
            time.sleep(3)
    time.sleep(0.5)

df_prices = pd.DataFrame(prices_rows, columns=[
    "ma_co_phieu", "ngay", "gia_mo_cua_vnd", "gia_cao_nhat_vnd", "gia_thap_nhat_vnd",
    "gia_dong_cua_vnd", "gia_dong_cua_dieu_chinh_vnd", "khoi_luong_giao_dich_co_phieu",
    "nguon_du_lieu", "ngay_thu_thap"
])
safe_save_csv(df_prices, "stock_prices.csv")

# ==========================================
# PART 5: macro_indicators (Excel & CSV)
# ==========================================
print("Thu thap du lieu vi mo tu Vietstock va SBV...")
import json
from bs4 import BeautifulSoup

def get_vietstock_token():
    urltoken = 'https://finance.vietstock.vn/du-lieu-vi-mo/'
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    r = requests.get(urltoken, headers={'User-Agent': ua}, timeout=15)
    soup = BeautifulSoup(r.content, 'html.parser')
    stoken = soup.body.input
    stoken = str(stoken)
    listtoken = stoken.split()
    xre = []
    for i in listtoken[1:]:
        i = i.replace('=', ':').replace('"', '')
        xre.append(i)
    token_val = str(xre[2]).replace('value:', '').replace('/>', '')
    dic = dict(r.cookies.get_dict())
    revtoken = dic['__RequestVerificationToken']
    revasp = dic['ASP.NET_SessionId']
    return revasp, revtoken, token_val

print("  Dang lay session token tu Vietstock...")
try:
    asp_m, rtoken_m, tken_m = get_vietstock_token()
    print("  Lay token thanh cong.")
except Exception as e:
    print(f"  Loi khi lay token tu Vietstock: {e}")
    raise e

headers_vs = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Cookie': f'language=vi-VN; ASP.NET_SessionId={asp_m}; __RequestVerificationToken={rtoken_m}; Theme=Light'
}
url_vs = 'https://finance.vietstock.vn/data/reportdatatopbynormtype'

def fetch_vietstock_macro(payload):
    payload['__RequestVerificationToken'] = tken_m
    r = requests.post(url_vs, headers=headers_vs, data=payload, timeout=15)
    if r.status_code == 200:
        content_str = r.content.decode('utf-8-sig')
        data_json = json.loads(content_str)
        return data_json.get('data', [])
    else:
        raise Exception(f"Request that bai, status code: {r.status_code}")

ty_gia_rows = []
gdp_rows = []
cpi_rows = []
lai_suat_rows = []

# A. Tỷ giá USD/VND (normTypeID: 53)
print("  Lay ty gia USD/VND tu Vietstock...")
payload_fx = {
    'type': '1',
    'fromYear': 2021,
    'toYear': datetime.datetime.now().year,
    'from': '2021-01-01',
    'to': datetime.date.today().strftime("%Y-%m-%d"),
    'normTypeID': '53'
}
try:
    data_fx = fetch_vietstock_macro(payload_fx)
    df_raw_fx = pd.DataFrame(data_fx)
    if not df_raw_fx.empty:
        df_fx_filtered = df_raw_fx[df_raw_fx['NormName'] == 'Tỷ giá trung tâm (từ 04/01/2016)'].copy()
        df_fx_filtered['date_conv'] = pd.to_datetime(df_fx_filtered['ReportTime'], format='%d/%m/%Y', errors='coerce')
        df_fx_filtered = df_fx_filtered.sort_values(by='date_conv')
        
        for _, row in df_fx_filtered.iterrows():
            if pd.notna(row['date_conv']) and row['NormValue'] is not None:
                dt_str = row['date_conv'].strftime('%Y-%m-%d')
                val = float(row['NormValue'])
                ty_gia_rows.append([
                    "Ty_Gia_USD_VND", "Ngay", dt_str, val, "VND/USD",
                    "https://finance.vietstock.vn", COLLECTED_AT
                ])
        print(f"    Lay thanh cong {len(ty_gia_rows)} dong ty gia trung tam.")
except Exception as e:
    print(f"    Loi khi tai ty gia tu Vietstock: {e}")

# B. GDP Tăng trưởng (vn.investing.com: Event ID 1853)
print("  Lay chi so tang truong GDP tu vn.investing.com...")
url_gdp = "https://vn.investing.com/economic-calendar/vietnamese-gdp-1853"
try:
    headers_inv = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    r_gdp = requests.get(url_gdp, headers=headers_inv, timeout=15)
    soup_gdp = BeautifulSoup(r_gdp.content, 'html.parser')
    script_gdp = soup_gdp.find('script', id='__NEXT_DATA__')
    if script_gdp:
        data_gdp = json.loads(script_gdp.string)
        state_gdp = data_gdp.get('props', {}).get('pageProps', {}).get('state', {})
        ec_store_gdp = state_gdp.get('economicCalendarEventStore', {})
        occurrences_gdp = ec_store_gdp.get('occurrences', [])
        
        gdp_temp_rows = []
        for occ in occurrences_gdp:
            val = occ.get('actual')
            if val is None:
                continue
            
            occ_time_str = occ.get('occurrence_time')
            dt = datetime.datetime.strptime(occ_time_str, "%Y-%m-%dT%H:%M:%SZ")
            
            # Map release month to quarter
            if dt.month in [3, 4]:
                ref_q = "Q1"
                ref_y = dt.year
            elif dt.month in [6, 7]:
                ref_q = "Q2"
                ref_y = dt.year
            elif dt.month in [9, 10]:
                ref_q = "Q3"
                ref_y = dt.year
            elif dt.month in [12, 1]:
                ref_q = "Q4"
                ref_y = dt.year - 1 if dt.month == 1 else dt.year
            else:
                ref_q = f"Q{(dt.month - 1) // 3 + 1}"
                ref_y = dt.year
                
            if ref_y < 2021:
                continue
                
            time_str = f"{ref_y}-{ref_q}"
            gdp_temp_rows.append({
                "time_str": time_str,
                "val": float(val)
            })
            
        gdp_temp_rows = sorted(gdp_temp_rows, key=lambda x: x['time_str'])
        for row in gdp_temp_rows:
            gdp_rows.append([
                "GDP_Tang_Truong", "Quy", row['time_str'], row['val'], "%",
                "https://vn.investing.com", COLLECTED_AT
            ])
        print(f"    Lay thanh cong {len(gdp_rows)} dong GDP.")
    else:
        print("    Loi: Khong tim thay the script __NEXT_DATA__ tren trang GDP.")
except Exception as e:
    print(f"    Loi khi tai GDP tu vn.investing.com: {e}")

# C. CPI Hàng tháng (vn.investing.com: Event ID 1851)
print("  Lay chi so CPI hang thang tu vn.investing.com...")
url_cpi = "https://vn.investing.com/economic-calendar/vietnamese-cpi-1851"
try:
    headers_inv = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    r_cpi = requests.get(url_cpi, headers=headers_inv, timeout=15)
    soup_cpi = BeautifulSoup(r_cpi.content, 'html.parser')
    script_cpi = soup_cpi.find('script', id='__NEXT_DATA__')
    if script_cpi:
        data_cpi = json.loads(script_cpi.string)
        state_cpi = data_cpi.get('props', {}).get('pageProps', {}).get('state', {})
        ec_store_cpi = state_cpi.get('economicCalendarEventStore', {})
        occurrences_cpi = ec_store_cpi.get('occurrences', [])
        
        cpi_temp_rows = []
        for occ in occurrences_cpi:
            val = occ.get('actual')
            if val is None:
                continue
            
            occ_time_str = occ.get('occurrence_time')
            dt = datetime.datetime.strptime(occ_time_str, "%Y-%m-%dT%H:%M:%SZ")
            
            ref_period = occ.get('reference_period', '')
            try:
                ref_m = int(ref_period.replace('Tháng', '').strip())
            except:
                ref_m = dt.month - 1 if dt.month > 1 else 12
                
            if ref_m == 12 and dt.month == 1:
                ref_y = dt.year - 1
            else:
                ref_y = dt.year
                
            if ref_y < 2021:
                continue
                
            time_str = f"{ref_y}-{ref_m:02d}"
            cpi_temp_rows.append({
                "time_str": time_str,
                "val": float(val)
            })
            
        cpi_temp_rows = sorted(cpi_temp_rows, key=lambda x: x['time_str'])
        for row in cpi_temp_rows:
            cpi_rows.append([
                "CPI_YoY", "Thang", row['time_str'], row['val'], "%",
                "https://vn.investing.com", COLLECTED_AT
            ])
        print(f"    Lay thanh cong {len(cpi_rows)} dong CPI.")
    else:
        print("    Loi: Khong tim thay the script __NEXT_DATA__ tren trang CPI.")
except Exception as e:
    print(f"    Loi khi tai CPI tu vn.investing.com: {e}")

# D. Lãi suất điều hành (SBV: Lịch sử Lãi suất tái cấp vốn chính thức từ 2021 đến nay)
print("  Xay dung lai suat dieu hanh (Lai suat tai cap von NHNN)...")
start_y = 2021
end_y = datetime.datetime.now().year
end_m = datetime.datetime.now().month

for year in range(start_y, end_y + 1):
    for month in range(1, 12 + 1):
        if year == end_y and month > end_m:
            continue
        dt_benchmark = datetime.date(year, month, 28)
        if dt_benchmark < datetime.date(2022, 9, 23):
            rate = 4.0
        elif dt_benchmark < datetime.date(2022, 10, 25):
            rate = 5.0
        elif dt_benchmark < datetime.date(2023, 4, 3):
            rate = 6.0
        elif dt_benchmark < datetime.date(2023, 5, 25):
            rate = 5.5
        elif dt_benchmark < datetime.date(2023, 6, 19):
            rate = 5.0
        else:
            rate = 4.5
        
        lai_suat_rows.append([
            "Lai_Suat_Dieu_Hanh", "Thang", f"{year}-{month:02d}", rate, "%",
            "https://www.sbv.gov.vn", COLLECTED_AT
        ])
print(f"    Xay dung thanh cong {len(lai_suat_rows)} dong lai suat.")

cols_macro = ["chi_so", "ky", "thoi_gian", "gia_tri", "don_vi_tinh", "nguon_du_lieu", "ngay_thu_thap"]
df_ty_gia = pd.DataFrame(ty_gia_rows, columns=cols_macro)
df_gdp = pd.DataFrame(gdp_rows, columns=cols_macro)
df_cpi = pd.DataFrame(cpi_rows, columns=cols_macro)
df_lai_suat = pd.DataFrame(lai_suat_rows, columns=cols_macro)

# Lưu Excel 4 sheets
safe_save_excel({
    "Tỷ giá USD-VND": df_ty_gia,
    "Tăng trưởng GDP": df_gdp,
    "Chỉ số CPI": df_cpi,
    "Lãi suất": df_lai_suat
}, "macro_indicators.xlsx")

# Đồng thời lưu các CSV
safe_save_csv(df_ty_gia, "macro_ty_gia.csv")
safe_save_csv(df_gdp, "macro_gdp.csv")
safe_save_csv(df_cpi, "macro_cpi.csv")
safe_save_csv(df_lai_suat, "macro_lai_suat.csv")

df_full_macro = pd.concat([df_ty_gia, df_gdp, df_cpi, df_lai_suat], ignore_index=True)
safe_save_csv(df_full_macro, "macro_indicators.csv")

print("=== COMPLETE HOAN THONG NHAT ===")
