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


def load_dtc_data():
    train = pd.read_csv("Data/TTV Split/training.csv", header=0)
    train_y = train[[goal_variable]]
    train_x = train.drop(goal_variable, axis=1)
    test = pd.read_csv("Data/TTV Split/testing.csv", header=0)
    test_y = test[[goal_variable]]
    test_x = test.drop(goal_variable, axis=1)
    val = pd.read_csv("Data/TTV Split/validation.csv", header=0)
    val_y = val[[goal_variable]]
    val_x = val.drop(goal_variable, axis=1)
    
    train_x = pd.get_dummies(train_x, columns=categorical_cols, drop_first=False)
    train_x = pd.get_dummies(train_x, columns=bool_cols, drop_first=True)
    train_x = train_x.astype(int)
    
    val_x = pd.get_dummies(val_x, columns=categorical_cols, drop_first=False)
    val_x = pd.get_dummies(val_x, columns=bool_cols, drop_first=True)
    val_x = val_x.astype(int)
    
    test_x = pd.get_dummies(test_x, columns=categorical_cols, drop_first=False)
    test_x = pd.get_dummies(test_x, columns=bool_cols, drop_first=True)
    test_x = test_x.astype(int)
    
    return (train_x, np.array(train_y[goal_variable].values)), \
            (val_x, np.array(val_y[goal_variable].values)), \
            (test_x, np.array(test_y[goal_variable].values))


def load_dnn_data():
    from sklearn.preprocessing import StandardScaler
    
    train = pd.read_csv("Data/TTV Split/training.csv", header=0)
    train_y = train[[goal_variable]]
    train_x = train.drop(goal_variable, axis=1)
    test = pd.read_csv("Data/TTV Split/testing.csv", header=0)
    test_y = test[[goal_variable]]
    test_x = test.drop(goal_variable, axis=1)
    val = pd.read_csv("Data/TTV Split/validation.csv", header=0)
    val_y = val[[goal_variable]]
    val_x = val.drop(goal_variable, axis=1)

    scaler = StandardScaler()
    
    train_x[numerical_cols] = scaler.fit_transform(train_x[numerical_cols])
    train_x = pd.get_dummies(train_x, columns=categorical_cols, drop_first=False)
    train_x = pd.get_dummies(train_x, columns=bool_cols, drop_first=True)
    train_x = train_x.astype(int)
    
    val_x[numerical_cols] = scaler.transform(val_x[numerical_cols])
    val_x = pd.get_dummies(val_x, columns=categorical_cols, drop_first=False)
    val_x = pd.get_dummies(val_x, columns=bool_cols, drop_first=True)
    val_x = val_x.astype(int)

    test_x[numerical_cols] = scaler.transform(test_x[numerical_cols])   
    test_x = pd.get_dummies(test_x, columns=categorical_cols, drop_first=False)
    test_x = pd.get_dummies(test_x, columns=bool_cols, drop_first=True)
    test_x = test_x.astype(int)
    
    return (train_x, np.array(train_y[goal_variable].values)), \
            (val_x, np.array(val_y[goal_variable].values)), \
            (test_x, np.array(test_y[goal_variable].values))


def load_data(model:str):
    if model == 'linear-reg':
        train, test = load_lr_data()
        return train, test
    elif model == 'dec-tree-class':
        train, val, test = load_dtc_data()
        return train, val, test
    elif model == 'dnn':
        train, val, test = load_dtc_data()
        return train, val, test
    else:
        return "Unknown Model"