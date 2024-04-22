import pandas as pd
import numpy as np


bool_cols = [
    'Sex', 
    'Fruits', 'Veggies', 'HvyAlcoholConsump', 
    'PhysActivity', 'DiffWalk',
    'HighBP', 'Smoker', 'Stroke', 'HeartDiseaseorAttack',
    'AnyHealthcare', 'NoDocbcCost',
    ]

categorical_cols = [
    'Age', 
    'GenHlth',
    'HighCholCheck',
    'Education', 'Income'
    ]

numerical_cols = [
    'BMI', 'MentHlth', 'PhysHlth',
    ]

goal_variable = 'Diabetes_binary'


def load_lr_data():
    train = pd.read_csv("Data/TTV Split/training.csv", header=0)
    train_y = train[[goal_variable]]
    train_x = train.drop(goal_variable, axis=1)
    test = pd.read_csv("Data/TTV Split/testing.csv", header=0)
    test_y = test[[goal_variable]]
    test_x = test.drop(goal_variable, axis=1)
    val = pd.read_csv("Data/TTV Split/validation.csv", header=0)
    val_y = val[[goal_variable]]
    val_x = val.drop(goal_variable, axis=1)
    
    train_full_x = pd.concat([train_x, val_x]).reset_index().drop(['index'], axis=1)
    train_full_y = pd.concat([train_y, val_y]).reset_index().drop(['index'], axis=1)
    
    train_full_x = pd.get_dummies(train_full_x, columns=categorical_cols, drop_first=False)
    train_full_x = pd.get_dummies(train_full_x, columns=bool_cols, drop_first=True)
    train_full_x = train_full_x.astype(int)

    test_x = pd.get_dummies(test_x, columns=categorical_cols, drop_first=False)
    test_x = pd.get_dummies(test_x, columns=bool_cols, drop_first=True)
    test_x = test_x.astype(int)
    
    return (train_full_x.to_numpy(), np.array(train_full_y[goal_variable].values)), \
            (test_x.to_numpy(), np.array(test_y[goal_variable].values))


def load_data(model:str):
    if model == 'linear-reg':
        train, test = load_lr_data()
        return train, test
    else:
        return (1, 2)