import matplotlib.pyplot as plt
import seaborn as sns


def plot_all(df):
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Bar Chart
    sns.barplot(data=df, x='Region', y='Total Sales', estimator=sum, ax=axes[0, 0])
    axes[0, 0].set_title('Total Sales by Region')
    axes[0, 0].tick_params(axis='x', rotation=30)

    # Line Chart
    df.groupby('Date')['Total Sales'].sum().plot(ax=axes[0, 1])
    axes[0, 1].set_title('Sales Trend Over Time')

    # Pie Chart
    category_sales = df.groupby('Category')['Total Sales'].sum()
    category_sales.plot(kind='pie', autopct='%1.1f%%', ax=axes[1, 0])
    axes[1, 0].set_title('Sales Share by Category')
    axes[1, 0].set_ylabel('')

    # Empty subplot
    axes[1, 1].axis('off')

    plt.tight_layout()

    # Center window
    try:
        manager = plt.get_current_fig_manager()
        window = manager.window

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        width, height = 1000, 700
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        window.geometry(f"{width}x{height}+{x}+{y}")
    except:
        pass

    plt.show()