is_non_negative_num = lambda x: x.replace(".", "", 1).isdigit()
print(is_non_negative_num("2.123123"))