import pandas as pd

class RDI:
    
    class Goals:

        def __init__(self):
            
            class parameters:
                def __init__(self):
                    self.value = 0
                    self.stopping_criteria = '='

            self.calories = parameters()
            self.protein = parameters()
            self.carbohydrates = parameters()
            self.fiber = parameters()
            self.sugars = parameters()
            self.fat = parameters()
            self.saturated_fat = parameters()
            self.polyunsaturated_fat = parameters()
            self.monounsaturated_fat = parameters()
            self.trans_fat = parameters()
            self.cholesterol = parameters()
            self.sodium = parameters()
            self.potassium = parameters()
            self.vitamin_a = parameters()
            self.vitamin_c = parameters()
            self.calcium = parameters()
            self.iron = parameters()
            
    def __init__(self):
        self.goals = RDI.Goals()




def select_food_choices(opt_foods, food_df):
    """
    Returns a DataFrame containing chosen foods from a database.

    Parameters:
    opt_foods (list): Foods to include in the optimization.
    
    food_df (DataFrame): DataFrame containing foods and nutritional profiles.

    Returns:
    DataFrame
    """

    selected_foods = food_df[food_df['Food'].isin(opt_foods)]
    return selected_foods

if __name__ == "__main__":
    # foods_df = pd.read_csv('data/RDI.csv')
    # opt_foods = ['Apple', 'Banana']
    # opt_nutrition = ['Calories, Protein']
    # calorie_goal = 2000
    # protein_goal = 200
    # out = select_food_choices(opt_foods=opt_foods, food_df=foods_df)
    # print(out)
    
    rdi = RDI()
    print(f"Value is: {RDI.goals.calories.stopping_criteria}")

