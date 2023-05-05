from lab_1__ import get_polygon_and_histogram_of_frequencies, get_mean, get_median, get_sample_variance, \
        get_sample_standard_deviation, get_results, get_mode, get_pie_diagram, get_pareto, get_diagram

data = [4.08, 5.1, 3.58, 3.02, 2.98, 2.78, 3.14, 2.98, 4.71, 3.02, 1.66, 3.99,
        2.33, 3.92, 6.19, 1.45, 4.12, 2.27, 3.19, 1.94, 4.03, 3.91, 4.27, 7.31,
        5.25, 0.59, 3.82, 1.52, 0.09, 2.31, 2.13, 1.49, 1.92, 4.13, 1.64, 2.61,
        2.32, 5.65, 2.91, 1.76, 2.3, 2.44, 2.57, 1.57, 5.27, 1.36, 0.44, 4.6,
        3.62, 2.01, 2.56, 2.6, 1.35, 6.05, 3.75, 2.68, 2.96, 2.91, 1.22, 3.07,
        3.23, 1.01, 0.99, 1.98, 3.33, 3.01, 1.91, 4.4, 1.45, 1.49, 4.18, 4.49,
        3.14, 4.51, 2.55, 5.01, 3.25, 0.54, 4.3, 5.33, 4.18, 2.49, 3.75, 0.41,
        3.98, 4.13, 2.38, 2.11, 3.36, 3.27, 2.61, 3.98, 3.97, 5.2, 3.51, 0.55,
        2.14, 5.29, 2.41, 3.03, 2.59, 1.4, 1.18, 3.8, 3.18, 4.33, 1, 0.9, 2.71,
        3.58, 0.85, 3.4, 4.02, 4.06, 5.23, 3.67, 1.43, 3.57, 3.27, 2.91, 4.27,
        0.81, 2.02, 2.57, 3.18, 4.65, 3.2, 2.88, 4.68, 0.95, 1.94, 3.32, 2.65,
        4.78, 3.27, 6.09, 3.52, 4.64, 2.65, 1.96, 2.71, 1.58, 3.08, 3.75, 4.49,
        2.93, 2.44, 0.18]

get_polygon_and_histogram_of_frequencies(data)

print("Вибіркове середнє: ", get_mean(data))
print("Медіана: ", get_median(data))
print("Мода: ", get_mode(data))
print("Вибіркова дисперсія: ", get_sample_variance(data))
print("Середнє квадратичне відхилення: ", get_sample_standard_deviation(data))
print("----------------------------------------------------")
get_results(data)

get_diagram(data)
get_pareto(data)
get_pie_diagram(data)

