# QUY TẮC CHẤT LƯỢNG DỮ LIỆU (DATA QUALITY RULES)
---

## 1. Quy tắc dữ liệu Giá cổ phiếu (`stock_prices.csv`)

| ID | Tên Quy Tắc | Mô Tả Kỹ Thuật / Công Thức |
| :--- | :--- | :--- |
| **SP_01** | Giá cổ phiếu không âm | Tất cả các cột giá (`gia_mo_cua_vnd`, `gia_cao_nhat_vnd`, `gia_thap_nhat_vnd`, `gia_dong_cua_vnd`, `gia_dong_cua_dieu_chinh_vnd`) bắt buộc phải là số nguyên dương lớn hơn `0`. |
| **SP_02** | Khối lượng không âm | Cột `khoi_luong_giao_dich_co_phieu` phải là số nguyên không âm (≥ `0`). |
| **SP_03** | Ràng buộc biên độ giá | Giá cao nhất trong phiên phải lớn hơn hoặc bằng giá thấp nhất trong phiên:<br>$$gia\_cao\_nhat\_vnd \ge gia\_thap\_nhat\_vnd$$ |
| **SP_04** | Tính duy nhất theo ngày | Ràng buộc duy nhất (Unique key): Một cặp giá trị (`ma_co_phieu`, `ngay`) chỉ được phép xuất hiện tối đa một dòng dữ liệu duy nhất trong bảng giá. |
| **SP_05** | Tính nhất quán của giá điều chỉnh | Đối với các mã không có sự kiện chia tách/cổ tức trong ngày, giá đóng cửa điều chỉnh phải bằng giá đóng cửa gốc:<br>$$gia\_dong\_cua\_dieu\_chinh\_vnd = gia\_dong\_cua\_vnd$$ |

---

## 2. Quy tắc dữ liệu Báo cáo tài chính doanh nghiệp (Thư mục `BCTC/`)

Do dữ liệu BCTC được lấy trực tiếp dưới dạng Excel gốc từ **trading.vietcap.com.vn**, các quy tắc kiểm tra chất lượng được áp dụng trên cấu trúc bảng tính:

| ID | Tên Quy Tắc | Mô Tả Kỹ Thuật / Công Thức |
| :--- | :--- | :--- |
| **FR_01** | Phân định rõ kỳ báo cáo | Báo cáo tài chính bắt buộc phải phân biệt rõ ràng giữa kỳ báo cáo Quý (`Quy` trong file `_quy.xlsx`) và Năm (`Nam` trong file `_nam.xlsx`). Tuyệt đối không được gộp chung hoặc làm lẫn lộn các cột thời gian giữa hai tần suất này. |
| **FR_02** | Xử lý dữ liệu khuyết thiếu | Khi một chỉ tiêu tài chính không có dữ liệu (hoặc doanh nghiệp không công bố), bắt buộc phải để giá trị trống (`null` hoặc trống trong Excel). **Tuyệt đối không được tự ý điền số `0`** vì điều này sẽ gây sai lệch nghiêm trọng các chỉ số phân tích như biên lợi nhuận gộp, biên lợi nhuận ròng. |
| **FR_03** | Nhất quán nhãn dòng kế toán | Bộ parser/mã nguồn xử lý phải phân biệt rõ nhãn dòng giữa **Ngân hàng** (doanh thu là Thu nhập lãi, lợi nhuận gộp là Thu nhập lãi thuần) và **Doanh nghiệp phi tài chính** (Doanh thu thuần, Lợi nhuận gộp) để tránh lấy sai chỉ tiêu. |

---

## 3. Quy tắc logic nghiệp vụ & Chỉ số định giá tài chính

Các quy tắc áp dụng khi lập công thức tính toán hoặc hiển thị các chỉ số định giá trên hệ thống:

| ID | Tên Quy Tắc | Mô Tả Kỹ Thuật / Công Thức |
| :--- | :--- | :--- |
| **VAL_01** | Logic P/E khi EPS âm | Nếu EPS (Lợi nhuận trên mỗi cổ phiếu) bị âm (doanh nghiệp đang thua lỗ), chỉ số định giá P/E không nên hiển thị hoặc phải được đánh dấu là không xác định (N/A). **Không được phép hiển thị P/E âm như một chỉ số chứng minh cổ phiếu đang "rẻ"**. |
| **VAL_02** | Dấu dòng tiền kinh doanh | Dòng tiền thuần từ hoạt động kinh doanh (`dong_tien_thuan_tu_hdkd_vnd`) được phép âm (phản ánh tình trạng doanh nghiệp bị đọng vốn, tăng hàng tồn kho hoặc khoản phải thu). Tuyệt đối không được áp dụng quy tắc ép dương hoặc mặc định gán về `0` cho chỉ tiêu này. |
| **VAL_03** | Mối quan hệ Doanh thu - Lợi nhuận | Lợi nhuận gộp không được lớn hơn doanh thu thuần (đối với doanh nghiệp phi tài chính) trong điều kiện bình thường:<br>$$loi\_nhuan\_gop\_vnd \le doanh\_thu\_thuan\_vnd$$ |

---

## 4. Quy tắc dữ liệu Chỉ số Vĩ mô (`macro_indicators.csv`)

| ID | Tên Quy Tắc | Mô Tả Kỹ Thuật / Công Thức |
| :--- | :--- | :--- |
| **MC_01** | Tỷ giá USD/VND hợp lệ | Tỷ giá trung tâm USD/VND phải là số dương và nằm trong khung biến động tỷ giá chính thức được kiểm soát bởi Ngân hàng Nhà nước. |
| **MC_02** | Lãi suất và lạm phát thực tế | Giá trị lãi suất điều hành NHNN (`Lai_Suat_Dieu_Hanh`) và lạm phát (`CPI_YoY`) phải nằm trong giới hạn thực tế hợp lý (không âm đối với lãi suất; CPI có thể âm trong trường hợp giảm phát cực đoan. |
| **MC_03** | Tính duy nhất theo mốc thời gian | Một chỉ số vĩ mô chỉ được phép có duy nhất một giá trị tại một thời điểm tương ứng:<br>- Tỷ giá: duy nhất 1 dòng mỗi ngày (`YYYY-MM-DD`).<br>- CPI & Lãi suất: duy nhất 1 dòng mỗi tháng (`YYYY-MM`).<br>- GDP: duy nhất 1 dòng mỗi quý (`YYYY-QX`). |
| **MC_04** | Đồng bộ đơn vị tính | Đơn vị tính (`don_vi_tinh`) phải được chuẩn hóa đồng bộ:<br>- Tỷ giá: `"VND/USD"`<br>- GDP, CPI, Lãi suất: `"%"` |
