is_logged_in = True
is_admin = False

if is_logged_in and is_admin:
    print("welcome Admin!")
elif is_logged_in and not is_admin:
    print("welcome user!")
else:
    print("Access Denied.please log in.")