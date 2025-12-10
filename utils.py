
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

def summarize_data(df):
    summary = df.describe().T
    return summary

def plot_numeric_data(df):
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    fig, axs = plt.subplots(len(numeric_cols), 1, figsize=(6, 4*len(numeric_cols)))
    if len(numeric_cols) == 1:
        axs = [axs]
    for i, col in enumerate(numeric_cols):
        sns.histplot(df[col], kde=True, ax=axs[i])
        axs[i].set_title(f"Distribution of {col}")
    plt.tight_layout()
    return fig

def plot_categorical_data(df):
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    fig, axs = plt.subplots(len(cat_cols), 1, figsize=(6, 4*len(cat_cols)))
    if len(cat_cols) == 1:
        axs = [axs]
    for i, col in enumerate(cat_cols):
        df[col].value_counts().plot(kind='bar', ax=axs[i])
        axs[i].set_title(f"Category Counts: {col}")
    plt.tight_layout()
    return fig
