def print_name(first_name, last_name, reverse):
	if reverse:
		print(last_name, first_name)
	else:
		print(first_name, last_name)

print_name('jinjia', 'liu', True)
print_name('jinjia', 'liu', False)
print_name('jinjia', last_name='liu', reverse=True)