def reverse(s, willreturn):
    if s == "":
        return willreturn
    index = len(s) - 1
    willreturn = willreturn + s[index]


    
    s = s[0:len(s) - 1]

    
    
    return reverse(s, willreturn)

print(reverse("12345",""))
