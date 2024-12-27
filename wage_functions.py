import re

# clean_wage function to clean rate from currency symbols
def clean_wage(rate:str)->str:
    """ Clean rate from currency symbols."""
    
    regex_pattern = r'[^0-9.]'
    rate = re.sub(regex_pattern,'',rate).strip()
    
    return rate


# function calculate_wage is used to calculate wage
def calculate_wage(hours:float, 
                   rate:float, 
                   date_range:str='m')->float:
    '''This calculates wage based on hours and rate.
        If date_range='m' then regular hours 173.3,
        if date_range='w' then regular hours 40! '''
    
    if not(isinstance(hours,float) or isinstance(rate,float)):
        #update data types if not correct
        hours = float(hours)
        rate = float(rate)

    if date_range=='m':
        regular_hours = 173.3
    elif date_range=='w':
        regular_hours = 40
    else:
        raise ValueError ('date_range excpets just "w" or "m" ')
        
    overtime_multiplier = 1.5

    if hours > regular_hours:
        regular_wage = regular_hours * rate
        overtime_hours = hours - regular_hours
        overtime_wage = overtime_hours * rate * overtime_multiplier
        total_wage = regular_wage + overtime_wage
    else:
        total_wage = hours * rate

    return total_wage