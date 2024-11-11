# # import streamlit as st
# # import pandas as pd
# # import random

# # # Streamlit app title
# # st.title("Student Marks Assignment")

# # # User inputs for mark assignment
# # highest_mark = st.number_input("Enter the highest possible mark for any single part of T5:", min_value=10, max_value=20, value=17)
# # average_mark = st.number_input("Enter the average mark across the four parts of T5:", min_value=10, max_value=20, value=16)

# # # File upload section
# # uploaded_file = st.file_uploader("Upload CSV or Excel file with columns 'RegNo' and 'Grade'", type=["csv", "xlsx"])

# # if uploaded_file is not None:
# #     # Load the uploaded file
# #     if uploaded_file.name.endswith(".csv"):
# #         df = pd.read_csv(uploaded_file)
# #     else:
# #         df = pd.read_excel(uploaded_file)
    
# #     # Verify necessary columns
# #     if "RegNo" in df.columns and "Grade" in df.columns:
# #         st.write("File uploaded successfully!")
        
# #         # Define grade-to-marks mappings and ranges
# #         grade_to_t1_marks = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3}
# #         t2_t3_ranges = {
# #             'A': (6, 7),
# #             'B': (5, 7),
# #             'C': (4, 6),
# #             'D': (4, 6),
# #             'E': (4, 5)
# #         }
        
# #         # Define total range for T5 based on grade
# #         grade_to_t5_total_range = {
# #             'A': (average_mark * 4, highest_mark * 4),
# #             'B': (average_mark * 3.5, highest_mark * 3.5),
# #             'C': (average_mark * 3, highest_mark * 3),
# #             'D': (average_mark * 2.5, highest_mark * 2.5),
# #             'E': (average_mark * 2, highest_mark * 2)
# #         }
        
# #         # Function to assign marks for T2 and T3
# #         def assign_t2_t3_marks(grade):
# #             min_sum, max_sum = t2_t3_ranges[grade]
# #             part1 = random.randint(2, max_sum - 2)
# #             part2 = max(min_sum - part1, 2)  # Ensure both parts have minimum mark of 2
# #             return part1, part2

# #         # Function to assign marks for T5
# #         def assign_t5_marks(grade):
# #             min_total, max_total = grade_to_t5_total_range[grade]
# #             total_marks = random.randint(int(min_total), int(max_total))
# #             parts = []
# #             remaining = total_marks
# #             for i in range(4):
# #                 max_part = min(highest_mark, remaining - 10 * (3 - i))
# #                 if max_part < 10:
# #                     max_part = 10
# #                 part = random.randint(10, max_part)
# #                 parts.append(part)
# #                 remaining -= part
# #             return parts

# #         # Apply grading system to each student
# #         df['T1'] = df['Grade'].map(grade_to_t1_marks)
# #         df[['T2_Part1', 'T2_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
# #         df[['T3_Part1', 'T3_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
# #         df[['T5a', 'T5b', 'T5c', 'T5d']] = df['Grade'].apply(lambda grade: pd.Series(assign_t5_marks(grade)))
        
# #         # Calculate T4 as a 20-point scaled total of T5
# #         df['T4'] = df[['T5a', 'T5b', 'T5c', 'T5d']].sum(axis=1) * 20 / (highest_mark * 4)
        
# #         # Display the processed data
# #         st.write("Processed Data:")
# #         st.dataframe(df)
        
# #         # Display summary statistics per grade
# #         st.write("Summary Statistics by Grade:")
# #         for grade in df['Grade'].unique():
# #             grade_df = df[df['Grade'] == grade]
# #             st.write(f"\nGrade {grade} ({len(grade_df)} students):")
# #             summary = {}
# #             for target in ['T1', 'T2', 'T3', 'T5', 'T4']:
# #                 if target == 'T5':
# #                     marks = grade_df[['T5a', 'T5b', 'T5c', 'T5d']].sum(axis=1)
# #                 elif target == 'T2' or target == 'T3':
# #                     marks = grade_df[[f'{target}_Part1', f'{target}_Part2']].sum(axis=1)
# #                 else:
# #                     marks = grade_df[target]
                
# #                 min_mark = marks.min()
# #                 max_mark = marks.max()
# #                 avg_mark = marks.mean()
# #                 count_min = (marks == min_mark).sum()
# #                 count_max = (marks == max_mark).sum()
# #                 count_avg = ((marks - avg_mark).abs() < 1).sum()
                
# #                 summary[target] = {
# #                     'Min': min_mark, 'Min Count': count_min,
# #                     'Max': max_mark, 'Max Count': count_max,
# #                     'Avg': avg_mark, 'Close to Avg Count': count_avg
# #                 }
# #             st.write(pd.DataFrame(summary).T)
        
