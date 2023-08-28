class Phone:
    def __delattr__(self, attr):
        del self.__dict__[attr]
        print(f"'{str(attr)}' was deleted")


phone = Phone()
phone.color = 'black'
print(phone.color)
del phone.color  # 'color' was deleted
print(phone.color)