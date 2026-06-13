# GHI CHÚ RỦI RO PHÁP LÝ VỀ DỮ LIỆU TÀI CHÍNH (LEGAL DATA NOTES)

---

## 1. Bản Quyền Dữ Liệu Tài Chính tại Việt Nam
Theo quy định pháp luật Việt Nam (Luật Sở hữu trí tuệ hiện hành):
*   **Dữ liệu thô (Raw Data):** Các số liệu đơn lẻ như giá khớp lệnh từng giây, khối lượng giao dịch, chỉ số GDP, chỉ số CPI... không thuộc đối tượng được bảo hộ quyền tác giả.
*   **Cơ sở dữ liệu (Database):** Tập hợp các dữ liệu được sắp xếp, hệ thống hóa một cách sáng tạo (như các bảng báo cáo tài chính đã được chuẩn hóa của FiinGroup, hệ thống chỉ số định giá tự tính của Vietstock) **được bảo hộ quyền tác giả** dưới hình thức bảo hộ cơ sở dữ liệu (Điều 22 Luật Sở hữu trí tuệ).
*   **Quyền sở hữu dữ liệu thị trường:** Sở Giao dịch Chứng khoán Việt Nam (VNX), HOSE và HNX là các đơn vị sở hữu hợp pháp duy nhất đối với thông tin giao dịch gốc trên thị trường chứng khoán Việt Nam. Bất kỳ tổ chức nào cung cấp lại dữ liệu này (Data Vendors) đều phải ký hợp đồng thương mại với Sở.

---

## 2. Rủi Ro Pháp Lý Khi Thu Thập Dữ Liệu (Web Scraping)

Hầu hết các nhà phát triển và sinh viên thường sử dụng công cụ cào quét dữ liệu (web scrapers) để lấy thông tin từ các trang như CafeF, Vietstock hoặc các trang báo chí tài chính. Việc này đối mặt với các rủi ro sau:

### A. Vi phạm Điều khoản sử dụng (Terms of Service - ToS)
*   **Hành vi:** Gửi số lượng lớn yêu cầu tự động (HTTP Requests) để lấy dữ liệu từ máy chủ của CafeF, Vietstock...
*   **Hệ quả pháp lý:** Hầu hết các trang web này đều có điều khoản cấm cào quét tự động bằng bot. Họ có quyền chặn địa chỉ IP (IP Block), vô hiệu hóa tài khoản và trong trường hợp gây nghẽn mạng nghiêm trọng (DDoS ngoài ý muốn), có thể bị truy cứu trách nhiệm theo Luật An ninh mạng 2018 (Hành vi cản trở hoạt động của mạng máy tính).

### B. Sử dụng API không chính thức (Undocumented/Private APIs)
*   **Hành vi:** Trích xuất và gọi trực tiếp vào API nội bộ (Backend Web APIs) của các công ty chứng khoán (như KBSec) hoặc các trang tin tài chính để lấy dữ liệu mà không qua cổng tích hợp đối tác chính thức.
*   **Hậu quả pháp lý:** 
    *   Các công ty chứng khoán có thể thiết lập tường lửa (WAF/Cloudflare) để chặn dải IP hoặc thay đổi cấu trúc dữ liệu JSON đột ngột, làm sập hệ thống thu thập dữ liệu.
    *   Về mặt pháp lý, việc khai thác tài nguyên máy chủ quy mô lớn cho mục đích thương mại mà không mua quyền sử dụng có thể bị xử lý theo Luật Sở hữu trí tuệ và Luật An ninh mạng.

---

## 3. Khác Biệt Giữa Đồ Án Học Thuật & Sản Phẩm Thương Mại

### 3.1. Sử dụng dữ liệu cho Đồ án (Academic / Educational Use)
*   **Đánh giá rủi ro:** **Thấp (Gần như không có rủi ro pháp lý)**.
*   **Cơ sở pháp lý:** Khoản 1 Điều 25 Luật Sở hữu trí tuệ quy định về các trường hợp ngoại lệ không phải xin phép, không phải trả tiền bản quyền, bao gồm: *"Tự sao chép một bản nhằm mục đích nghiên cứu khoa học, giảng dạy của cá nhân"* và *"Trích dẫn hợp lý tác phẩm mà không làm sai ý tác giả để giảng dạy, nghiên cứu"*.
*   **Yêu cầu tuân thủ:**
    *   Phải trích dẫn nguồn rõ ràng (Ví dụ: *"Số liệu giá cổ phiếu lấy từ CafeF tại ngày..."*).
    *   Không được chia sẻ lại toàn bộ bộ cơ sở dữ liệu đã cào quét lên các kho lưu trữ công cộng (Public Repo) nếu bộ dữ liệu đó mang tính bản quyền của bên khác.
    *   Chỉ sử dụng trong phạm vi nội bộ trường học/viện nghiên cứu.

### 3.2. Sử dụng dữ liệu cho Sản phẩm Thương mại (Commercial Use)
*   **Đánh giá rủi ro:** **Rất cao (Nếu không mua bản quyền)**.
*   **Các hành vi vi phạm phổ biến:**
    1.  Cào dữ liệu từ CafeF/Vietstock về hiển thị trên ứng dụng thương mại của mình (app tư vấn đầu tư, web phân tích tài chính).
    2.  Đóng gói dữ liệu cào được thành các API trả phí để bán lại cho người khác (Redistribution).
    3.  Tích hợp thư viện `vnstock` vào backend của sản phẩm thương mại để cung cấp biểu đồ kỹ thuật thời gian thực cho người dùng cuối.
*   **Hậu quả pháp lý đối với sản phẩm thương mại:**
    *   **Bị kiện bản quyền:** Các đơn vị sở hữu dữ liệu (FiinGroup, Vietstock) có đội ngũ pháp lý để rà soát và gửi yêu cầu gỡ bỏ (DMCA) hoặc khởi kiện đòi bồi thường thiệt hại nếu phát hiện hành vi sử dụng dữ liệu trái phép để kinh doanh.
    *   **Đình trệ hệ thống:** Việc bị chặn IP đột ngột từ phía nguồn dữ liệu sẽ khiến sản phẩm thương mại bị mất kết nối dữ liệu, ảnh hưởng nghiêm trọng đến uy tín và trải nghiệm khách hàng.