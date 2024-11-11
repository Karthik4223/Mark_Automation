# # # # import pandas as pd
# # # # import random

# # # # # Load student data from Excel
# # # # input_file = 'Assigned_Grades.csv'  # Replace with the path to your file
# # # # df = pd.read_csv(input_file)

# # # # # Get user input for highest mark and average mark for T5 parts
# # # # highest_mark = int(input("Enter the highest possible mark for any single part of T5: "))
# # # # average_mark = int(input("Enter the average mark across the four parts of T5: "))

# # # # # Define grade-to-marks mappings and ranges
# # # # grade_to_t1_marks = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3}
# # # # t2_t3_ranges = {
# # # #     'A': (6, 7),  # Higher range for grades A and B
# # # #     'B': (5, 7),
# # # #     'C': (4, 6),  # Medium range for grades C and D
# # # #     'D': (4, 6),
# # # #     'E': (4, 5)   # Lower range for grade E
# # # # }

# # # # # Define total range for T5 based on grade, ensuring higher grades have higher totals
# # # # grade_to_t5_total_range = {
# # # #     'A': (average_mark * 4, highest_mark * 4),
# # # #     'B': (average_mark * 3.5, highest_mark * 3.5),
# # # #     'C': (average_mark * 3, highest_mark * 3),
# # # #     'D': (average_mark * 2.5, highest_mark * 2.5),
# # # #     'E': (average_mark * 2, highest_mark * 2)
# # # # }

# # # # # Track unique patterns
# # # # t2_t3_patterns = set()
# # # # t5_patterns = set()

# # # # # Function to assign marks for T2 and T3 with two parts, sum in range [4, 7]
# # # # def assign_t2_t3_marks(grade, max_attempts=10):
# # # #     min_sum, max_sum = t2_t3_ranges[grade]
    
# # # #     for _ in range(max_attempts):
# # # #         if grade == 'A':
# # # #             part1 = random.randint(3, 4)
# # # #             part2 = random.randint(3, 4)
# # # #         elif grade == 'B':
# # # #             part1 = random.randint(2, 4)
# # # #             part2 = random.randint(2, 4)
# # # #         elif grade == 'C':
# # # #             part1 = random.randint(2, 3)
# # # #             part2 = random.randint(2, 3)
# # # #         elif grade == 'D':
# # # #             part1 = random.randint(1, 3)
# # # #             part2 = random.randint(1, 3)
# # # #         else:  # grade == 'E'
# # # #             part1 = random.randint(1, 2)
# # # #             part2 = random.randint(1, 2)
        
# # # #         total = part1 + part2
# # # #         if min_sum <= total <= max_sum:
# # # #             pattern = (part1, part2)
# # # #             if pattern not in t2_t3_patterns or random.random() <= 0.05:
# # # #                 t2_t3_patterns.add(pattern)
# # # #                 return part1, part2

# # # #     # Fallback if unique pattern not found
# # # #     return part1, part2

# # # # # Function to assign marks for T5 with 4 parts based on user-defined highest mark and grade-based range
# # # # def assign_t5_marks(grade, max_attempts=10):
# # # #     min_total, max_total = grade_to_t5_total_range[grade]
# # # #     total_marks = random.randint(int(min_total), int(max_total))
    
# # # #     for _ in range(max_attempts):
# # # #         # Ensure each part is at least 10 and adjust dynamically
# # # #         remaining = total_marks
# # # #         parts = []
# # # #         for i in range(4):
# # # #             # Calculate maximum for this part while ensuring at least 10 for each remaining part
# # # #             max_part = min(highest_mark, remaining - 10 * (3 - i))
# # # #             if max_part < 10:
# # # #                 max_part = 10  # Set minimum to 10 to avoid invalid range

# # # #             part = random.randint(10, max_part)
# # # #             parts.append(part)
# # # #             remaining -= part

# # # #         # Ensure all four parts sum to `total_marks` and each part is within [10, highest_mark]
# # # #         if sum(parts) == total_marks and all(10 <= p <= highest_mark for p in parts):
# # # #             pattern = tuple(parts)
# # # #             if pattern not in t5_patterns or random.random() <= 0.05:
# # # #                 t5_patterns.add(pattern)
# # # #                 return parts

