class ThisIsACustomException(Exception):
    pass


a = 'bgfhddgfhdghdfghd' + 'sgsfdgsdfg' + 'bgfhddgfhdghdfghd' + 'sgsfdgsdfg' + 'bgfhddgfhdghdfghd' + 'sgsfdgsdfg' + 'bgfhddgfhdghdfghd' + 'sgsfdgsdfg'
sample_dict = {"a": 1}

print(sample_dict["a"])

a = 1
b = 0

c = None

try:
    # if b == 0:
    #     raise ThisIsACustomException

    c = a / b

    # print(1/0)
    # print(sample_dict["b"])
except KeyError:
    print("we've encountered a key error")
    c = a / 1
except ZeroDivisionError:
    print("we've encountered a zero division error")
    c = a / 1
except ThisIsACustomException:
    print("we've encountered a custom exception error")
except Exception as e:
    print("oh no", str(e))
finally:
    print("we've encountered a finally block")

print("c: ", c)
print("we've made it to the end")
