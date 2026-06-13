# TỪ ĐIỂN DỮ LIỆU (DATA DICTIONARY)

---

## 1. Bảng Danh Mục Ngành (`industries.csv`)
Lưu trữ danh mục các ngành được khảo sát.

| Tên Cột | Kiểu Dữ Liệu | Ví dụ | Giải thích |
| :--- | :---: | :--- | :--- |
| `ma_nganh` | String (Key) | `BANK` | Mã định danh viết tắt của ngành (BANK, TECH, STEEL, RE). |
| `ten_nganh` | String | `Ngân hàng` | Tên đầy đủ của ngành. |
| `nguon_du_lieu` | String (URL) | `https://vietstock.vn` | Nguồn phân loại ngành. |
| `ngay_thu_thap` | DateTime | `2026-06-13 17:44:45` | Thời điểm ghi nhận dữ liệu vào hệ thống (`YYYY-MM-DD HH:MM:SS`). |

---

## 2. Bảng Danh Sách Cổ Phiếu (`stocks.csv`)
Lưu trữ danh sách thông tin cơ bản của 14 mã cổ phiếu.

| Tên Cột | Kiểu Dữ Liệu | Ví dụ | Giải thích |
| :--- | :---: | :--- | :--- |
| `ma_co_phieu` | String (Key) | `VCB` | Mã chứng khoán. |
| `ten_doanh_nghiep` | String | `Tập đoàn Hòa Phát` | Tên đầy đủ của công ty/ngân hàng niêm yết. |
| `ma_nganh` | String (FK) | `STEEL` | Mã ngành. |
| `san_giao_dich` | String | `HOSE` | Sàn niêm yết cổ phiếu (HOSE, HNX hoặc UPCoM). |
| `nguon_du_lieu` | String (URL) | `https://vietstock.vn` | Nguồn thông tin doanh nghiệp. |
| `ngay_thu_thap` | DateTime | `2026-06-13 17:44:45` | Thời điểm ghi nhận dữ liệu vào hệ thống (`YYYY-MM-DD HH:MM:SS`). |

---

## 3. Bảng Lịch Sử Giá Cổ Phiếu (`stock_prices.csv`)
Lưu trữ dữ liệu giao dịch hàng ngày của các mã cổ phiếu từ năm 2021 đến nay.

| Tên Cột | Kiểu Dữ Liệu | Đơn Vị | Ví dụ | Giải thích |
| :--- | :---: | :---: | :--- | :--- |
| `ma_co_phieu` | String (FK) | - | `FPT` | Mã cổ phiếu giao dịch. |
| `ngay` | Date | - | `2026-06-12` | Ngày diễn ra phiên giao dịch (`YYYY-MM-DD`). |
| `gia_mo_cua_vnd` | Integer | VND | `132000` | Giá khớp lệnh đầu tiên trong phiên giao dịch. |
| `gia_cao_nhat_vnd` | Integer | VND | `135200` | Giá khớp lệnh cao nhất đạt được trong phiên. |
| `gia_thap_nhat_vnd` | Integer | VND | `131500` | Giá khớp lệnh thấp nhất chạm tới trong phiên. |
| `gia_dong_cua_vnd` | Integer | VND | `134500` | Giá khớp lệnh cuối cùng khi đóng cửa phiên. |
| `gia_dong_cua_dieu_chinh_vnd` | Integer | VND | `134500` | Giá đóng cửa đã điều chỉnh sau các sự kiện chia cổ tức/tách cổ phiếu. |
| `khoi_luong_giao_dich_co_phieu` | Integer | Cổ phiếu | `2540000` | Tổng khối lượng cổ phiếu giao dịch thành công trong phiên. |
| `nguon_du_lieu` | String (URL) | - | `https://kbbuddywts.kbsec.com.vn` | Nguồn dữ liệu. |
| `ngay_thu_thap` | DateTime | - | `2026-06-13 17:44:45` | Thời điểm ghi nhận dữ liệu vào hệ thống (`YYYY-MM-DD HH:MM:SS`). |

---

## 4. Thư Mục Báo Cáo Tài Chính Gốc (`BCTC/`)
Thư mục chứa các tệp tin báo cáo tài chính gốc định dạng Excel của 14 doanh nghiệp. Mỗi doanh nghiệp có 2 tệp tin:
-  Báo cáo tài chính theo năm (từ 2021 đến 2025).
-  Báo cáo tài chính theo quý (từ Q1/2021 đến Q1/2026).

Mỗi tệp tin Excel chứa 4 sheets:
1. **Bảng cân đối kế toán**: Lưu trữ các chỉ tiêu về tài sản ngắn/dài hạn, nợ phải trả, vốn chủ sở hữu tại các thời điểm cuối kỳ báo cáo.
2. **Kết quả kinh doanh**: Lưu trữ số liệu về doanh thu bán hàng, giá vốn, doanh thu tài chính, chi phí bán hàng, chi phí quản lý và lợi nhuận sau thuế của kỳ báo cáo.
3. **Lưu chuyển tiền tệ**: Trình bày dòng tiền lưu chuyển từ 3 hoạt động chính (Hoạt động kinh doanh, Hoạt động đầu tư, Hoạt động tài chính).
4. **Thuyết minh**: Chi tiết hóa các chỉ tiêu trọng yếu trên 3 báo cáo tài chính chính thức.

*Nguồn gốc dữ liệu*: Được tải trực tiếp từ hệ thống giao dịch trực tuyến của VietCap ([trading.vietcap.com.vn](https://trading.vietcap.com.vn)).

---

## 5. Bảng Chỉ Số Vĩ Mô (`macro_indicators.xlsx` & các file CSV)
Lưu trữ 4 chỉ số vĩ mô quan trọng: Tỷ giá, GDP tăng trưởng, CPI và Lãi suất.

| Tên Cột | Kiểu Dữ Liệu | Ví dụ | Giải thích |
| :--- | :---: | :--- | :--- |
| `chi_so` | String | `CPI_YoY` | Chỉ số vĩ mô (`Ty_Gia_USD_VND`, `GDP_Tang_Truong`, `CPI_YoY`, `Lai_Suat_Dieu_Hanh`). |
| `ky` | String | `Thang` | Kỳ tần suất cập nhật dữ liệu (`Ngay`, `Thang`, `Quy`). |
| `thoi_gian` | String | `2026-Q1` | Mốc thời gian tương ứng của chỉ số (`YYYY-MM-DD` cho ngày, `YYYY-MM` cho tháng, `YYYY-QX` cho quý). |
| `gia_tri` | Float | `7.83` | Số liệu giá trị thực tế của chỉ số vĩ mô. |
| `don_vi_tinh` | String | `%` | Đơn vị của giá trị (`VND/USD` hoặc `%`). |
| `nguon_du_lieu` | String (URL) | `https://vn.investing.com` | Nguồn thu thập chỉ số vĩ mô. |
| `ngay_thu_thap` | DateTime | `2026-06-13 17:44:45` | Thời điểm ghi nhận dữ liệu vào hệ thống (`YYYY-MM-DD HH:MM:SS`). |
