#both init  and new are same. But difference lies in utilising them.
#when you are customizing the mutables use init.
#when working with immutables use new.

#new is used only when working with class.
class ReverseStr(str):

    def __new__(*args,**kwargs):
        self = str.__new__(*args,**kwargs)
        self = self[::-1]
        return self

rev=ReverseStr('swathirekha')
print(rev)