# #         # Option to download processed data
# #         st.write("Download Processed Data:")
# #         processed_file = df.to_csv(index=False).encode('utf-8')
# #         st.download_button("Download CSV", data=processed_file, file_name="processed_student_marks.csv", mime="text/csv")

# #     else:
# #         st.error("The uploaded file must contain 'RegNo' and 'Grade' columns.")

# import streamlit as st
# import pandas as pd
# import random

# # Streamlit app title
# st.title("Student Marks Assignment")

# # User inputs for mark assignment
# highest_mark = st.number_input("Enter the highest possible mark for any single part of T5:", min_value=10, max_value=20, value=17)
# average_mark = st.number_input("Enter the average mark across the four parts of T5:", min_value=10, max_value=20, value=16)

# # File upload section
# uploaded_file = st.file_uploader("Upload CSV or Excel file with columns 'RegNo' and 'Grade'", type=["csv", "xlsx"])

# if uploaded_file is not None:
#     # Load the uploaded file
#     if uploaded_file.name.endswith(".csv"):
#         df = pd.read_csv(uploaded_file)
#     else:
#         df = pd.read_excel(uploaded_file)
    
#     # Verify necessary columns
#     if "RegNo" in df.columns and "Grade" in df.columns:
#         st.write("File uploaded successfully!")
        
#         # Define grade-to-marks mappings and ranges with prioritization for higher grades
#         grade_to_t1_marks = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3}
#         t2_t3_ranges = {
#             'A': (6, 7),
#             'B': (5, 6),
#             'C': (4, 5),
#             'D': (4, 5),
#             'E': (4, 4)
#         }
        
#         # Define total range for T5 based on grade
#         grade_to_t5_total_range = {
#             'A': (average_mark * 4, highest_mark * 4),
#             'B': (average_mark * 3.5, highest_mark * 3.5),
#             'C': (average_mark * 3, highest_mark * 3),
#             'D': (average_mark * 2.5, highest_mark * 2.5),
#             'E': (average_mark * 2, highest_mark * 2)
#         }
        
#         # Function to assign marks for T2 and T3 with enforced ranking for higher grades
#         def assign_t2_t3_marks(grade):
#             min_sum, max_sum = t2_t3_ranges[grade]
#             part1 = random.randint(min_sum // 2, max_sum // 2)
#             part2 = max_sum - part1  # Ensure the sum stays within min_sum and max_sum
#             return part1, part2
#         def assign_t5_marks(grade):
#             min_total, max_total = grade_to_t5_total_range[grade]
#             total_marks = random.randint(int(min_total), int(max_total))
#             parts = []
#             remaining = total_marks
#             for i in range(4):
#                 # Calculate the maximum allowable part, but ensure it's at least 10
#                 max_part = min(highest_mark, remaining - (10 * (3 - i)))  # Reserve 10 for remaining parts
#                 if max_part < 10:
#                     max_part = 10  # Ensure each part is at least 10 to avoid the invalid range issue

#                 part = random.randint(10, max_part)
#                 parts.append(part)
#                 remaining -= part

#             return parts


#         # Apply grading system to each student
#         df['T1'] = df['Grade'].map(grade_to_t1_marks)
#         df[['T2_Part1', 'T2_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
#         df[['T3_Part1', 'T3_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
#         df[['T5a', 'T5b', 'T5c', 'T5d']] = df['Grade'].apply(lambda grade: pd.Series(assign_t5_marks(grade)))
        
#         # Calculate T4 as a 20-point scaled total of T5
#         df['T4'] = df[['T5a', 'T5b', 'T5c', 'T5d']].sum(axis=1) * 20 / (highest_mark * 4)
        
#         # Display the processed data
#         st.write("Processed Data:")
#         st.dataframe(df)
        
#         # Display summary statistics per grade
#         st.write("Summary Statistics by Grade:")
#         for grade in df['Grade'].unique():
#             grade_df = df[df['Grade'] == grade]
#             st.write(f"\nGrade {grade} ({len(grade_df)} students):")
#             summary = {}
#             for target in ['T1', 'T2', 'T3', 'T5', 'T4']:
#                 if target == 'T5':
#                     marks = grade_df[['T5a', 'T5b', 'T5c', 'T5d']].sum(axis=1)
#                 elif target == 'T2' or target == 'T3':
#                     marks = grade_df[[f'{target}_Part1', f'{target}_Part2']].sum(axis=1)
#                 else:
#                     marks = grade_df[target]
                
#                 min_mark = marks.min()
#                 max_mark = marks.max()
#                 avg_mark = marks.mean()
#                 count_min = (marks == min_mark).sum()
#                 count_max = (marks == max_mark).sum()
#                 count_avg = ((marks - avg_mark).abs() < 1).sum()
                
