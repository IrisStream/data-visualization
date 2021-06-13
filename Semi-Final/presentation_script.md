# Nội dung thuyết trình đồ án "Telecom operator executive dashboard"

_Các thuật ngữ được giải thích đầy đủ tại đây_

## Scenario (Bối cảnh)

Công ty CTT cần theo dõi và đánh giá các mục tiêu kinh doanh của họ. Cụ thể hơn họ cần theo dõi và tối ưu các chỉ số sau:

- Giảm SAC
- Tăng ARPU
- Giảm Churn

Vì vậy họ cần 1 dashboard có thể quan sát một cách tổng quát các chỉ số trên. Dashboard này không cần phải có các chứa năng tưởng tác nhưng vần phải chứa đầy đủ các thông tin cần thiết, đơn giản không gây rối mắt người xem để có thể trình bày trong các buổi họp công ty.

### Yêu cầu cần được trình bày trong Dashboard

- Biểu diễn đầy đủ 3 thông tin quan trọng nhất: SAC, ARPU, Churn.

- Các thông tin được biểu diễn theo thời gian (YTD).
- Cần có tóm tắt về Revenu (lợi nhuận), OPEX, EBITDA của năm nay và năm ngoái để so sánh.
- Cần các thông tin trong 4 quý gần nhất của Subscribers (Total Subscriber, new Subscriber trả trước/trả sau).
- Tổ chức Dashboard từ tổng quát đến chi tiết các thông tin.
- Biểu diên xu hướng của các chỉ số (sử dụng line chart).
- Có thể so sánh được các chỉ số ở các giai đoạn thời gian khác nhau (Giữa các quý, giữa năm nay và năm ngoái).
- Xem xét các thông tin của bộ phận chăm sóc khách hàng (do chúng sẽ ảnh hưởng đến chỉ số churn).

## How People Use the dashboard (Cách sử dụng Dashboard)

Dashboard được thiết kế gồm 4 vùng: 3 vùng biểu diễn 3 mục tiêu (SAC, ARPU, Churn) và 1 vùng tóm tắt các chỉ số điều hành. 3 mục tiêu đươc thiết kế theo hàng từ trái sang phải. Và phần tóm tắt chỉ số được biểu diễn theo chiều thẳng đứng nằm phía bên phải của Dashboard.

### SAC

Số liệu cho thấy SAC đang tăng $4. Và công ti cần tốn $16 cho mỗi tháng hợp đồng. Số liệu được tính theo YTD. Line chart bên dưới cho ta thấy SAC của 4 quý gần nhất.

Biểu đồ thứ 2 cho ta biết SAC của các loại hợp đồng khác nhau (1, 2, 3 năm). Có thể thấy SAC tăng trong 4 quý gần đây và tăng ở cả 3 loại hợp đồng. Ngoài ra, hợp đồng dài hạn hơn thì có SAC thấp hơn. (Giải thích).

Biểu đồ thứ 3 cho ta biết chi phí cho các sản phẩm ODM của công ty trong 4 quý gần nhất. Nhãn của mỗi cột là số lượng sản phẩm ODM và trục x là số tiền phải chi.

Biểu đồ cuối cho ta thấy ... thấy cl éo giải thích gì hết sao mà thấy

### ARPU

Số liệu ARPU tổng thể, tăng $6, và doanh thu trung bình của dịch vụ trả sau theo tháng là $68.

Biểu đồ thứ 2 cho ta thấy ARPU của 2 loại khách hàng trả trước và trả sau. Có thể thấy doanh thu từ các khách hàng trả sau cao hơn gấp 3 lần doanh thu của các khách hàng trả trước. _(Giải thích)_

Biểu đồ thứ 3 cho ta thấ tổng số lượng subscriber của 3 loại dịch vụ: Voice, Data và Addons trong 4 quý gần nhất. Trong đó voice có mức lợi nhuận cao nhất và data là thấp nhất. _(Giải thích)_

Biểu đồ cuối cùng cho ta thấy số lượng yêu cầu nâng cấp dịch vụ trong 4 quý gần đây, cột biểu thị cho số lượng offer được đưa ra. Đường gạch ngang thể hiện số lượng offer được khách hàng đồng ý nâng cấp. Có thể thấy số lượng offer và số khách hàng đồng ý đang tăng.

### Churn rate

Biểu đồ thể hiện tỉ lệ churn của các khách hàng trả sau hàng tháng từ đầu năm cho đến nay là 1.43% giảm 0.18% so với đầu năm. Biểu đồ đường phía dưới cho ta thấy tỉ lệ churn tăng nhẹ trong 2 quý đầu nhưng và bắt đầu giảm mạnh trong 2 quý sau.

