# Recommended Daily Intake Optimization
Nutritional information limited to what is tracked on MyFitnessPal.
Nutrition data from https://nutritiondata.self.com/

## TODO
- Add in optimization for single parameter based on calories for 2000 calorie goal (Should return single food)
- Add in optimization for two+ parameters based on calories for 2000 calorie goal (Should return two+ foods)
- Add in optimization for two+ parameters based on calories and macros for 2000 calorie goal and macro split (Should return two+ foods)
- Add in early stopping criteria/ hard cap (Stop after 1, multiple, or all goals are met)
- Add in weighting order for optimization (e.g. Prefer hitting protein over Vitamin A)
- Expand nutritional database
- Use MFP API for logged foods to expand nutrition database (If possible)
- Adjust optimization to account for specific nutrition goal (=,>,<. e.g. =2000 calories, >200 protein, <2300 sodium)
- Add a randomness variable or a serving limit (Will reduce optimization score for variability)
- Calculate baseline RDAs based on user input (Weight, height, age, nutritional goals, e.g. cut/maintain/bulk by n calories)