#                 summary[target] = {
#                     'Min': min_mark, 'Min Count': count_min,
#                     'Max': max_mark, 'Max Count': count_max,
#                     'Avg': avg_mark, 'Close to Avg Count': count_avg
#                 }
#             st.write(pd.DataFrame(summary).T)
        
#         # Option to download processed data
#         st.write("Download Processed Data:")
#         processed_file = df.to_csv(index=False).encode('utf-8')
#         st.download_button("Download CSV", data=processed_file, file_name="processed_student_marks.csv", mime="text/csv")

#     else:
#         st.error("The uploaded file must contain 'RegNo' and 'Grade' columns.")

import streamlit as st
import pandas as pd
import random

# Streamlit app title
st.title("Student Marks Assignment")

# User inputs for mark assignment
highest_mark = st.number_input("Enter the highest possible mark for any single part of T5:", min_value=10, max_value=20, value=17)
average_mark = st.number_input("Enter the average mark across the four parts of T5:", min_value=10, max_value=20, value=16)

# File upload section
uploaded_file = st.file_uploader("Upload CSV or Excel file with columns 'RegNo' and 'Grade'", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Load the uploaded file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    # Verify necessary columns
    if "RegNo" in df.columns and "Grade" in df.columns:
        st.write("File uploaded successfully!")
        
        # Define grade-to-marks mappings and ranges with prioritization for higher grades
        grade_to_t1_marks = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3}
        t2_t3_ranges = {
            'A': (6, 7),
            'B': (5, 6),
            'C': (4, 5),
            'D': (4, 5),
            'E': (4, 4)
        }
        
        # Define total range for T5 based on grade
        grade_to_t5_total_range = {
            'A': (average_mark * 4, highest_mark * 4),
            'B': (average_mark * 3.5, highest_mark * 3.5),
            'C': (average_mark * 3, highest_mark * 3),
            'D': (average_mark * 2.5, highest_mark * 2.5),
            'E': (average_mark * 2, highest_mark * 2)
        }
        
        # Function to assign marks for T2 and T3 with enforced ranking for higher grades
        def assign_t2_t3_marks(grade):
            min_sum, max_sum = t2_t3_ranges[grade]
            part1 = random.randint(min_sum // 2, max_sum // 2)
            part2 = max_sum - part1  # Ensure the sum stays within min_sum and max_sum
            return part1, part2

        # Function to assign marks for T5 with enforced ranking for higher grades
        def assign_t5_marks(grade):
            min_total, max_total = grade_to_t5_total_range[grade]
            total_marks = random.randint(int(min_total), int(max_total))
            parts = []
            remaining = total_marks
            for i in range(4):
                max_part = min(highest_mark, remaining - 10 * (3 - i))  # Reserve 10 for remaining parts
                if max_part < 10:
                    max_part = 10  # Ensure each part is at least 10 to avoid the invalid range issue

                part = random.randint(10, max_part)
                parts.append(part)
                remaining -= part

            return parts

        # Apply grading system to each student
        df['T1'] = df['Grade'].map(grade_to_t1_marks)
        df[['T2_Part1', 'T2_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
        df[['T3_Part1', 'T3_Part2']] = df['Grade'].apply(lambda grade: pd.Series(assign_t2_t3_marks(grade)))
        df[['T5a', 'T5b', 'T5c', 'T5d']] = df['Grade'].apply(lambda grade: pd.Series(assign_t5_marks(grade)))
        
        # Calculate Overall T5 as a 20-point scaled total of T5
        df['Overall T5'] = df[['T5a', 'T5b', 'T5c', 'T5d']].sum(axis=1) * 20 / (highest_mark * 4)
        
        # Display the processed data
        st.write("Processed Data:")
        st.dataframe(df)
        
        # Display summary statistics per grade
        st.write("Summary Statistics by Grade:")
        for grade in df['Grade'].unique():
            grade_df = df[df['Grade'] == grade]
            st.write(f"\nGrade {grade} ({len(grade_df)} students):")
            summary = {}
            for target in ['T1', 'T2', 'T3', 'T5', 'Overall T5']:
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
                count_avg = ((marks - avg_mark).abs() < 1).sum()
                
                summary[target] = {
                    'Min': min_mark, 'Min Count': count_min,
                    'Max': max_mark, 'Max Count': count_max,
                    'Avg': avg_mark, 'Close to Avg Count': count_avg
                }
            st.write(pd.DataFrame(summary).T)
        
        # Option to download processed data
        st.write("Download Processed Data:")
        processed_file = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", data=processed_file, file_name="processed_student_marks.csv", mime="text/csv")

    else:
        st.error("The uploaded file must contain 'RegNo' and 'Grade' columns.")