# # # #     # Fallback if unique pattern not found
# # # #     return parts

# # # # # Apply grading system to each student
# # # # df['T1'] = df['Grade'].map(grade_to_t1_marks)
# # # # df[['T2_Part1', 'T2_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
# # # # df[['T3_Part1', 'T3_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
# # # # df[['T5a', 'T5b', 'T5c', 'T5d']] = df['Grade'].apply(lambda grade: pd.Series(assign_t5_marks(grade)))

# # # # # Save results to a new Excel file
# # # # output_file = 'student_marks_assigned.xlsx'
# # # # df.to_excel(output_file, index=False)

# # # # print(f"Marks assigned and saved to {output_file}")

# # # import pandas as pd
# # # import random

# # # # Load student data from Excel
# # # input_file = 'Assigned_Grades.csv'  # Replace with the path to your file
# # # df = pd.read_csv(input_file)

# # # # Get user input for highest mark and average mark for T5 parts
# # # highest_mark = int(input("Enter the highest possible mark for any single part of T5: "))
# # # average_mark = int(input("Enter the average mark across the four parts of T5: "))

# # # # Define grade-to-marks mappings and ranges
# # # grade_to_t1_marks = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3}
# # # t2_t3_ranges = {
# # #     'A': (6, 7),  # Higher range for grades A and B
# # #     'B': (5, 7),
# # #     'C': (4, 6),  # Medium range for grades C and D
# # #     'D': (4, 6),
# # #     'E': (4, 5)   # Lower range for grade E
# # # }

# # # # Define total range for T5 based on grade, ensuring higher grades have higher totals
# # # grade_to_t5_total_range = {
# # #     'A': (average_mark * 4, highest_mark * 4),
# # #     'B': (average_mark * 3.5, highest_mark * 3.5),
# # #     'C': (average_mark * 3, highest_mark * 3),
# # #     'D': (average_mark * 2.5, highest_mark * 2.5),
# # #     'E': (average_mark * 2, highest_mark * 2)
# # # }

# # # # Track unique patterns
# # # t2_t3_patterns = set()
# # # t5_patterns = set()

# # # # Function to assign marks for T2 and T3 with priority on higher marks for higher grades
# # # def assign_t2_t3_marks(grade, max_attempts=10):
# # #     min_sum, max_sum = t2_t3_ranges[grade]
    
# # #     for _ in range(max_attempts):
# # #         # Assign values with a bias towards higher values for higher grades
# # #         if grade in ['A', 'B']:
# # #             part1 = random.randint(3, 4)
# # #             part2 = random.randint(max(2, min_sum - part1), 4)
# # #         elif grade in ['C', 'D']:
# # #             part1 = random.randint(2, 3)
# # #             part2 = random.randint(2, max_sum - part1)
# # #         else:  # grade == 'E'
# # #             part1 = 2
# # #             part2 = random.randint(2, max_sum - part1)
        
# # #         total = part1 + part2
# # #         if min_sum <= total <= max_sum:
# # #             pattern = (part1, part2)
# # #             if pattern not in t2_t3_patterns or random.random() <= 0.05:
# # #                 t2_t3_patterns.add(pattern)
# # #                 return part1, part2

# # #     return part1, part2

# # # # Function to assign marks for T5 with 4 parts based on user-defined highest mark and grade-based range
# # # def assign_t5_marks(grade, max_attempts=10):
# # #     min_total, max_total = grade_to_t5_total_range[grade]
# # #     total_marks = random.randint(int(min_total), int(max_total))
    
# # #     for _ in range(max_attempts):
# # #         remaining = total_marks
# # #         parts = []
# # #         for i in range(4):
# # #             max_part = min(highest_mark, remaining - 10 * (3 - i))
# # #             if max_part < 10:
# # #                 max_part = 10

# # #             part = random.randint(10, max_part)
# # #             parts.append(part)
# # #             remaining -= part

# # #         if sum(parts) == total_marks and all(10 <= p <= highest_mark for p in parts):
# # #             pattern = tuple(parts)
# # #             if pattern not in t5_patterns or random.random() <= 0.05:
# # #                 t5_patterns.add(pattern)
# # #                 return parts

