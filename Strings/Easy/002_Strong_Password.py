def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    strong_req = [False, False, False, False]
    for letter in password:
        if numbers.__contains__(letter):
           strong_req[0] = True
        elif lower_case.__contains__(letter):
            strong_req[1] = True
        elif upper_case.__contains__(letter):
            strong_req[2] = True
        elif special_characters.__contains__(letter):
            strong_req[3] = True

    extra_letters = 0
    for condition in strong_req:
        if not condition:
            extra_letters += 1

    total_letters = n + extra_letters
    if total_letters >= 6:
        return extra_letters
    else:
        return extra_letters + (6 - n - extra_letters)