Biểu đồ thứ 2 cho ta thấy tỉ lệ churn của CTT và 3 công ty đối thủ là Targus, Roberts, BTEL. Ở 2 quý đầu, CTT đứng hạng 2 nhưng sau đó đã vượt lên đứng đầu trong 4 công ty.

Biểu đồ thứ 3 cho tat thấy tình hình của trung tâm hỗ trợ khách hàng (call center). Gồm có 4 biểu đồ biểu diễn về hold time, 1st call Resolution, Call Length, và số lượng open ticket. 3 chỉ số hold time, 1st call resolution và call length đều có dấu hiệu giảm từ đầu quý 3 đến nay, trong khi đó thì số lượng open ticket lại tăng trong quý gần nhất.

Biểu đồ cuối cho ta thấy mức độ hài lòng của khách hàng vào năm 2015 (cột) và năm 2014 (đường). (Năm kinh tế).

### Executive Summary

Biểu đồ cho ta thấy tóm tắt các số liệu về lợi nhuận (Revenue), OPEX và EBITDA của năm nay và năm ngoái. _(Nói vài câu so sánh)_. Bốn đồ thị phía dưới cho ta thấy tổng số lượng và số lượng khách hàng mới của 2 loại khách hàng trả trước và trả sau trong 4 quý gần đây. _(Nhận xét vài dòng)_

## Why this works (Vì sao các biểu diễn này hiệu quả)

### Các chỉ số đươc biểu diễn đầy đủ nhưng không lộn xộn

Dashboard này nắm bắt tất cả dữ liệu quan trọng cần thiết để trả lời các câu hỏi kinh doanh ở cấp điều hành mà không cần phải đi sâu vào các báo cáo và dữ liệu khác. Nó chứa đầy dữ liệu nhưng không cảm thấy lộn xộn. Điều này được thực hiện bằng cách sử dụng hình ảnh nhỏ, được thiết kế tốt sử dụng các kỹ thuật khác nhau để làm cho nó trở nên nhỏ gọn.

_Ví dụ_: biểu đồ đường hiển thị dữ liệu chuỗi thời gian có nhãn theo sau mà không cần phải thêm chú giải màu sắc hoặc hình dạng. Màu sắc được sử dụng biểu thị sự tăng và giảm của các mục tiêu.

### Bố cục hỗ thiết kế để để có thểm xem nhanh

Bảng điều khiển cung cấp thông tin chi tiết về bốn lĩnh vực, mỗi lĩnh vực có các chi tiết cần thiết, theo cách có tổ chức. Các chỉ số chính được sắp xếp thành ba hàng và một cột, giúp chúng dễ dàng nhóm lại với nhau và nhanh chóng quét.

### Các loại Biểu đồ phụ hợp cho các so sánh khác nhau

Biểu đồ đường là một lựa chọn tuyệt vời để hiển thị xu hướng theo thời gian. Chúng được sử dụng khắp dashboard này để hiển thị các số liệu khác nhau trong 4 quý gần nhất. Các đường gấp khúc được sử dụng để hiển thị các xu hướng trong các chỉ số chính. Biểu đồ cột với các đường mục tiêu được sử dụng để hiển thị giai đoạn này so với giai đoạn trước.

## Author Commentary

### Jeff

- Việc chọn màu xanh lá và đỏ gây bất lợi cho người bị mù màu, Có thể đổi thành xanh dương và cam.
- Nên đổi thời gian thành trục x ở đồ thị thứ 3 hàng 1 để có thể đồng bộ với các đồ thị khác. Ngoài ra còn có thể đổi các biểu đồ cột thành biểu đồ đường, điều này sẽ giúp người đọc nhìn thấy xu hướng theo thời gian tốt hơn. Biểu đồ 3 của goal 2 có thể cho đươc kết qua so sánh tốt hơn bằng các sử dụng biểu đồ đường thay vì cột.

### Andy

- Việc loại bỏ màu sắc trong các biểu đồ đường có thể gây ra sự bối rối khi các đường thẳng giao nhau. Việc này có thể được giải quyết bằng 2 cách sau đây:
  1.  Sử dụng màu sắc cho các đường khác nhau. Song, việc sử dụng quá nhiều màu sắc trong 1 dashboard có thể làm cho người xem rối mắt đồng thời mất đi tính thẩm mĩ của dashboard.
  2.  Sử dộng opacity khác nhau cho các đường khác nhau. Cách này có nhược điểm là không thể sử dụng cho các biểu đồ đường có quan nhiều đường khác nhau sẽ dẫn đến khó phân biệt chúng. Và vì thế nên khá phù hợp cho dashboard trên vì số lượng đường trong các biểu đồ ít nên ta có được 1 dãi sắc độ rộng hơn để phân biệt các đường với nhau. Và cách này cũng giúp tránh được các nhược điểm của cách 1.