# # #     return parts

# # # # Apply grading system to each student
# # # df['T1'] = df['Grade'].map(grade_to_t1_marks)
# # # df[['T2_Part1', 'T2_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
# # # df[['T3_Part1', 'T3_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
# # # df[['T5a', 'T5b', 'T5c', 'T5d']] = df['Grade'].apply(lambda grade: pd.Series(assign_t5_marks(grade)))

# # # # Validation and adjustment function
# # # def validate_and_adjust(df):
# # #     for index, row in df.iterrows():
# # #         grade = row['Grade']
        
# # #         # Check and adjust T2 and T3 parts
# # #         for target in ['T2', 'T3']:
# # #             parts_sum = row[f'{target}_Part1'] + row[f'{target}_Part2']
# # #             min_sum, max_sum = t2_t3_ranges[grade]
# # #             if not (min_sum <= parts_sum <= max_sum):
# # #                 part1, part2 = assign_t2_t3_marks(grade)
# # #                 df.at[index, f'{target}_Part1'] = part1
# # #                 df.at[index, f'{target}_Part2'] = part2
        
# # #         # Check and adjust T5 parts
# # #         total_t5 = row['T5a'] + row['T5b'] + row['T5c'] + row['T5d']
# # #         min_total, max_total = grade_to_t5_total_range[grade]
# # #         if not (min_total <= total_t5 <= max_total):
# # #             parts = assign_t5_marks(grade)
# # #             df.at[index, 'T5a'], df.at[index, 'T5b'], df.at[index, 'T5c'], df.at[index, 'T5d'] = parts

# # # # Validate and adjust the dataframe
# # # validate_and_adjust(df)

# # # # Calculate and display summary statistics for each target
# # # for target in ['T1', 'T2', 'T3', 'T5']:
# # #     if target == 'T5':
# # #         marks = df[['T5a', 'T5b', 'T5c', 'T5d']].sum(axis=1)
# # #     elif target == 'T2' or target == 'T3':
# # #         marks = df[[f'{target}_Part1', f'{target}_Part2']].sum(axis=1)
# # #     else:
# # #         marks = df[target]
    
# # #     print(f"Summary statistics for {target}:")
# # #     print(f"  Min: {marks.min()}")
# # #     print(f"  Max: {marks.max()}")
# # #     print(f"  Avg: {marks.mean():.2f}")
# # #     print()

# # # # Save results to a new Excel file
# # # output_file = 'student_marks_assigned.xlsx'
# # # df.to_excel(output_file, index=False)

# # # print(f"Marks assigned and saved to {output_file}")

# # import pandas as pd
# # import random

# # # Load student data from Excel
# # input_file = 'Assigned_Grades.csv'  # Replace with the path to your file
# # df = pd.read_csv(input_file)

# # # Get user input for highest mark and average mark for T5 parts
# # highest_mark = int(input("Enter the highest possible mark for any single part of T5: "))
# # average_mark = int(input("Enter the average mark across the four parts of T5: "))

# # # Define grade-to-marks mappings and ranges
# # grade_to_t1_marks = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3}
# # t2_t3_ranges = {
# #     'A': (6, 7),  # Higher range for grades A and B
# #     'B': (5, 7),
# #     'C': (4, 6),  # Medium range for grades C and D
# #     'D': (4, 6),
# #     'E': (4, 5)   # Lower range for grade E
# # }

# # # Define total range for T5 based on grade, ensuring higher grades have higher totals
# # grade_to_t5_total_range = {
# #     'A': (average_mark * 4, highest_mark * 4),
# #     'B': (average_mark * 3.5, highest_mark * 3.5),
# #     'C': (average_mark * 3, highest_mark * 3),
# #     'D': (average_mark * 2.5, highest_mark * 2.5),
# #     'E': (average_mark * 2, highest_mark * 2)
# # }

# # # Track unique patterns
# # t2_t3_patterns = set()
# # t5_patterns = set()

# # # Function to assign marks for T2 and T3 with priority on higher marks for higher grades
# # def assign_t2_t3_marks(grade, max_attempts=10):
# #     min_sum, max_sum = t2_t3_ranges[grade]
    
