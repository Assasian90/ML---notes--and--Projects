# ML Day 1 – Statistics & Data Basics

These notes cover basic statistics and data concepts required for Machine Learning.

---

## Measures of Central Tendency
These describe the **center of the data**.

- **Mean**  
  Average of all values.  
  Formula: (sum of values) / (number of values)

- **Median**  
  Middle value after sorting the data.

- **Mode**  
  Value(s) that occur most frequently.

---

## Measures of Dispersion
These describe **how spread out the data is**.

- **Variance**  
  Average of squared differences from the mean.

- **Standard Deviation (SD)**  
  Square root of variance.  
  Shows how far values typically deviate from the mean.

- **Interquartile Range (IQR)**  
  Spread of the middle 50% of the data.  
  Formula:  
  IQR = Q3 − Q1

---

## Why Squaring is Used in Variance
- Differences from the mean can be positive or negative
- Squaring makes all values positive
- Larger deviations are penalized more

---

## Data Types

### Qualitative (Categorical)
- Non-numeric data
- Examples: branch, gender, department

### Quantitative (Numerical)
- Numeric data
- Examples: marks, salary, height

---

## Machine Learning Workflow
Data → Cleaning → Preprocessing → Modeling → Evaluation


---

## Regression vs Classification

- **Regression**
  - Predicts numeric values
  - Works on quantitative output
  - Example: salary prediction

- **Classification**
  - Assigns data to categories
  - Output is a class/label
  - Example: student branch allocation

---

## Example Dataset


4, 6, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 15, 18, 30


Count = 15

---

## Calculations

### Mean
- Mean = 12

### Median
- Median = 11

### Mode
- Mode = 8, 10, 12

---

## Quartiles
- Q1 = 8  
- Q2 (Median) = 11  
- Q3 = 14  

---

## Interquartile Range


IQR = Q3 − Q1 = 14 − 8 = 6


---

## Outlier Detection (IQR Method)

Formula:


Lower Bound = Q1 − 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR


Calculation:
- 1.5 × IQR = 9
- Lower Bound = 8 − 9 = −1
- Upper Bound = 14 + 9 = 23

Any value < −1 or > 23 is an outlier.

→ **30 is an outlier**

---

## Variance & Standard Deviation
- Variance ≈ 34.93
- Standard Deviation ≈ 5.91
