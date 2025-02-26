# Ionic conductivity predictor 
- Database of Li conducting liquid and solid electrolytes (organic)
    - polymers, liquids, etc
- Predict thier ionic conductivity by machine learning
- Related paper
    - https://pubs.acs.org/doi/10.1021/jacs.9b11442
    - Database and models are slightly different from the original paper
        - i.e., copyright and available module version issues


# How to use?
## [DEMO server](https://ionpred.herokuapp.com/admin/) is available!
-  Just wait for ca. 30 seconds to load the page
- Login info
    - username: user
    - pass: user
- Database will reset every day
- Response is slow because it runs on a free server

## [Manual is here!](manual/Manual.md)

# Overview
## Chemical database
![about](manual/media/misc/chems.PNG)
## Electrolyte database
![about](manual/media/misc/pred.PNG)
## Predicted conductivity
- It can export the prediction data as a csv file
- Log10 (conductivity) is predicted
![about](manual/media/misc/csv.PNG)

# Version
- 2022.4.23 Update manual
- 2022.4.22 Add tag admin
- 2022.3.17 First prototype

# Author
- Kan Hatakeyama-Sato
- Waseda University
- https://kanhatakeyama.github.io/
- satokan@toki.waseda.(japan)