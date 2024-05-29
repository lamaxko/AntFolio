from AntFolio.utils.imports import *

def plot_cumulative_returns_portfolio(data, title=None):
    fig, ax = plt.subplots(figsize=(12, 6))

    if title is None:
        title = 'Cumulative Returns of Portfolio Over Time'

    for column in data.columns:
        ax.plot(data.index, data[column], label=column)
    
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Cumulative Return', fontsize=12)
    ax.set_title(title, fontsize=15, fontweight='bold', color='navy')
    ax.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')
    ax.minorticks_on()
    ax.grid(True, which='minor', linestyle=':', linewidth=0.5, color='lightgrey')
    ax.tick_params(axis='x', rotation=45)
    ax.legend(title='Portfolio')
    
    plt.tight_layout()
    plt.show()