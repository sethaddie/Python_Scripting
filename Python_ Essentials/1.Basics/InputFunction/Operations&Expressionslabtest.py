hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total = mins + dura 
 
hr = int(total/60) 
 
end_hour = hour + hr 
end_min = total % 60 
 
end_time = str(end_hour) + ":" + str(end_min)  
 
    
print(end_time)