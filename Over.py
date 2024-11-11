import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Streamlit app title
st.title("Detailed Student Marks Analysis Report")

# User inputs for mark assignment
highest_mark = st.number_input("Enter the highest possible mark for any single part of T5:", min_value=10, max_value=20, value=17)
average_mark = st.number_input("Enter the average mark across the four parts of T5:", min_value=10, max_value=20, value=16)

# File upload section
uploaded_file = st.file_uploader("Upload CSV or Excel file with columns 'RegNo', 'Grade', and 'Attendance'", type=["csv", "xlsx"])

# Grade-to-marks mapping with higher marks for higher grades
grade_to_t1_marks = {'S': 7, 'A': 6, 'B': 5, 'C': 4, 'D': 3, 'E': 2}

# Attendance-based adjustment marks table
attendance_adjustment = {
    '0-49%': {'T2_T3': 0, 'T5': 0},
    '50-64%': {'T2_T3': 0, 'T5': 0},
    '65-74%': {'T2_T3': 0, 'T5': 1},
    '75-84%': {'T2_T3': 1, 'T5': 2},
    '85-94%': {'T2_T3': 2, 'T5': 2},
    '95% and above': {'T2_T3': 2, 'T5': 3}
}

# Report-specific attendance ranges
report_attendance_ranges = ['≥75%', '≥65 - <75%', '≥50 - <65%', '<50']

# Function to determine attendance range category for assigning additional marks
def get_adjustment_range(attendance):
    if attendance < 50:
        return '0-49%'
    elif 50 <= attendance < 65:
        return '50-64%'
    elif 65 <= attendance < 75:
        return '65-74%'
    elif 75 <= attendance < 85:
        return '75-84%'
    elif 85 <= attendance < 95:
        return '85-94%'
    else:
        return '95% and above'

# Function to determine attendance range category for reporting purposes
def get_report_range(attendance):
    if attendance >= 75:
        return '≥75%'
    elif 65 <= attendance < 75:
        return '≥65 - <75%'
    elif 50 <= attendance < 65:
        return '≥50 - <65%'
    else:
        return '<50'