# #     for _ in range(max_attempts):
# #         # Assign values with a bias towards higher values for higher grades
# #         if grade in ['A', 'B']:
# #             part1 = random.randint(3, 4)
# #             part2 = random.randint(max(2, min_sum - part1), 4)
# #         elif grade in ['C', 'D']:
# #             part1 = random.randint(2, 3)
# #             part2 = random.randint(2, max_sum - part1)
# #         else:  # grade == 'E'
# #             part1 = 2
# #             part2 = random.randint(2, max_sum - part1)
        
# #         total = part1 + part2
# #         if min_sum <= total <= max_sum:
# #             pattern = (part1, part2)
# #             if pattern not in t2_t3_patterns or random.random() <= 0.05:
# #                 t2_t3_patterns.add(pattern)
# #                 return part1, part2

# #     return part1, part2

# # # Function to assign marks for T5 with 4 parts based on user-defined highest mark and grade-based range
# # def assign_t5_marks(grade, max_attempts=10):
# #     min_total, max_total = grade_to_t5_total_range[grade]
# #     total_marks = random.randint(int(min_total), int(max_total))
    
# #     for _ in range(max_attempts):
# #         remaining = total_marks
# #         parts = []
# #         for i in range(4):
# #             max_part = min(highest_mark, remaining - 10 * (3 - i))
# #             if max_part < 10:
# #                 max_part = 10

# #             part = random.randint(10, max_part)
# #             parts.append(part)
# #             remaining -= part

# #         if sum(parts) == total_marks and all(10 <= p <= highest_mark for p in parts):
# #             pattern = tuple(parts)
# #             if pattern not in t5_patterns or random.random() <= 0.05:
# #                 t5_patterns.add(pattern)
# #                 return parts

# #     return parts

# # # Apply grading system to each student
# # df['T1'] = df['Grade'].map(grade_to_t1_marks)
# # df[['T2_Part1', 'T2_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
# # df[['T3_Part1', 'T3_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
# # df[['T5a', 'T5b', 'T5c', 'T5d']] = df['Grade'].apply(lambda grade: pd.Series(assign_t5_marks(grade)))

# # # Validation and adjustment function
# # def validate_and_adjust(df):
# #     for index, row in df.iterrows():
# #         grade = row['Grade']
        
# #         # Check and adjust T2 and T3 parts
# #         for target in ['T2', 'T3']:
# #             parts_sum = row[f'{target}_Part1'] + row[f'{target}_Part2']
# #             min_sum, max_sum = t2_t3_ranges[grade]
# #             if not (min_sum <= parts_sum <= max_sum):
# #                 part1, part2 = assign_t2_t3_marks(grade)
# #                 df.at[index, f'{target}_Part1'] = part1
# #                 df.at[index, f'{target}_Part2'] = part2
        
# #         # Check and adjust T5 parts
# #         total_t5 = row['T5a'] + row['T5b'] + row['T5c'] + row['T5d']
# #         min_total, max_total = grade_to_t5_total_range[grade]
# #         if not (min_total <= total_t5 <= max_total):
# #             parts = assign_t5_marks(grade)
# #             df.at[index, 'T5a'], df.at[index, 'T5b'], df.at[index, 'T5c'], df.at[index, 'T5d'] = parts

# # # Validate and adjust the dataframe
# # validate_and_adjust(df)

# # # Calculate and display summary statistics for each target
# # for target in ['T1', 'T2', 'T3', 'T5']:
# #     if target == 'T5':
# #         marks = df[['T5a', 'T5b', 'T5c', 'T5d']].sum(axis=1)
# #     elif target == 'T2' or target == 'T3':
# #         marks = df[[f'{target}_Part1', f'{target}_Part2']].sum(axis=1)
# #     else:
# #         marks = df[target]
    
# #     print(f"Summary statistics for {target}:")
# #     print(f"  Min: {marks.min()}")
# #     print(f"  Max: {marks.max()}")
# #     print(f"  Avg: {marks.mean():.2f}")
# #     print()

