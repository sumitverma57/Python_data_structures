import array1
if __name__ == '__main__':
    ar=array1.ArrayStack()
    ar.push(10)
    ar.push(20)
    if ar.push("m")==False:
        print("Full")
    print(ar.ls)
