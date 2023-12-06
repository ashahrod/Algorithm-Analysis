# Algorithm-Analysis
**Goal**:

  
  Record the running times of Selection Sort, Merge Sort, & Counting Sort, with a varying number of elements.
  
  Use trendlines and linear analysis to determine the time to sort 1,000,000 elements, with each sort.
  
**Process**:

  We will randomly generate a sequence of integers starting from 1000, to 50,000, in increments of 1000.
  
  These random integers will range from values [-10000000,10000000].
  
  This will give us 150 data points across the sorts.
  
  Plot the timing results, with the length of the sequence on the x-axis and running time on the y-axis.
  
  Use data to perform analysis.

**How to Run**:

  Compile the program using "./compile.sh"
  
  Run the program using "./run.sh $file1"
  
  where $file1 is a file with comma separated integers.
  
  ex: "./run.sh test_cases/in1.txt"