# # # Display T4 statistics after reducing marks to a 20-point scale
# # df['T4'] = df[['T5a', 'T5b', 'T5c', 'T5d']].sum(axis=1) * 20 / (highest_mark * 4)
# # print("Summary statistics for T4 (20-point scale):")
# # print(f"  Min: {df['T4'].min()}")
# # print(f"  Max: {df['T4'].max()}")
# # print(f"  Avg: {df['T4'].mean():.2f}")
# # print()

# # # Save results to a new Excel file
# # output_file = 'student_marks_assigned.xlsx'
# # df.to_excel(output_file, index=False)

# # print(f"Marks assigned and saved to {output_file}")
# import pandas as pd
# import random

# # Load student data from Excel
# input_file = 'Assigned_Grades.csv'  # Replace with the path to your file
# df = pd.read_csv(input_file)

# # Get user input for highest mark and average mark for T5 parts
# highest_mark = int(input("Enter the highest possible mark for any single part of T5: "))
# average_mark = int(input("Enter the average mark across the four parts of T5: "))

# # Define grade-to-marks mappings and ranges
# grade_to_t1_marks = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3}
# t2_t3_ranges = {
#     'A': (6, 7),  # Higher range for grades A and B
#     'B': (5, 7),
#     'C': (4, 6),  # Medium range for grades C and D
#     'D': (4, 6),
#     'E': (4, 5)   # Lower range for grade E
# }

# # Define total range for T5 based on grade, ensuring higher grades have higher totals
# grade_to_t5_total_range = {
#     'A': (average_mark * 4, highest_mark * 4),
#     'B': (average_mark * 3.5, highest_mark * 3.5),
#     'C': (average_mark * 3, highest_mark * 3),
#     'D': (average_mark * 2.5, highest_mark * 2.5),
#     'E': (average_mark * 2, highest_mark * 2)
# }

# # Track unique patterns
# t2_t3_patterns = set()
# t5_patterns = set()

# # Function to assign marks for T2 and T3 with priority on higher marks for higher grades
# def assign_t2_t3_marks(grade, max_attempts=10):
#     min_sum, max_sum = t2_t3_ranges[grade]
    
#     for _ in range(max_attempts):
#         # Assign values with a bias towards higher values for higher grades
#         if grade in ['A', 'B']:
#             part1 = random.randint(3, 4)
#             part2 = random.randint(max(2, min_sum - part1), 4)
#         elif grade in ['C', 'D']:
#             part1 = random.randint(2, 3)
#             part2 = random.randint(2, max_sum - part1)
#         else:  # grade == 'E'
#             part1 = 2
#             part2 = random.randint(2, max_sum - part1)
        
#         total = part1 + part2
#         if min_sum <= total <= max_sum:
#             pattern = (part1, part2)
#             if pattern not in t2_t3_patterns or random.random() <= 0.05:
#                 t2_t3_patterns.add(pattern)
#                 return part1, part2

#     return part1, part2

# # Function to assign marks for T5 with 4 parts based on user-defined highest mark and grade-based range
# def assign_t5_marks(grade, max_attempts=10):
#     min_total, max_total = grade_to_t5_total_range[grade]
#     total_marks = random.randint(int(min_total), int(max_total))
    
#     for _ in range(max_attempts):
#         remaining = total_marks
#         parts = []
#         for i in range(4):
#             max_part = min(highest_mark, remaining - 10 * (3 - i))
#             if max_part < 10:
#                 max_part = 10

#             part = random.randint(10, max_part)
#             parts.append(part)
#             remaining -= part

#         if sum(parts) == total_marks and all(10 <= p <= highest_mark for p in parts):
#             pattern = tuple(parts)
#             if pattern not in t5_patterns or random.random() <= 0.05:
#                 t5_patterns.add(pattern)
#                 return parts

#     return parts

# # Apply grading system to each student
# df['T1'] = df['Grade'].map(grade_to_t1_marks)
# df[['T2_Part1', 'T2_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
# df[['T3_Part1', 'T3_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
# df[['T5a', 'T5b', 'T5c', 'T5d']] = df['Grade'].apply(lambda grade: pd.Series(assign_t5_marks(grade)))

