try:
	high = int(row[4])
	low = int(row[5])
except ValueError:
	print(f"Missing data for {current_date}") 
else:
	print('todo va super')