import streamlit as st
import pandas as pd
import random
from collections import Counter

# Streamlit app title
st.title("Student Marks Assignment")

# User inputs for mark assignment
highest_mark = st.number_input("Enter the highest possible mark for any single part of T5:", min_value=10, max_value=20, value=17)
average_mark = st.number_input("Enter the average mark across the four parts of T5:", min_value=10, max_value=20, value=16)

# File upload section
uploaded_file = st.file_uploader("Upload CSV or Excel file with columns 'RegNo' and 'Grade'", type=["csv", "xlsx"])

def assign_marks(df):
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
    
    # Track patterns to ensure uniqueness
    t2_t3_patterns = Counter()
    t5_patterns = set()  # Track unique combinations of all four parts in T5

    # Function to assign marks for T2 and T3 with alternating patterns for uniqueness
    def assign_t2_t3_marks(grade, flip=False):
        min_sum, max_sum = t2_t3_ranges[grade]
        part1, part2 = min_sum // 2, max_sum - min_sum // 2

        # Flip the pattern if flip is True
        if flip:
            part1, part2 = part2, part1

        pattern = (part1, part2)

        # Check if the pattern has been used less than the allowed max count
        if t2_t3_patterns[pattern] < 5:  # Limit of 5 identical patterns
            t2_t3_patterns[pattern] += 1
            return part1, part2
        else:
            # Use the other pattern if the current one has reached the threshold
            return part2, part1

    # Function to assign marks for T5 with unique patterns across all four parts, min mark set to 10
    def assign_t5_marks(grade):
        min_total, max_total = grade_to_t5_total_range[grade]
        total_marks = random.randint(int(min_total), int(max_total))
        
        for _ in range(100):  # Limit retries to prevent infinite loop
            remaining = total_marks
            parts = []
            
            for i in range(4):
                # Ensure each part is at least 10 and within the calculated maximum
                max_part = min(highest_mark, remaining - 10 * (3 - i))
                if max_part < 10:
                    max_part = 10

                part = random.randint(10, max_part)
                parts.append(part)
                remaining -= part
            
            # Convert parts to a tuple and check for uniqueness
            pattern = tuple(parts)
            
            # Check if the pattern is unique
            if pattern not in t5_patterns:
                t5_patterns.add(pattern)  # Add to the set of unique patterns
                return parts

        # If unable to find a unique pattern after retries, return the parts as-is
        return parts

    # Apply grading system to each student with alternating patterns in T2 and T3
    df['T1'] = df['Grade'].map(grade_to_t1_marks)
    flip = False
    for i in range(len(df)):
        grade = df.at[i, 'Grade']
        df.at[i, 'T2_Part1'], df.at[i, 'T2_Part2'] = assign_t2_t3_marks(grade, flip)
        df.at[i, 'T3_Part1'], df.at[i, 'T3_Part2'] = assign_t2_t3_marks(grade, not flip)
        flip = not flip

    df[['T5a', 'T5b', 'T5c', 'T5d']] = df['Grade'].apply(lambda grade: pd.Series(assign_t5_marks(grade)))
    
    # Calculate Overall T5 as a 20-point scaled total of T5
    df['Overall T5'] = df[['T5a', 'T5b', 'T5c', 'T5d']].sum(axis=1) * 20 / (highest_mark * 4)
    return df

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    # Verify necessary columns
    if "RegNo" in df.columns and "Grade" in df.columns:
        st.write("File uploaded successfully!")
        
        # Initial mark assignment
        df = assign_marks(df)
        
        # Display the processed data
        st.write("Processed Data:")
        st.dataframe(df)
        
        # Add a re-run button
        if st.button("Re-run Mark Assignment"):
            df = assign_marks(df)
            st.write("Updated Mark Assignment:")
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
