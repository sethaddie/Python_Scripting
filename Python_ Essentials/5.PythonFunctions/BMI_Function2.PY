
weight=float(input("Enter weight in pounds here:"))
height=float(input("Enter height in feet/inches here:"))####

def ft_and_inch_to_m(ft, inch= 0.0):
    return ft* 0.3048 + inch * 0.0254

def lb_to_kg(lb):
    return lb * 0.45359237

def bmi(weight, height):
    if height <1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

print(bmi(lb_to_kg(weight), ft_and_inch_to_m(height)))

#########################################################################################################################################

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.45359237


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2


print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))