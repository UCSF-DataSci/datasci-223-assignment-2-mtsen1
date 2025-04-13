# Analysis

### Debugging

To debug the 3_cohort_analysis.py, I found it easier to first remove the pipes so that I could check each part of the code. Next, I added print statements and try/except statements to try each part of the code and print the data structure or print an error message. By doing this, I could check each part of the script more intuitively. 

### Cohort Analysis Results

The final results revealed that average glucose, patient count, and average age increased as BMI range increased with the Underweight group having the lowest averages and least patients and the Obese group having the highest averages and greatest patient count. 

### Parquet 

Using Polars and converting the .csv file to a parquet allowed for more efficient processing especially through the lazy evaluation. More specifically, Polars operations such as filter() allowed for much faster processing than Pandas. 