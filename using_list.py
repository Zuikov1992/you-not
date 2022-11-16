def function_delete():
    delete = True
    while delete:
        element = input("возможно хотите что-то удалить? ")
        if element != "нет":
            mylist.remove(element)
        else:
            delete = False


def function_out_buy():
    print("я должен купить", len(mylist), "покупок(ки)")
    for it in mylist:
        print(it, end=" ")


mylist = ["молоко", "яйца", "хлеб"]
addlist = True
while addlist:
    y = input("введите наименование товара или 'нет' если не хотите нечего добавить ")
    if y != "нет":
        mylist.append(y)
    else:
        addlist = False

see = input("просмотреть список? да/нет? ")
if see == "да":
    print(mylist)
    function_delete()
else:
    function_delete()

n = input("Отсортировать список? да нет? ")
if n == "да":
    mylist.sort()
    print(mylist)

out = input("Как вывести покупки? список/текст? ")
if out == "текст":
    function_out_buy()
elif out == "текстом":
    function_out_buy()
else:
    print("я должен купить", len(mylist), "покупок(ки)")
    for item in mylist:
        print(item)
