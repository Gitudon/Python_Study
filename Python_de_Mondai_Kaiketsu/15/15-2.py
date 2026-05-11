height = {"taro": 180, "hanako": 160}
print(height["hanako"])
if "hanako" in height:
    print("hanako's height available")
if 160 in height:
    print("160's height available")
height["taro"] = 170
height["jiro"] = 110
print(height["taro"])
print(height["jiro"])