# Adjust marks based on attendance
def adjust_marks_based_on_attendance(row, attendance_adj):
    if row['T2_Part1'] + row['T2_Part2'] < 5:
        row['T2_Part1'] += attendance_adj['T2_T3'] // 2
        row['T2_Part2'] += attendance_adj['T2_T3'] - (attendance_adj['T2_T3'] // 2)
    if row['T3_Part1'] + row['T3_Part2'] < 5:
        row['T3_Part1'] += attendance_adj['T2_T3'] // 2
        row['T3_Part2'] += attendance_adj['T2_T3'] - (attendance_adj['T2_T3'] // 2)
    if sum([row['T5a'], row['T5b'], row['T5c'], row['T5d']]) < 11:
        adjustment = attendance_adj['T5']
        row['T5a'] += adjustment // 4
        row['T5b'] += adjustment // 4
        row['T5c'] += adjustment // 4
        row['T5d'] += adjustment - (3 * (adjustment // 4))
    return row

# Function to assign marks based on grade and attendance
# Function to assign marks based on grade and attendance
def assign_marks(df):
    t2_t3_ranges = {
        'S': (6, 7),
        'A': (5, 6),
        'B': (5, 6),
        'C': (4, 5),
        'D': (4, 5),
        'E': (4, 4)
    }
    grade_to_t5_total_range = {
        'S': (average_mark * 4, highest_mark * 4),
        'A': (average_mark * 3.5, highest_mark * 3.5),
        'B': (average_mark * 3, highest_mark * 3),
        'C': (average_mark * 2.5, highest_mark * 2.5),
        'D': (average_mark * 2, highest_mark * 2),
        'E': (average_mark * 2, highest_mark * 2)
    }

    # Ensure the grade is valid; if invalid, default to 'E'
    def get_valid_grade(grade):
        if grade not in t2_t3_ranges:
            return 'E'  # Default to 'E' if the grade is not valid
        return grade

    def assign_t2_t3_marks(grade, flip=False):
        grade = get_valid_grade(grade)  # Ensure valid grade
        min_sum, max_sum = t2_t3_ranges[grade]
        part1, part2 = min_sum // 2, max_sum - min_sum // 2
        if flip:
            part1, part2 = part2, part1
        return part1, part2

    def assign_t5_marks(grade):
        grade = get_valid_grade(grade)  # Ensure valid grade
        min_total, max_total = grade_to_t5_total_range[grade]
        
        # T5 mark ranges are adjusted for different grades
        total_marks = random.randint(int(min_total), int(max_total))
        
        # Distribute the marks among the 4 parts while ensuring no overlap
        parts = []
        remaining = total_marks
        
        # Ensure each part gets at least 10 marks, adjusting the remaining sum
        for i in range(4):
            max_part = min(highest_mark, remaining - (10 * (3 - i)))  # Ensure the remaining can accommodate the parts
            part = random.randint(10, max_part) if max_part >= 10 else 10
            parts.append(part)
            remaining -= part
        
        return parts

    df['T1'] = df['Grade'].map(grade_to_t1_marks)
    flip = False
    for i in range(len(df)):
        grade = df.at[i, 'Grade']
        attendance = df.at[i, 'Attendance']
        adjustment_range = get_adjustment_range(attendance)
        attendance_adj = attendance_adjustment[adjustment_range]

        # Assign marks for T2 and T3 with alternating patterns
        df.at[i, 'T2_Part1'], df.at[i, 'T2_Part2'] = assign_t2_t3_marks(grade, flip)
        df.at[i, 'T3_Part1'], df.at[i, 'T3_Part2'] = assign_t2_t3_marks(grade, not flip)
        flip = not flip

        # Assign marks for T5
        df.at[i, 'T5a'], df.at[i, 'T5b'], df.at[i, 'T5c'], df.at[i, 'T5d'] = assign_t5_marks(grade)
        df.iloc[i] = adjust_marks_based_on_attendance(df.iloc[i], attendance_adj)
    
    # Scale T5 to 20-point system
    df['Overall T5'] = df[['T5a', 'T5b', 'T5c', 'T5d']].sum(axis=1) * 20 / (highest_mark * 4)
    df['Total'] = df['T1'] + df[['T2_Part1', 'T2_Part2', 'T3_Part1', 'T3_Part2']].sum(axis=1) + df['Overall T5']
    
    return df

# Main function to generate the report
def generate_report():
    # Ensure file is uploaded
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        if "RegNo" in df.columns and "Grade" in df.columns and "Attendance" in df.columns:
            st.write("File uploaded successfully!")
            
            # Initial mark assignment
            df = assign_marks(df)
            
            # Display assigned marks per student
            st.subheader("Assigned Marks for Each Student")
            st.dataframe(df)
            
            # Summary of Highest, Lowest, and Average Marks
            st.subheader("Detailed Report Summary")
            summary_data = {
                'T1': [df['T1'].max(), df['T1'].min(), df['T1'].mean()],
                'T2': [df[['T2_Part1', 'T2_Part2']].sum(axis=1).max(), df[['T2_Part1', 'T2_Part2']].sum(axis=1).min(), df[['T2_Part1', 'T2_Part2']].sum(axis=1).mean()],
                'T3': [df[['T3_Part1', 'T3_Part2']].sum(axis=1).max(), df[['T3_Part1', 'T3_Part2']].sum(axis=1).min(), df[['T3_Part1', 'T3_Part2']].sum(axis=1).mean()],
                'Overall T5': [df['Overall T5'].max(), df['Overall T5'].min(), df['Overall T5'].mean()],
                'Total': [df['Total'].max(), df['Total'].min(), df['Total'].mean()]
            }

            summary_df = pd.DataFrame(summary_data, index=['Highest', 'Lowest', 'Average'])
            st.dataframe(summary_df)

            # Differences between averages for T1, T2 + T3, and Overall T5
            st.subheader("Summary of Differences Between Averages")

            avg_t1 = df['T1'].mean()
            avg_t2_t3 = df[['T2_Part1', 'T2_Part2', 'T3_Part1', 'T3_Part2']].sum(axis=1).mean()
            avg_t5_scaled = df['Overall T5'].mean()  # T5 is already scaled to 20 points
            avg_total = df['Total'].mean()

            diff_t1_t2_t3 = abs(avg_t1 - avg_t2_t3)
            diff_t5_t1_t2_t3 = abs(avg_t5_scaled - (avg_t1 + avg_t2_t3))

            st.write(f"**Difference between average marks of T1 & (T2 + T3):** {diff_t1_t2_t3:.2f} ({(diff_t1_t2_t3 / avg_t1) * 100:.1f}%)")
            st.write(f"**Difference between average marks of T5 (for 20 marks) & (T1 + T2 + T3):** {diff_t5_t1_t2_t3:.2f} ({(diff_t5_t1_t2_t3 / (avg_t1 + avg_t2_t3)) * 100:.1f}%)")

            # Attendance-Based Module 1 Marks Distribution Table
            st.subheader("Attendance-Based Module 1 Marks Distribution")
            mark_ranges = ['<=10', '>10 & <=20', '>20 & <=30', '>30 & <=40', '>40 & <=60']

            # Initialize the DataFrame for the attendance-based distribution
            attendance_mark_dist = pd.DataFrame(index=report_attendance_ranges, columns=mark_ranges).fillna(0)

            # Fill in the attendance-based distribution counts based on the conditions
            for idx, row in df.iterrows():
                report_range = get_report_range(row['Attendance'])
                total_marks = row['Total']
                if total_marks <= 10:
                    attendance_mark_dist.at[report_range, '<=10'] += 1
                elif total_marks <= 20:
                    attendance_mark_dist.at[report_range, '>10 & <=20'] += 1
                elif total_marks <= 30:
                    attendance_mark_dist.at[report_range, '>20 & <=30'] += 1
                elif total_marks <= 40:
                    attendance_mark_dist.at[report_range, '>30 & <=40'] += 1
                else:
                    attendance_mark_dist.at[report_range, '>40 & <=60'] += 1

            attendance_mark_dist['Total'] = attendance_mark_dist.sum(axis=1)
            attendance_mark_dist.loc['Total'] = attendance_mark_dist.sum()

            st.dataframe(attendance_mark_dist)

            # Plotting bell curves for each target and total
            st.subheader("Marks Distribution (Bell Curves) for Each Target and Total")

            fig, axes = plt.subplots(2, 2, figsize=(14, 10))

            # Define a function to plot bell curves
            def plot_bell_curve(data, ax, title):
                mean = np.mean(data)
                std_dev = np.std(data)
                x = np.linspace(min(data), max(data), 100)
                y = norm.pdf(x, mean, std_dev)
                ax.plot(x, y, color='blue')
                ax.set_title(title)
                ax.set_xlabel("Marks")
                ax.set_ylabel("Density")
                ax.fill_between(x, y, alpha=0.2)  # Shade under the curve for better visualization

            # Plot T1 distribution as a bell curve
            plot_bell_curve(df['T1'], axes[0, 0], "Distribution of T1 Marks")

            # Plot T2 + T3 combined marks distribution as a bell curve
            plot_bell_curve(df[['T2_Part1', 'T2_Part2', 'T3_Part1', 'T3_Part2']].sum(axis=1), axes[0, 1], "Distribution of T2 + T3 Marks")

            # Plot Overall T5 distribution as a bell curve
            plot_bell_curve(df['Overall T5'], axes[1, 0], "Distribution of Overall T5 Marks")

            # Plot Total as a bell curve
            plot_bell_curve(df['Total'], axes[1, 1], "Distribution of Total Marks")

            st.pyplot(fig)

            # Provide an option to download the processed data as a CSV
            st.write("**Download Processed Data**")
            processed_file = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV", data=processed_file, file_name="processed_student_marks.csv", mime="text/csv")
            
            # Button to reassign marks if user is not satisfied
            if st.button("Reassign Marks"):
                st.write("Reassigning marks...")
                df = assign_marks(df)  # Reassign marks
                st.write("Marks reassigned successfully!")
                
                # Re-display all the results after reassignment
                st.subheader("Assigned Marks for Each Student")
                st.dataframe(df)

                # Re-calculate and display the summary
                st.subheader("Detailed Report Summary")
                summary_data = {
                    'T1': [df['T1'].max(), df['T1'].min(), df['T1'].mean()],
                    'T2': [df[['T2_Part1', 'T2_Part2']].sum(axis=1).max(), df[['T2_Part1', 'T2_Part2']].sum(axis=1).min(), df[['T2_Part1', 'T2_Part2']].sum(axis=1).mean()],
                    'T3': [df[['T3_Part1', 'T3_Part2']].sum(axis=1).max(), df[['T3_Part1', 'T3_Part2']].sum(axis=1).min(), df[['T3_Part1', 'T3_Part2']].sum(axis=1).mean()],
                    'Overall T5': [df['Overall T5'].max(), df['Overall T5'].min(), df['Overall T5'].mean()],
                    'Total': [df['Total'].max(), df['Total'].min(), df['Total'].mean()]
                }
                
                summary_df = pd.DataFrame(summary_data, index=['Highest', 'Lowest', 'Average'])
                st.dataframe(summary_df)
                
                # Recalculate and display differences between averages
                st.subheader("Summary of Differences Between Averages")

                avg_t1 = df['T1'].mean()
                avg_t2_t3 = df[['T2_Part1', 'T2_Part2', 'T3_Part1', 'T3_Part2']].sum(axis=1).mean()
                avg_t5_scaled = df['Overall T5'].mean()  # T5 is already scaled to 20 points
                avg_total = df['Total'].mean()

                diff_t1_t2_t3 = abs(avg_t1 - avg_t2_t3)
                diff_t5_t1_t2_t3 = abs(avg_t5_scaled - (avg_t1 + avg_t2_t3))

                st.write(f"**Difference between average marks of T1 & (T2 + T3):** {diff_t1_t2_t3:.2f} ({(diff_t1_t2_t3 / avg_t1) * 100:.1f}%)")
                st.write(f"**Difference between average marks of T5 (for 20 marks) & (T1 + T2 + T3):** {diff_t5_t1_t2_t3:.2f} ({(diff_t5_t1_t2_t3 / (avg_t1 + avg_t2_t3)) * 100:.1f}%)")
                
                # Re-display the attendance-based distribution table
                st.subheader("Attendance-Based Module 1 Marks Distribution")
                st.dataframe(attendance_mark_dist)

                # Re-plot the bell curves for all targets and total
                st.subheader("Marks Distribution (Bell Curves) for Each Target and Total")
                st.pyplot(fig)

        else:
            st.error("The uploaded file must contain 'RegNo', 'Grade', and 'Attendance' columns.")

# Execute the function to generate the report
generate_report()