# # Validation and adjustment function
# def validate_and_adjust(df):
#     for index, row in df.iterrows():
#         grade = row['Grade']
        
#         # Check and adjust T2 and T3 parts
#         for target in ['T2', 'T3']:
#             parts_sum = row[f'{target}_Part1'] + row[f'{target}_Part2']
#             min_sum, max_sum = t2_t3_ranges[grade]
#             if not (min_sum <= parts_sum <= max_sum):
#                 part1, part2 = assign_t2_t3_marks(grade)
#                 df.at[index, f'{target}_Part1'] = part1
#                 df.at[index, f'{target}_Part2'] = part2
        
#         # Check and adjust T5 parts
#         total_t5 = row['T5a'] + row['T5b'] + row['T5c'] + row['T5d']
#         min_total, max_total = grade_to_t5_total_range[grade]
#         if not (min_total <= total_t5 <= max_total):
#             parts = assign_t5_marks(grade)
#             df.at[index, 'T5a'], df.at[index, 'T5b'], df.at[index, 'T5c'], df.at[index, 'T5d'] = parts

# # Validate and adjust the dataframe
# validate_and_adjust(df)

# # Calculate T4 (scaled to 20-point scale)
# df['T4'] = df[['T5a', 'T5b', 'T5c', 'T5d']].sum(axis=1) * 20 / (highest_mark * 4)

# # Calculate and display summary statistics per grade
# print("Summary statistics by grade category:")
# for grade in df['Grade'].unique():
#     grade_df = df[df['Grade'] == grade]
#     print(f"\nGrade {grade} ({len(grade_df)} students):")
#     for target in ['T1', 'T2', 'T3', 'T5', 'T4']:
#         if target == 'T5':
#             marks = grade_df[['T5a', 'T5b', 'T5c', 'T5d']].sum(axis=1)
#         elif target == 'T2' or target == 'T3':
#             marks = grade_df[[f'{target}_Part1', f'{target}_Part2']].sum(axis=1)
#         else:
#             marks = grade_df[target]
        
#         print(f"  {target} - Min: {marks.min()}, Max: {marks.max()}, Avg: {marks.mean():.2f}")

# # Save results to a new Excel file
# output_file = 'student_marks_assigned.xlsx'
# df.to_excel(output_file, index=False)

# print(f"\nMarks assigned and saved to {output_file}")

import pandas as pd
import random

# Load student data from Excel
input_file = 'Assigned_Grades.csv'  # Replace with the path to your file
df = pd.read_csv(input_file)

# Get user input for highest mark and average mark for T5 parts
highest_mark = int(input("Enter the highest possible mark for any single part of T5: "))
average_mark = int(input("Enter the average mark across the four parts of T5: "))

# Define grade-to-marks mappings and ranges
grade_to_t1_marks = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3}
t2_t3_ranges = {
    'A': (6, 7),  # Higher range for grades A and B
    'B': (5, 7),
    'C': (4, 6),  # Medium range for grades C and D
    'D': (4, 6),
    'E': (4, 5)   # Lower range for grade E
}

# Define total range for T5 based on grade, ensuring higher grades have higher totals
grade_to_t5_total_range = {
    'A': (average_mark * 4, highest_mark * 4),
    'B': (average_mark * 3.5, highest_mark * 3.5),
    'C': (average_mark * 3, highest_mark * 3),
    'D': (average_mark * 2.5, highest_mark * 2.5),
    'E': (average_mark * 2, highest_mark * 2)
}

# Track unique patterns
t2_t3_patterns = set()
t5_patterns = set()

# Function to assign marks for T2 and T3 with priority on higher marks for higher grades
def assign_t2_t3_marks(grade, max_attempts=10):
    min_sum, max_sum = t2_t3_ranges[grade]
    
    for _ in range(max_attempts):
        # Assign values with a bias towards higher values for higher grades
        if grade in ['A', 'B']:
            part1 = random.randint(3, 4)
            part2 = random.randint(max(2, min_sum - part1), 4)
        elif grade in ['C', 'D']:
            part1 = random.randint(2, 3)
            part2 = random.randint(2, max_sum - part1)
        else:  # grade == 'E'
            part1 = 2
            part2 = random.randint(2, max_sum - part1)
        
        total = part1 + part2
        if min_sum <= total <= max_sum:
            pattern = (part1, part2)
            if pattern not in t2_t3_patterns or random.random() <= 0.05:
                t2_t3_patterns.add(pattern)
                return part1, part2

    return part1, part2

