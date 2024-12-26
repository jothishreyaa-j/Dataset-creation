!pip install pandas

!pip install fpdf

#this part of the code creates the sample data set and generates only first five rows to check if it is in the required format

import pandas as pd
import random

# Parameters for the dataset
categories = ['Easy', 'Medium', 'Hard']
time_values = [5, 10, 15]
weight_values = [10, 20, 30, 40]

# Generating the first 5 sample rows
sample_data = []
for i in range(5):
    question = f"Sample question {i+1}: Describe a scenario relevant to category {random.choice(categories)}."
    category = random.choice(categories)
    time = random.choice(time_values)
    weight = random.choice(weight_values)
    sample_data.append({'Question': question, 'Category': category, 'Time (minutes)': time, 'Weight (marks)': weight})

# Creating a DataFrame
sample_df = pd.DataFrame(sample_data)
sample_df





#The below code creates and downloads the dataset

import pandas as pd
import random

# Parameters
num_samples = 10000  # Total dataset size
questions_per_category = num_samples // 3  # Even distribution across categories

# Time and Marks ranges (we'll use uniform distribution within these ranges)
time_min = 5  # Minimum time
time_max = 15  # Maximum time
marks_min = 10  # Minimum marks
marks_max = 50  # Maximum marks
time = int(input("Enter the required time in minutes:"))
marks = int(input("Enter the required marks:"))

# Generate dataset with specified constraints
data = []
for i in range(1, num_samples + 1):
    if i <= questions_per_category:
        category = 'Easy'
    elif i <= 2 * questions_per_category:
        category = 'Medium'
    else:
        category = 'Hard'

    # Generate time and weight using uniform distribution and round to nearest multiple of 5
    time = round(random.uniform(time_min, time_max) / 5) * 5
    weight = round(random.uniform(marks_min, marks_max) / 5) * 5

    text = f"This is a uniquely identifiable text snippet number {i}."
    data.append([f"Q{i:05d}", category, text, weight, time])

# Create the full dataset DataFrame
df = pd.DataFrame(data, columns=['ID', 'Category', 'Text', 'Weight', 'Time (minutes)'])

# Save the dataset to a CSV file
file_path = 'interview_questions_dataset_uniform.csv'
df.to_csv(file_path, index=False)

print(f"✅ Dataset successfully generated and saved as {file_path}")

from google.colab import files

# Download the generated dataset
files.download('interview_questions_dataset.csv')


#upload files into colab

from google.colab import files
uploaded = files.upload()


# Load the dataset into colab environment
file_path = '/content/interview_questions_dataset_2.csv'  #Path in Colab, modify if needed
df = pd.read_csv(file_path)



