weather= input("what's the weather like today? (sunny/rainy/cold):")
weather=["sunny","rainy","cold"]
if weather=="sunny":
    print("wear a t-shirt and sunglasses:")
elif weather=="rainny":
    print("don't forget umbrella and raincoat")
elif weather=="cold":
    print("make sure to wear a coat and scarf:")
else:
    print("sorry,i don't have recommendations for this weather:")
