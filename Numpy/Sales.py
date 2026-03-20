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

# Array Indexing - one -dimensional array

x = np.arange(10)
print("x: ",x[0])
x1 = np.array([5, 0, 3, 3, 7, 9])
print("x1: ", x1[0])

# Array Indexing - multi-dimensional array
x2 = np.array([[3, 5, 2, 4], # Row 0
               [7, 6, 8, 8], # Row 1
               [1, 6, 7, 7]]) # Row 2
print("Accessing the last element: ", x2[2, -1]) # Accessing the last element
print("Accessing the element in the first row and fourth column: ", x2[0, 3]) # Accessing the element in the first row and fourth column
x2[0,0]= 12 # Modifying the element in the first row and first column
print("Modified element in the first row and first column: ", x2)