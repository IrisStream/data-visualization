## Tú
### Tree Map
- Lợi ích: Tree Map cho phép biểu diễn tập dữ liệu được sắp xếp theo thứ bậc, mục đích là để chia nhỏ tập dữ liệu thành các phần cấu thành của nó và nhanh chóng xác định các thành phần lớn hơn và nhỏ hơn của tập dữ liệu.
- Biểu đồ Tree Map biểu diễn 1 biến **Total Cases** dựa theo các giá trị của thuộc tính **Country Other**
- Biểu đồ cho một cái nhìn trực quan về tập dữ liệu của biến **Total Cases**, các giá trị của biến **Total Cases** của các nước thể hiện ít hay nhiều dựa theo kích thước của các hình chữ nhật, kích thước hình chữ nhật càng nhỏ thì giá trị biến **Total Cases** càng thấp. Dễ dàng nhận thấy USA là nước có tổng số ca Covid nhiều nhất trên thế giới (hình chữ nhật lớn nhất) và tiếp sau đó là các nước India, Brazil, France...

### Word Cloud
- Lợi ích: dễ dàng nhận ra xu hướng dựa theo kích thước chữ, chữ càng lớn thì xu hướng càng nhiều, xu hướng nhiều nhất thường được để ở trung tâm của Cloud
- Biểu đồ  Word Cloud biểu diễn 1 biến **Total Cases** dựa theo các giá trị của thuộc tính **Country Other**
- Biểu đồ dễ dàng thể hiện được xu hướng hay giá trị **Total Cases** lớn nhất thuộc về USA (kích thước chữ lớn nhất, nằm ở trung tâm). Ngoài ra, ta cũng dễ dàng nhận thấy các nước có giá trị lớn tiếp theo dựa theo kích thước chữ 

### Top Deaths Country
- Lợi ích: thể hiện trực quan các giá trị và cho thấy sự tăng trưởng hay suy giảm của 1 tập dữ liệu từ đó có được cái nhìn tổng quát về thuộc tính
- Biểu đồ Top Deaths Country biểu diễn 1 biến **Total Deaths** ở các nước có giá trị cao nhất.
- Biểu đồ cho thấy được sự khác biệt và ta dễ dàng so sánh giá trị giữa các nước. Từ đó có thể hiểu được sự nguy hiểm của dịch bệnh cũng như tình hình dịch bệnh ở các nước trên thế giới

## Minh Phuong
### Scatter Plot
- Lợi ích: Scatter Plot cho phép biểu diễn tập dữ liệu theo từng điểm trên không gian hai chiều để thể hiện sự tương quan giữa ít nhất hai biến được thể hiện trên trục tung và trục hoành trong biểu đồ. Từ đó rút ra được quan hệ giữa data là như thế nào (nagative - positive, strong - weak, linear - nonlinear, clusters, gap in values, outliers)

### Scatter Plot: Total Cases - Total Deaths - Active Cases
- Biểu đồ này biểu diễn 3 biến Total Cases - Total Deaths - Active Cases:
+ **Total Cases** được biểu diễn bằng tọa độ vị trí điểm dữ liệu trên trục hoành
+ **Total Deaths** được biểu diễn bằng tọa độ vị trí điểm dữ liệu trên trục tung
+ **Active Cases** được biểu diễn bằng kích thước điểm dữ liệu

### Scatter Plot: Total Cases - Total Deaths - Total Recovered
- Biểu đồ này biểu diễn 3 biến Total Cases - Total Deaths - Active Cases:
+ **Total Cases** được biểu diễn bằng tọa độ vị trí điểm dữ liệu trên trục hoành
+ **Total Deaths** được biểu diễn bằng tọa độ vị trí điểm dữ liệu trên trục tung
+ **Total Recovereds** được biểu diễn bằng kích thước điểm dữ liệu

### Scatter Plot: Total Cases - Active Cases - Total Recovered
- Biểu đồ này biểu diễn 3 biến Total Cases - Total Deaths - Active Cases:
+ **Total Cases** được biểu diễn bằng tọa độ vị trí điểm dữ liệu trên trục hoành
+ **Active Cases** được biểu diễn bằng tọa độ vị trí điểm dữ liệu trên trục tung
+ **Total Recovereds** được biểu diễn bằng kích thước điểm dữ liệu

### Scatter Plot: Total Cases - Total Deaths - Total Recovered - Active Cases
- Biểu đồ này biểu diễn 3 biến Total Cases - Total Deaths - Active Cases:
+ **Total Cases** được biểu diễn bằng tọa độ vị trí điểm dữ liệu trên trục hoành
+ **Total Deaths** được biểu diễn bằng tọa độ vị trí điểm dữ liệu trên trục tung
+ **Total Recovereds** được biểu diễn bằng kích thước điểm dữ liệu
+ **Active Cases** được biểu diễn bằng sự biến thiên màu sắc từ cam sang đỏ (giá trị càng lớn càng đỏ)

### Ý nghĩa biểu đồ: 
- Có sự đồng biến giữa biến Total Case và Total Deaths. Đồng thời, cũng có sự đồng biến giữa biến Recovered Cases và Total Cases (khi điểm dữ liệu nằm càng xa thì kích thước biểu diễn điểm dữ liệu càng to).
- Dễ dàng nhận thấy sự chênh lệch cực lớn giữa dữ liệu 3 biến của biểu đồ giữa nước USA, India, Brazil, France, Turkey, UK, Italy, Mexico, Peru...
- Trong các nước có số ca nhiễm lớn, có thể thấy Mexico có tỉ lệ tử vong rất cao và Turkey có tỉ lệ tử vong tương đối thấp
- Đa phần các nước có tổng ca nhiễm < 50 triệu và số Active Cases < 10 triệu (tạo thành một cụm dữ liệu ở góc trái biểu đồ Total Cases - Active Cases - Total Recovered), trừ 4 nước USA, India, Brazil, France là những nơi có dịch nghiêm trọng hơn cả
- Mọi quốc gia có số ca nhiễm lớn cũng có số ca hồi phục lớn, chứng tỏ đang có sự nỗ lực rất lớn trong việc điều trị bệnh dịch. Tuy nhiên, riêng các nước USA, Brazil, India dường như có sự mất kiểm soát nghiêm trọng khi Total Cases và Active Cases tăng quá nhanh.