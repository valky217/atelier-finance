# Atelier Finance: Hệ Thống Thu Thập Dữ Liệu Tài Chính & Vĩ Mô Việt Nam

Hệ thống tự động hóa thu thập dữ liệu giao dịch lịch sử của cổ phiếu, chỉ số kinh tế vĩ mô cốt lõi của Việt Nam và quản lý kho báo cáo tài chính gốc (Excel) phục vụ cho đồ án nghiên cứu định lượng tài chính.

---

## 🌟 Tính Năng Nổi Bật

*   **Dữ liệu Giá Cổ Phiếu**: Tự động tải dữ liệu lịch sử giá OHLCV của 14 cổ phiếu đại diện từ 4 ngành kinh tế (Ngân hàng, Công nghệ, Thép, Bất động sản) từ API của KB Securities (từ năm 2021 đến nay).
*   **Dữ liệu Kinh Tế Vĩ Mô**:
    *   Tốc độ tăng trưởng GDP thực tế hàng quý và chỉ số lạm phát CPI hàng tháng của Việt Nam tải trực tiếp từ **Investing.com**.
    *   Tỷ giá trung tâm USD/VND cập nhật hàng ngày từ **Vietstock**.
    *   Lãi suất điều hành (lãi suất tái cấp vốn NHNN) được mô hình hóa chính xác theo các quyết định của Ngân hàng Nhà nước Việt Nam.
*   **Quản Lý BCTC Gốc**: Tổ chức kho dữ liệu báo cáo tài chính gốc (Excel) được tải trực tiếp từ cổng giao dịch **trading.vietcap.com.vn** của VietCap cho 14 doanh nghiệp theo kỳ báo cáo năm (2021-2025) và quý (Q1/2021-Q1/2026).

---

## 📁 Cấu Trúc Thư Mục Dự Án

```text
├── BCTC/                     # Thư mục chứa 28 file báo cáo tài chính gốc (Excel) của 14 doanh nghiệp
│   ├── {Ticker}_nam.xlsx     # BCTC định kỳ năm (2021-2025)
│   └── {Ticker}_quy.xlsx     # BCTC định kỳ quý (Q1/2021 - Q1/2026)
├── DATA_SOURCES.md           # Chi tiết về nguồn dữ liệu và tính pháp lý của từng nguồn
├── DATA_SCOPE_V1.md          # Định vị phạm vi dữ liệu được thu thập
├── DATA_DICTIONARY.md        # Từ điển dữ liệu mô tả ý nghĩa tất cả các bảng và cột dữ liệu
├── DATA_QUALITY_RULES.md     # Bộ quy tắc kiểm soát chất lượng dữ liệu (data validation rules)
├── LEGAL_DATA_NOTES.md       # Phân tích rủi ro pháp lý và rào cản cào quét dữ liệu (Web Scraping)
├── download_real_data.py     # Script Python chính thực hiện kết nối API và thu thập dữ liệu
├── industries.csv            # Danh mục các ngành kinh tế khảo sát
├── stocks.csv                # Danh sách thông tin cơ bản của 14 mã cổ phiếu
├── stock_prices.csv          # Dữ liệu giá giao dịch lịch sử hàng ngày của 14 cổ phiếu
├── macro_indicators.xlsx     # File Excel tổng hợp chỉ số vĩ mô (Tỷ giá, GDP, CPI, Lãi suất)
├── macro_indicators.csv      # File CSV tổng hợp toàn bộ số liệu vĩ mô
├── macro_ty_gia.csv          # Chi tiết lịch sử Tỷ giá trung tâm
├── macro_gdp.csv             # Chi tiết lịch sử Tăng trưởng GDP hàng quý
├── macro_cpi.csv             # Chi tiết lịch sử Chỉ số lạm phát CPI hàng tháng
└── macro_lai_suat.csv        # Chi tiết lịch sử Lãi suất điều hành
```

---

## 🚀 Hướng Dẫn Cài Đặt & Sử Dụng

### 1. Yêu cầu hệ thống
*   Hệ điều hành: Windows / macOS / Linux.
*   Cài đặt sẵn **Python 3.8** trở lên.

### 2. Cài đặt các thư viện phụ thuộc
Mở terminal tại thư mục dự án và chạy lệnh sau để cài đặt các thư viện cần thiết:
```bash
pip install pandas requests openpyxl beautifulsoup4
```

### 3. Thực thi thu thập dữ liệu vĩ mô và giá cổ phiếu
Chạy lệnh dưới đây để khởi chạy script cập nhật dữ liệu mới nhất đến ngày hôm nay:
```bash
python download_real_data.py
```
*Sau khi chạy xong, toàn bộ các file CSV và Excel dữ liệu giá/vĩ mô trong thư mục sẽ được cập nhật đồng bộ.*

---

## 📄 Hệ Thống Tài Liệu Kèm Theo

Dự án cung cấp bộ tài liệu đi kèm rất chi tiết giúp bạn dễ dàng thuyết trình hoặc đưa vào báo cáo đồ án:
1.  [DATA_SOURCES.md](DATA_SOURCES.md): Hướng dẫn chi tiết cách trích nguồn dữ liệu và đánh giá từng nhà cung cấp.
2.  [DATA_SCOPE_V1.md](DATA_SCOPE_V1.md): Khung phạm vi và định hướng thiết kế dữ liệu.
3.  [DATA_DICTIONARY.md](DATA_DICTIONARY.md): Từ điển dữ liệu chuẩn hóa cho các lập trình viên/nhà phân tích.
4.  [DATA_QUALITY_RULES.md](DATA_QUALITY_RULES.md): Hệ thống quy tắc ràng buộc đảm bảo dữ liệu không bị lỗi (như giá âm, sai lệch tổng tài sản, v.v.).
5.  [LEGAL_DATA_NOTES.md](LEGAL_DATA_NOTES.md): Ghi chú pháp lý quan trọng khi chuyển giao từ môi trường học thuật sang sản phẩm thương mại.
