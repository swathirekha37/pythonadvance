class JavaScriptObject(dict):
    def __getattribute__(self,item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)

jso=JavaScriptObject({"name":"swathi rekha","age":23,"occupation":"python developer"})
print("my name is ",jso.name)
print("my age is ",jso.age)
print("my occupation is ",jso.occupation)
# print(jso.job)  key error