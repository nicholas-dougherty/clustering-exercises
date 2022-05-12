```                                                                                                                                                                                                
   ____   ____   ____     ___  ____  __________ __________ ________   _______      ___   ____   
  6MMMMb/ `MM'   `MM'     `M' 6MMMMb\MMMMMMMMMM `MMMMMMMMM `MMMMMMMb. `MM'`MM\     `M'  6MMMMb/ 
 8P    YM  MM     MM       M 6M'    `/   MM   \  MM      \  MM    `Mb  MM  MMM\     M  8P    YM 
6M      Y  MM     MM       M MM          MM      MM         MM     MM  MM  M\MM\    M 6M      Y 
MM         MM     MM       M YM.         MM      MM    ,    MM     MM  MM  M \MM\   M MM        
MM         MM     MM       M  YMMMMb     MM      MMMMMMM    MM    .M9  MM  M  \MM\  M MM        
MM         MM     MM       M      `Mb    MM      MM    `    MMMMMMM9'  MM  M   \MM\ M MM     ___
MM         MM     MM       M       MM    MM      MM         MM  \M\    MM  M    \MM\M MM     `M'
YM      6  MM     YM       M       MM    MM      MM         MM   \M\   MM  M     \MMM YM      M 
 8b    d9  MM    / 8b     d8 L    ,M9    MM      MM      /  MM    \M\  MM  M      \MM  8b    d9 
  YMMMM9  _MMMMMMM  YMMMMM9  MYMMMM9    _MM_    _MMMMMMMMM _MM_    \M\_MM__M_      \M   YMMMM9
```

Clustering is...

- Unsupervised machine learning methodology
- Used to group and identify similar observations when we do not have labels that identify the groups.
- Often a preprocessing or an exploratory step in the data science pipeline.

Suppose you have a data set with observations, features, but no labels or target variable. You want to predict which group of similar observations a new observation will fall in. Without the labels, you cannot use a supervised algorithm, such as a random forest or KNN. We can address this challenge by finding groups of data in our dataset which are similar to one another. These groups are called clusters.

Clustering can also be used for data exploration, or to generate a new feature that can then be fed into a supervised model.

Formally, clustering is an unsupervised process of grouping similar observations or objects together. In this process similarities are based on comparing a vector of information for each observation or object, often using various mathematical distance functions.

Clustering methodologies include:

- Partitioned based clustering (K-Means)
- Hierarchical clustering
- Density-based clustering (Density-Based Spatial Clustering of Applications with Noise (DBSCAN))

Every methodology follows a different set of rules for defining the ‘similarity’ among data points. While there are more than 100 known clustering algorithms, few of the algorithms are popularly used, and we will be focusing on K-means in the coming lesson.
***
### Clustering Use Cases

- Text: Document classification, summarization, topic modeling, recommendations
- Geographic: Crime zones, housing prices
- Marketing: Customer segmentation, market research
- Anomaly Detection: Account takeover, security risk, fraud
- Image Processing: Radiology, security
***
### Vocabulary

##### Euclidean Distance
The shortest distance between two points in n-dimensional space, a.k.a. L2 distance.

##### Manhattan Distance

The distance between two points is the sum of the absolute differences of their Cartesian coordinates. Also known as: taxicab metric, rectilinear distance, norm, snake distance, city block distance, or Manhattan length.

##### Cosine Similarity

Cosine Similarity measures the cosine of the angle between two vectors to define similarity between two vectors. It is a measure of orientation and not magnitude: two vectors with the same orientation, i.e. parallel, have a cosine similarity of 1 indicating they are maximally "similar". Two vectors oriented at 90° relative to each other, i.e. perpendicular or orthogonal, have a similarity of 0 and are considered maximally "dissimilar". 

##### Sparse vs. Desnse Matrix

A sparse matrix is a matrix in which most of the elements are zero. By contrast, if most of the elements are nonzero, then the matrix is considered dense.
The number of zero-valued elements divided by the total number of elements (e.g., m × n for an m × n matrix) is called the sparsity of the matrix (which is equal to 1 minus the density of the matrix). Using those definitions, a matrix will be sparse when its sparsity is greater than 0.5.

In taxicab geometry, the red, yellow, and blue paths all have the same shortest path length of 12. In Euclidean geometry, the green line has length 6√2 ≈ 8.49 and is the unique shortest path.
***
#### Data Types

Input: Continuous data, or ordered discrete data at a minimum.

Output: Integer representing a cluster id. The number itself doesn't mean anything except that those who share the same number are most similar. In addition, the number doesn't compare to any of the other cluster id's beyond the fact that they are different.
***
