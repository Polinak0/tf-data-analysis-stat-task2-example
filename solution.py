import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 470039295 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    #n=len(x)
    #mean = np.mean(x)
    #std_error=np.std(x)/np.sqrt(n)
    #t_value=norm.ppf(1-alpha/2,n-1)
    #lower_bound=mean-t_value*std_error
    #upper_bound=mean-t_value*std_error
    #return (lower_bound,upper_bound)
    loc = x.mean()
    return (loc - np.sqrt(np.var(x)) * norm.ppf(1 - alpha / 2) / np.sqrt(len(x)))/29**2, \
           (loc - np.sqrt(np.var(x)) * norm.ppf(alpha / 2) / np.sqrt(len(x)))/29**2
    #loc = x.mean()
    #scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    #return loc - scale * norm.ppf(1 - alpha / 2), \
           #loc - scale * norm.ppf(alpha / 2)
