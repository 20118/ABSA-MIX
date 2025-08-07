# ABSA-MIX

This repository contains the dataset for our paper:
"Quality achhi hai (is good), satisfied! Towards aspect based sentiment analysis in code-mixed language"

Link to paper: https://www.sciencedirect.com/science/article/abs/pii/S0885230824000512

File restaurant.csv contains samples from the restaurant dataset and laptop.csv contains laptop reviews. 
Complete_restaurant_train.csv and Complete_restaurant_test.csv contain complete train and test sets for restaurant domain.
Complete_laptop_train.csv and Complete_laptop_test.csv contain complete train and test sets for laptop domain.


Data is present in the "CSV" format, annotated for aspect terms and corresponding polarities. Polarity can be positive, negative, neutral, or conflict.

## columns description
  * Column A represents the unique id of text
  * Column B contains the code-mixed reviews
  * Column C contains the number of aspect terms in the dataset
  * Column D contains the aspect terms present in the review sentence. 
  * A sentence can have zero, single, or multiple aspect terms. A comma separates multiple aspects.
  * Column E contains the sentiment class for each aspect. A comma separates multiple aspects.

## load.py contains sample code to load data 
