# DANH SÁCH NGUỒN DỮ LIỆU THẬT (DATA SOURCES)

Tài liệu này tổng hợp và đánh giá chi tiết các nguồn dữ liệu tài chính, chứng khoán và vĩ mô tại Việt Nam phục vụ cho đồ án (nghiên cứu khoa học) và các sản phẩm thương mại.

---

## I. BẢNG TỔNG HỢP CÁC NGUỒN DỮ LIỆU

| STT | Tên Nguồn | Link Nguồn | Loại Dữ Liệu | Tần Suất Cập Nhật | Loại Phí | Đồ Án? |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| 1 | **KB Securities (KBSec)** | [kbsec.com.vn](https://kbsec.com.vn) | Giá đóng cửa điều chỉnh, mở cửa, cao, thấp, khối lượng giao dịch | Hàng ngày | Miễn phí | **Có** |
| 2 | **Trading Vietcap** | [trading.vietcap.com.vn](https://trading.vietcap.com.vn) | Báo cáo tài chính gốc dưới dạng Excel của 14 doanh nghiệp | Hàng quý/Năm | Miễn phí | **Có** |
| 3 | **Investing.com** | [vn.investing.com](https://vn.investing.com) | Chỉ số GDP tăng trưởng thực tế, lạm phát CPI YoY Việt Nam | Hàng tháng/Quý | Miễn phí | **Có** |
| 4 | **Vietstock** | [vietstock.vn](https://vietstock.vn) | Tỷ giá trung tâm chính thức của Ngân hàng Nhà nước | Hàng ngày | Miễn phí | **Có** |
| 5 | **Ngân hàng Nhà nước (SBV)** | [sbv.gov.vn](https://www.sbv.gov.vn) | Lịch sử quyết định lãi suất tái cấp vốn điều hành | Định kỳ | Miễn phí | **Có** |

---

## II. CHI TIẾT TỪNG NGUỒN DỮ LIỆU
### 1. Vietstock
*   **Tên nguồn:** Cổng thông tin tài chính - chứng khoán Vietstock.
*   **Link nguồn:** [https://vietstock.vn](https://vietstock.vn) (Dữ liệu tài chính: [https://finance.vietstock.vn](https://finance.vietstock.vn))
*   **Loại dữ liệu lấy:**
    *   Danh sách cổ phiếu niêm yết theo sàn (HOSE, HNX, UPCoM).
    *   Báo cáo tài chính chi tiết (Cân đối kế toán, Kết quả HĐKD, Lưu chuyển tiền tệ) dạng số hóa.
    *   Chỉ số tài chính tính sẵn (P/E, P/B, ROE, ROA, EPS).
    *   Chỉ số vĩ mô Việt Nam.
*   **Tần suất cập nhật:** Thời gian thực (giá); Hàng ngày (kết quả giao dịch); Cập nhật liên tục (tin tức/sự kiện); Định kỳ hàng quý (BCTC).
*   **Chi phí:** Miễn phí xem web cơ bản. Trả phí nếu muốn tải dữ liệu lớn bằng Excel hoặc tích hợp API của Vietstock.
*   **Sử dụng cho đồ án:** **Được phép** (sử dụng thông tin xem trực quan hoặc xuất số liệu thủ công quy mô nhỏ).

---

### 2. Thư viện Vnstock (Python Open Source)
*   **Tên nguồn:** Vnstock - Python Library for Vietnam Stock Market (Tác giả: Thịnh Vũ).
*   **Link nguồn:** [https://github.com/thinh-vu/vnstock](https://github.com/thinh-vu/vnstock)
*   **Loại dữ liệu lấy:**
    *   Dữ liệu giá lịch sử và trong ngày.
    *   Báo cáo tài chính (Cân đối kế toán, Kết quả HĐKD, Lưu chuyển tiền tệ) dạng DataFrame.
    *   Thông tin hồ sơ công ty, danh sách cổ phiếu, nhóm ngành.
    *   Chỉ số kỹ thuật và bộ lọc cổ phiếu.
*   **Cơ chế hoạt động:** Thư viện này hoạt động bằng cách gọi gián tiếp các API công khai/không công khai của các công ty chứng khoán lớn tại Việt Nam (như TCBS, VNDirect, SSI).
*   **Tần suất cập nhật:** Thời gian thực/Hàng ngày.
*   **Chi phí:** Miễn phí (Mã nguồn mở MIT).
*   **Sử dụng cho đồ án:** **Được phép và khuyến nghị**. Rất tiện lợi cho các bài toán phân tích định lượng bằng Python/Jupyter Notebook.

---

### 3. Ngân hàng Nhà nước Việt Nam (SBV)
*   **Tên nguồn:** Ngân hàng Nhà nước Việt Nam (State Bank of Vietnam).
*   **Link nguồn:** [https://www.sbv.gov.vn](https://www.sbv.gov.vn)
*   **Loại dữ liệu lấy:**
    *   Tỷ giá trung tâm của Đồng Việt Nam với Đô la Mỹ (USD/VND) và tỷ giá tính chéo của một số ngoại tệ khác.
    *   Lãi suất điều hành: Lãi suất tái cấp vốn, lãi suất tái chiết khấu, trần lãi suất huy động.
    *   Lãi suất bình quân liên ngân hàng.
*   **Tần suất cập nhật:** Hàng ngày (cho tỷ giá trung tâm và lãi suất liên ngân hàng).
*   **Chi phí:** Hoàn toàn miễn phí.
*   **Sử dụng cho đồ án:** **Được phép**.
---

### 4. KB Securities Vietnam (KBSec)
*   **Tên nguồn:** Công ty Cổ phần Chứng khoán KB Việt Nam.
*   **Link nguồn:** [https://kbsec.com.vn](https://kbsec.com.vn)
*   **Loại dữ liệu lấy:**
    *   Dữ liệu giá đóng cửa điều chỉnh, mở cửa, cao, thấp và khối lượng giao dịch hàng ngày của cổ phiếu.
*   **Tần suất cập nhật:** Hàng ngày (sau 15:00).
*   **Chi phí:** Miễn phí (qua API Web đầu cuối).
*   **Sử dụng cho đồ án:** **Được phép** (tận dụng để lấy dữ liệu thực và chính xác nhanh chóng).


---

### 5. Trading Vietcap
*   **Tên nguồn:** Công ty cổ phần chứng khoán Vietcap.
*   **Link nguồn:** Dữ liệu được tải trực tiếp từ hệ thống giao dịch của VietCap: [trading.vietcap.com.vn](https://trading.vietcap.com.vn)
*   **Loại dữ liệu lấy:**
    *   Các tệp báo cáo tài chính định dạng Excel (`.xlsx`) gốc của 14 doanh nghiệp theo năm (`_nam.xlsx`) và theo quý (`_quy.xlsx`), bao gồm các sheet Bảng cân đối kế toán, Kết quả hoạt động kinh doanh, Lưu chuyển tiền tệ, Thuyết minh.
*   **Tần suất cập nhật:** Định kỳ hàng quý sau khi doanh nghiệp công bố thông tin và người dùng tải về.
*   **Chi phí:** Miễn phí (Được cung cấp qua hệ thống giao dịch khách hàng VietCap).
*   **Sử dụng cho đồ án:** **Được phép**.

---

### 6. Investing.com
*   **Tên nguồn:** Cổng thông tin tài chính quốc tế Investing.com (phiên bản Việt Nam).
*   **Link nguồn:** [https://vn.investing.com](https://vn.investing.com)
*   **Loại dữ liệu lấy:**
    *   Tốc độ tăng trưởng GDP hàng quý của Việt Nam từ 2021-Q1 đến 2026-Q1.
    *   Chỉ số lạm phát CPI theo năm (YoY %) hàng tháng từ 2021-01 đến 05/2026.
*   **Tần suất cập nhật:** Ngay khi Tổng cục Thống kê công bố số liệu.
*   **Chi phí:** Miễn phí.
*   **Sử dụng cho đồ án:** **Được phép** (Khuyến nghị trích xuất thông qua dữ liệu Next.js preloaded để tránh lỗi tải trang).
