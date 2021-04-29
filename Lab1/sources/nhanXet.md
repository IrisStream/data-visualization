# Giải thích biểu đồ & Nhận xét dữ liệu

- Tại đây chứa phần **giải thích biểu đồ** (tại sao lại sử dụng loại biểu đồ này để visualize) và phần **nhận xét dữ liệu** (giống kiểu sách tóm tắt thống kê trang 76)

## Giải thích biểu đồ

- Lý do sử dụng **Line Chart** trong biểu diễn mối quan hệ giữa 3 biến dữ liệu và 4 biến dữ liệu
    ```python
    # visualize the first 10 countries
    # relationships: list of tuple. ex: [(Total Case, Total Deaths, Total Recovered), ...]
    def visualizeRelationships(relationships):
        fig, axs = plt.subplots(2,5, figsize=(30,15))
        fig.tight_layout(pad=7.5)
        
        countries = df['CountryName'][:10]
        for i in range(2):
            for j in range(5):
                X = []
                for k in range(len(relationships[0])-1):
                    X.append(df[relationships[5*i+j][k]].values)
                    axs[i,j].plot(countries, X[k][:10], '-o', label=relationships[5*i+j][k])
                X = np.array(X)
                Y = df[relationships[5*i+j][-1]].values
                axs[i,j].plot(countries, Y[:10], '--o', label=relationships[5*i+j][-1]+' (phụ thuộc)')

                w,_ = linear_regression(X,Y)
                axs[i,j].set_xlabel('Country')
                axs[i,j].set_ylabel('Case')
                axs[i,j].legend()
                axs[i,j].set_title(f'{relationships[5*i+j]}\nW = {np.round(w,1)}')
                axs[i,j].set_xticklabels(countries, rotation=90)

        plt.show()
    ```

    - 

- Lý do sử dụng **Biểu đồ Scatter** (Tú)
    - write something here

- Lý do sử dụng **Stacked Bar Chart** (MP)
    - write something here

## Nhận xét dữ liệu 

- 