# Function to assign marks for T5 with 4 parts based on user-defined highest mark and grade-based range
def assign_t5_marks(grade, max_attempts=10):
    min_total, max_total = grade_to_t5_total_range[grade]
    total_marks = random.randint(int(min_total), int(max_total))
    
    for _ in range(max_attempts):
        remaining = total_marks
        parts = []
        for i in range(4):
            max_part = min(highest_mark, remaining - 10 * (3 - i))
            if max_part < 10:
                max_part = 10

            part = random.randint(10, max_part)
            parts.append(part)
            remaining -= part

        if sum(parts) == total_marks and all(10 <= p <= highest_mark for p in parts):
            pattern = tuple(parts)
            if pattern not in t5_patterns or random.random() <= 0.05:
                t5_patterns.add(pattern)
                return parts

    return parts

# Apply grading system to each student
df['T1'] = df['Grade'].map(grade_to_t1_marks)
df[['T2_Part1', 'T2_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
df[['T3_Part1', 'T3_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
df[['T5a', 'T5b', 'T5c', 'T5d']] = df['Grade'].apply(lambda grade: pd.Series(assign_t5_marks(grade)))

# Validation and adjustment function
def validate_and_adjust(df):
    for index, row in df.iterrows():
        grade = row['Grade']
        
        # Check and adjust T2 and T3 parts
        for target in ['T2', 'T3']:
            parts_sum = row[f'{target}_Part1'] + row[f'{target}_Part2']
            min_sum, max_sum = t2_t3_ranges[grade]
            if not (min_sum <= parts_sum <= max_sum):
                part1, part2 = assign_t2_t3_marks(grade)
                df.at[index, f'{target}_Part1'] = part1
                df.at[index, f'{target}_Part2'] = part2
        
        # Check and adjust T5 parts
        total_t5 = row['T5a'] + row['T5b'] + row['T5c'] + row['T5d']
        min_total, max_total = grade_to_t5_total_range[grade]
        if not (min_total <= total_t5 <= max_total):
            parts = assign_t5_marks(grade)
            df.at[index, 'T5a'], df.at[index, 'T5b'], df.at[index, 'T5c'], df.at[index, 'T5d'] = parts

# Validate and adjust the dataframe
validate_and_adjust(df)

# Calculate T4 (scaled to 20-point scale)
df['T4'] = df[['T5a', 'T5b', 'T5c', 'T5d']].sum(axis=1) * 20 / (highest_mark * 4)

# Calculate and display summary statistics per grade with counts of min, max, avg marks
print("Summary statistics by grade category with counts of min, max, and avg:")
for grade in df['Grade'].unique():
    grade_df = df[df['Grade'] == grade]
    print(f"\nGrade {grade} ({len(grade_df)} students):")
    for target in ['T1', 'T2', 'T3', 'T5', 'T4']:
        if target == 'T5':
            marks = grade_df[['T5a', 'T5b', 'T5c', 'T5d']].sum(axis=1)
        elif target == 'T2' or target == 'T3':
            marks = grade_df[[f'{target}_Part1', f'{target}_Part2']].sum(axis=1)
        else:
            marks = grade_df[target]

        min_mark = marks.min()
        max_mark = marks.max()
        avg_mark = marks.mean()

        count_min = (marks == min_mark).sum()
        count_max = (marks == max_mark).sum()
        count_avg = ((marks - avg_mark).abs() < 1).sum()  # Close to average within a tolerance of 1

        print(f"  {target} - Min: {min_mark} (Count: {count_min}), Max: {max_mark} (Count: {count_max}), Avg: {avg_mark:.2f} (Close to Avg Count: {count_avg})")

# Save results to a new Excel file
output_file = 'student_marks_assigned.xlsx'
df.to_excel(output_file, index=False)

print(f"\nMarks assigned and saved to {output_file}")
