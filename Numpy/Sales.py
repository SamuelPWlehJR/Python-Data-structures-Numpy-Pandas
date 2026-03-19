import numpy as np

# sales = np.array([
#   [1, 2, 3, 4, 6],
#  [4, 1, 1, 2, 3],
#  [1, 1, 1, 1, 2]
# ])

# sales_sum = np.sum(sales, axis=0)
# print(sales_sum)

# average_daily_sales = np.mean(sales)

# print(average_daily_sales)

# highest_daily_sales = np.max(sales)
# print(highest_daily_sales)


# sales_mean = np.mean(sales, axis=0)
# print(sales, axis=0)

# np.random.seed(0)
# array1 = np.random.randint(10, size=4)
# print("arrary1: ", array1)

# array2 = np.random.randint(10, size=(2, 4))
# print("array2: ", array2)

# array3 = np.random.randint(10, size=(3, 4, 5))
# print("array3: ", array3)

# print("numpy array attributes example:")
# print("array3 ndim: ", array3.ndim)
# print("array3 shape: ", array3.shape)
# print("array3 size: ", array3.size)
# print("array3 dtype: ", array3.dtype)
# print("array3 itemsize: ", array3.itemsize, "bytes")
# print("array3 nbytes: ", array3.nbytes, "bytes")

# mark = np.array([
#   [75, 80, 65, 70],
#   [40, 35, 50, 45],
#   [90, 88, 92, 85],
#   [60, 55, 58, 62],
#   [30, 45, 40, 35]
# ])

# new_mark = mark.copy()

# print(new_mark)

# mark[1] = 5
# print(mark)

# new_mark[new_mark < 50] += 100
# print(new_mark)

# passed_students = np.all(mark >= 50, axis=1)
# print(passed_students)


# generating random numbers
#salary = np.random.randint(1000, 5000, size=10)
#print(salary)

#average_salary = np.mean(salary)
#print("Average Salary: ", average_salary)

#median_salary = np.median(salary)
#print("median salary: ", median_salary)

#salary(salary <= average_salary) *= 2
#print("updadted salary: ", salary)

# 1. retail company has daily sales data for 3 products over 7 days
# stored in a 2D numpy array.

sales = np.array([
    [200, 220, 250, 230, 210, 260, 270],
    [150, 160, 170, 180, 175, 165, 155],
    [300, 310, 320, 330, 340, 350, 360]
])

# Total sales
total_sales = np.sum(sales)
print("Total sales: ", total_sales)

#calculate the total sales for each product.
total_sales_per_product = np.sum(sales, axis = 1)
print("Total sales per product: ", total_sales_per_product)

# calculate the total sales for each day.
total_sales_each_day = np.sum(sales, axis = 0)
print("Total sales each day: ", total_sales_each_day)


# find the average daily sales across all products.
average_daily_sales = np.mean(sales, axis = 0)
print("Average daily sales across all products: ", average_daily_sales)

# identify which product had the highest total weekly sales.
highest_total_weekly_sales = np.max(total_sales_per_product)
print("Hightest total weekly sales: ", highest_total_weekly_sales)

# on which day were total sales the highest?
day_highest_sales = np.max(sales, axis = 0)
print("Day with highest sales: ", day_highest_sales)