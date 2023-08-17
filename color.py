#color formatting:
class colors:
	R = '\033[30;0m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
    
def error(text):
    return f"{colors.FAIL}" + text + f"{colors.R}"
def warning(text):
    return f"{colors.WARNING}" + text + f"{colors.R}"
def success(text):
    return f"{colors.OKGREEN}" + text + f"{colors.R}"
def progress(text):
    return f"{colors.OKBLUE}" + text + f"{colors.R}"



#usage example:
#print(color.progress("idi nahuy"))
