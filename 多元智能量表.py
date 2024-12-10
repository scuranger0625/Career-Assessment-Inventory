import matplotlib.pyplot as plt
import numpy as np

def collect_scores():
    """Collect user input for multiple intelligence T-scores."""
    print("Enter the standard scores (T-scores, 0 to 100) for each intelligence type:")
    categories = {
        "Linguistic": "Linguistic Intelligence",
        "Logical": "Logical-Mathematical Intelligence",
        "Spatial": "Spatial Intelligence",
        "Musical": "Musical Intelligence",
        "Kinesthetic": "Bodily-Kinesthetic Intelligence",
        "Intrapersonal": "Intrapersonal Intelligence",
        "Interpersonal": "Interpersonal Intelligence",
        "Naturalistic": "Naturalistic Intelligence",
        "Existential": "Existential Intelligence"
    }
    scores = {}
    for category, description in categories.items():
        while True:
            try:
                score = float(input(f"{description} ({category}): "))
                if 0.0 <= score <= 100.0:
                    scores[category] = score
                    break
                else:
                    print("Please enter a value between 0 and 100!")
            except ValueError:
                print("Please enter a valid number!")
    return scores

def calculate_pr(t_value):
    """Calculate PR value and range based on T-score."""
    if t_value >= 60:
        return "High", 91
    elif 55 <= t_value <= 59:
        return "Slightly High", 75
    elif 45 <= t_value <= 54:
        return "Average", 50
    elif 40 <= t_value <= 44:
        return "Slightly Low", 25
    else:
        return "Low", 9

def plot_intelligence_chart(scores):
    """Plot the multiple intelligences bar chart."""
    categories = list(scores.keys())
    t_values = list(scores.values())
    pr_values = [calculate_pr(t)[1] for t in t_values]
    ranges = [calculate_pr(t)[0] for t in t_values]

    x = np.arange(len(categories))  # Define positions for each category

    # Create the chart
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(x, t_values, color='blue', alpha=0.7, edgecolor='black')
    
    # Add labels and ranges
    for bar, t_value, pr_value, t_range in zip(bars, t_values, pr_values, ranges):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f"T: {t_value:.1f}\nPR: {pr_value}\n{t_range}",
                ha='center', va='bottom', fontsize=10, color='black')

    # Set axis labels and ticks
    ax.set_title("Multiple Intelligences Chart", fontsize=16)
    ax.set_ylabel("Standard Scores (T-scores)", fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=10, rotation=45)
    ax.set_ylim(0, 100)

    # Add range lines
    ax.axhline(60, color='green', linestyle='--', linewidth=1, label="High")
    ax.axhline(55, color='lime', linestyle='--', linewidth=1, label="Slightly High")
    ax.axhline(45, color='orange', linestyle='--', linewidth=1, label="Average")
    ax.axhline(40, color='red', linestyle='--', linewidth=1, label="Slightly Low")
    ax.legend(loc='upper right')

    plt.tight_layout()
    plt.show()

def main():
    print("Welcome to the Multiple Intelligences Test!")
    scores = collect_scores()
    print("\nYour entered T-scores:")
    for category, score in scores.items():
        t_range, pr_value = calculate_pr(score)
        print(f"{category}: T-score = {score:.1f}, PR = {pr_value}, Range = {t_range}")

    plot_intelligence_chart(scores)

if __name__ == "__main__":
    main()
