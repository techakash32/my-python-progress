# 1. try and except

try:
    a=100
    try:
        b=10
        print(a/b)
    except:
        print("inner error")
    a+"gnkh"
    print("output is here")


except Exception as e:
    print("error is ",e)

# 2. try and else:

try:
    a=100
    a+"dfgbm"
    print("output is here")
except Exception as e:
    print("error =",e)
else:
    print("final block")

# 3. try and finally :

try:
    a=100
    print("output is here")
except Exception as e:
    print("error ocuured =",e)
finally:
    print("finally block")

# 4. raise:

account=15000
amount=4000
try :
    if amount>=account:
        print("account can be open")
    else:
        raise ValueError
except:
    print("value is less then ",account)