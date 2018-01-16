import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model,discriminant_analysis,cross_validation

def load_data():
    diabets = datasets.load_diabetes()
    return cross_validation.train_test_split(diabets.data,diabets.target,test_size = 0.25,random_state =0)