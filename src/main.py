import warnings
warnings.filterwarnings("ignore")

from data_cleaning import clean_data
from visualization import plot_all


def main():
    filepath = "../data/messy_sales.csv"

    # Clean data
    df = clean_data(filepath)

    # Visualization
    plot_all(df)

if __name__ == "__main__":
    main()