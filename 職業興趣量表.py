import matplotlib.pyplot as plt
import numpy as np

def collect_scores():
    """收集使用者輸入的興趣分數"""
    print("請輸入以下領域的興趣分數 (0.0 到 6.0):")
    categories = {
        "R": "實用型",
        "I": "研究型",
        "A": "藝術型",
        "S": "社會型",
        "E": "企業型",
        "C": "事務型"
    }
    scores = {}
    for category, description in categories.items():
        while True:
            try:
                score = float(input(f"{description} ({category})："))
                if 0.0 <= score <= 6.0:
                    scores[category] = score
                    break
                else:
                    print("請輸入範圍內的數值 (0.0 到 6.0)！")
            except ValueError:
                print("請輸入有效的數字！")
    return scores

def plot_radar_chart(scores):
    """繪製六角形雷達圖"""
    categories = list(scores.keys())
    values = list(scores.values())
    
    # 將數據封閉以形成完整的多邊形
    values += values[:1]  # 將第一個值追加到最後形成封閉
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]  # 將第一個角度追加到最後形成封閉

    # 繪製雷達圖
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='blue', alpha=0.25)
    ax.plot(angles, values, color='blue', linewidth=2)
    ax.set_yticks([1, 2, 3, 4, 5, 6])
    ax.set_ylim(0, 6)
    ax.set_xticks(angles[:-1])  # 使用原始類別數的角度
    ax.set_xticklabels(categories)  # 對應原始類別名稱

    # 在每個頂點顯示輸入的分數
    for i, value in enumerate(values[:-1]):  # 最後一個值是封閉的點，不重複標記
        angle_rad = angles[i]
        x = angle_rad
        y = value * 1.1  # 標記位置稍微偏外
        ax.annotate(f"{value:.1f}", xy=(angle_rad, value), xytext=(x, y),
                    textcoords='data', ha='center', va='center', color='black')

    # 添加標題
    ax.set_title("Career Interest Inventory Radar Chart", va='bottom')
    plt.show()

def main():
    print("歡迎使用職業興趣量表！")
    scores = collect_scores()
    print("\n您輸入的興趣分數：")
    for category, score in scores.items():
        print(f"{category}：{score}")
    
    plot_radar_chart(scores)

if __name__ == "__main__":
    main()
