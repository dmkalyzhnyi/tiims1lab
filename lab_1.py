import math
from collections import Counter
import statistics
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.ticker import PercentFormatter


def get_polygon_and_histogram_of_frequencies(data):
    count, bins, _ = plt.hist(data, bins=10, alpha=0.75, color='blue', edgecolor='black')
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    plt.plot(bin_centers, count, linestyle='-', marker='o')
    plt.xlabel('Значення')
    plt.ylabel('Частота')
    plt.title('Полігон та гістограма частот')
    plt.show()


def get_mean(data):
    n = len(data)
    result = sum(data) / n
    return round(result, 3)


def get_median(data):
    sorted_data = sorted(data)
    n = len(data)
    midpoint = n // 2
    if n % 2 == 0:
        result = (sorted_data[midpoint - 1] + sorted_data[midpoint]) / 2
    else:
        result = sorted_data[midpoint]
    return round(result, 3)


def get_mode(data):
    counts = Counter(data)
    max_count = max(counts.values())
    mode = [key for key, value in counts.items() if value == max_count]
    return mode


def get_sample_variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [round((x - mean), 3) ** 2 for x in data]
    result = sum(deviations) / (n - 1)
    return round(result, 3)


def get_sample_standard_deviation(data):
    result = math.sqrt(get_sample_variance(data))
    return round(result, 3)


def get_results(data):
    print("Вибіркове середнє: ", statistics.mean(data))
    print("Медіана: ", statistics.median(data))
    print("Мода: ", statistics.mode(data))
    print("Вибіркова дисперсія: ", statistics.pvariance(data))
    print("Середнє квадратичне відхилення: ", statistics.pstdev(data))


def get_diagram(data):
    fig = plt.figure(figsize=(10, 7))
    plt.boxplot(data)
    plt.show()


def get_pareto(data):
    data = pd.DataFrame({'values': data})

    data = data.sort_values(by='values', ascending=False)
    data['c'] = data['values'].cumsum() / data['values'].sum() * 100

    color1 = 'steelblue'
    color2 = 'red'
    line_size = 4

    fig, ax = plt.subplots()

    ax2 = ax.twinx()
    ax2.plot(data['values'], data['c'], color=color1, marker="D", ms=line_size)
    ax2.yaxis.set_major_formatter(PercentFormatter())

    ax.tick_params(axis='y', colors=color1)
    ax2.tick_params(axis='y', colors=color2)

    plt.show()


def get_pie_diagram(data):
    plt.pie(data)
    plt.show()
