a = int(input("Enter First Product Price : "))
b = int(input("Enter Second Product Price : "))
c = int(input("Enter Third Product Price : "))
def  buy_get_one_free(p1,p2,p3):
    free = 0
    if b > a < c:
        free += a 
    elif  a > b < c:
        free += b
    else:
        free += c
    return free

print(f"Free Product is {buy_get_one_free(a,b,c)}")
total = a+b+c-(buy_get_one_free(a,b,c))
print(f"Total product  Value : {total}")

def tax(t):
    tax = 0
    if total < 2000:
        tax += 0
    elif 4000 < total > 2000:
        disc = (total * 5)/100
        tax += disc
    elif 4000 < total > 6000:
        disc = (total * 10)/100
        tax += disc
    elif total > 6000:
        disc = (total*20)/100
        tax += disc
    return tax

print(f"Your Discount Value is {tax(total)}")
print(f"Your Total Paid Amount is {total-tax(total)}")

        
