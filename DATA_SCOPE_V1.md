# PHẠM VI DỮ LIỆU ĐỀ XUẤT (DATA SCOPE PROPOSAL - V1)

---

## 1. Danh Sách Mã Cổ Phiếu Đề Xuất (14 Mã)
Danh sách dưới đây bao gồm **14 mã cổ phiếu** được chọn lọc từ 4 ngành kinh tế đại diện quan trọng, đảm bảo phân bổ hợp lý trong khoảng từ **10 đến 15 mã** theo yêu cầu đề xuất:

| Ngành | Mã CK | Tên Doanh Nghiệp |  Sàn |
| :--- | :---: | :--- | :--- |
| **Ngân hàng** | **VCB** | Ngân hàng TMCP Ngoại thương Việt Nam | HOSE |
| | **TCB** | Ngân hàng TMCP Kỹ thương Việt Nam | HOSE |
| | **MBB** | Ngân hàng TMCP Quân đội | HOSE |
| | **CTG** | Ngân hàng TMCP Công Thương Việt Nam |  HOSE |
| **Công nghệ** | **FPT** | Công ty Cổ phần FPT | HOSE |
| | **CMG** | Công ty Cổ phần Tập đoàn Công nghệ CMC | HOSE |
| | **VGI** | Tổng Công ty Cổ phần Đầu tư Quốc tế Viettel | UPCoM |
| **Thép** | **HPG** | Công ty Cổ phần Tập đoàn Hòa Phát | HOSE |
| | **HSG** | Công ty Cổ phần Tập đoàn Hoa Sen | HOSE |
| | **NKG** | Công ty Cổ phần Thép Nam Kim | HOSE |
| **Bất động sản** | **VHM** | Công ty Cổ phần Vinhomes | HOSE |
| | **VIC** | Tập đoàn Vingroup | THOSE |
| | **NLG** | Công ty Cổ phần Đầu tư Nam Long | HOSE |
| | **DXG** | Công ty Cổ phần Tập đoàn Đất Xanh | HOSE |

---

## 2. Phạm Vi Dữ Liệu Giá và Tài Chính

### 2.1. Dữ Liệu Giá Cổ Phiếu
*   **Thời gian thu thập:** Từ năm **2021** đến thời điểm hiện tại (**2026**).
*   **Tần suất dữ liệu:** Hàng ngày .
*   **Các trường thông tin thu thập:**
    *   Mã cổ phiếu 
    *   Ngày giao dịch 
    *   Giá mở cửa 
    *   Giá cao nhất 
    *   Giá thấp nhất
    *   Giá đóng cửa
    *   Giá đóng cửa điều chỉnh
    *   Khối lượng giao dịch

### 2.2. Dữ Liệu Báo Cáo Tài Chính (BCTC)
*   **Danh sách tệp tin**: Mỗi doanh nghiệp có 2 tệp Excel là báo cáo năm từ 2021 đến 2025 và báo cáo quý từ Q1/2021 đến Q1/2026.
*   **Các báo cáo thành phần có sẵn trong tệp tin**:
    1.  **Bảng Cân đối kế toán **
    2.  **Báo cáo Kết quả hoạt động kinh doanh **
    3.  **Báo cáo Lưu chuyển tiền tệ **
    4.  **Thuyết minh báo cáo tài chính **

---

## 3. Dữ Liệu Vĩ Mô Cơ Bản (Macroeconomic Data)

| Chỉ số vĩ mô | Tần suất | Đơn vị tính | Nguồn dữ liệu chính | Phạm vi thời gian |
| :--- | :---: | :---: | :--- | :--- |
| **Tỷ giá trung tâm** | Hàng ngày | VND/USD | finance.vietstock.vn | 2021-01-01 đến nay (2026) |
| **Tăng trưởng GDP** | Quý | % | vn.investing.com | 2021-Q1 đến 2026-Q1 |
| **Chỉ số CPI (Lạm phát)** | Tháng | % | vn.investing.com | 2021-01 đến 2026-05 |
| **Lãi suất điều hành** | Tháng | % | www.sbv.gov.vn (Quyết định của NHNN) | 2021-01 đến 2026-06 |

*   **Thời gian thu thập:** từ năm 2021 đến thời điểm hiện tại (2026).

---

## 4. Công Cụ & Nguồn Thu Thập Dữ Liệu Thực Tế

Toàn bộ dữ liệu được trích xuất hoàn toàn tự động thông qua các kết nối API trực tiếp từ hệ thống:
1.  **Dữ liệu giao dịch cổ phiếu:**
    *   **KB Securities (KBSec) API:** Thu thập dữ liệu lịch sử giá OHLC và khối lượng giao dịch hàng ngày của 14 mã cổ phiếu.
2.  **Báo cáo tài chính doanh nghiệp:**
    *   **Thư mục BCTC:** Dữ liệu báo cáo tài chính gốc của 14 doanh nghiệp được lưu dưới dạng file Excel trong thư mục `BCTC/`, được tải trực tiếp từ hệ thống **trading.vietcap.com.vn** của VietCap.
3.  **Dữ liệu vĩ mô:**
    *   **vn.investing.com:** Cập nhật số liệu Tăng trưởng GDP và Chỉ số lạm phát CPI thực tế của Việt Nam.
    *   **finance.vietstock.vn:** Cập nhật Tỷ giá trung tâm USD/VND hàng ngày.
    *   **State Bank of Vietnam (SBV):** Lịch sử các mốc lãi suất tái cấp vốn điều hành thực tế của Ngân hàng Nhà nước Việt Nam.
