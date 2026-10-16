# CSPC

## PW1 - Lab A

### Tests
- All three tests passed successfully with `pytest -v`.

### Speed comparison
- Pure Python: 3.7436 seconds
- NumPy: 0.0004 seconds
- NumPy speed-up: 10377.80x

### Conclusion
- The NumPy implementation is much faster than the pure-Python loop for a large simulation. All three tests passed, confirming that the decay simulation behaves as expected.

## PW1 - Lab B

### What I Built:

- In plot.py, I wrote code to read the data from decay_observed.csv and create graphs using the observed values.
- I used NumPy to calculate the analytical decay law with (lambda = 0.3) and the first observed count as (N0).
- I created a figure with two subplots to compare the observed data points with the analytical decay curve.
- I also created a Snakefile with a rule that runs plot.py and generates figure.png automatically.

### How to Use:
- Run `snakemake --cores 1 figure.png` to create figure.png in the same folder.
- Snakemake checks whether the output needs to be generated again. If the input files have not changed and the output already exists, it does not repeat the work.

### Results:
- The observed data shows that the particle count decreases over time.
- The analytical decay curve follows a similar pattern to the observed data, allowing us to compare the real measurements with the theoretical model.

### Expected Result:
![decay plot](https://private-user-images.githubusercontent.com/106445856/675667716-8c7594df-e366-4e1e-a701-4fffa3c48fc6.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTIxNDMwOTQsIm5iZiI6MTc5MjE0Mjc5NCwicGF0aCI6Ii8xMDY0NDU4NTYvNjc1NjY3NzE2LThjNzU5NGRmLWUzNjYtNGUxZS1hNzAxLTRmZmZhM2M0OGZjNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMDE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTAxNlQwOTI2MzRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zN2ZkNTZjYjdmMzNmMWIxMDNmNTI3ODA2MTM0ZWUyNzRhZjBlYzVjZTZhM2NkYzU4YTY4NDFhMTU3MjgxNDQyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.A3k-dhgp8yxBz6895rR_SbHEsQDE_c3c-8v_bpuJdQU)

### Conclusion:
- In this lab, we learned how to read data from a CSV file, plot it using Python and Matplotlib, and compare observed results with an analytical decay law. We also learned how to use Snakemake to automate the process of generating a figure. This makes the workflow easier to repeat and avoids unnecessary work when the input files have not changed.