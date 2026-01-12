## リストの中の要素は自転車のブランド名
bicycles = ['trek', 'cannnondale', 'redlne', 'specialized']

##リストの中の1番最初の文字を取ってくる→trek
# print(bicycles[0])

##titleメソッドを付けたら文字列と判断して先頭を大文字にしてくれる
# print(bicycles[0].title())

## -1にすると1番後ろの要素を取ってくる
# print(bicycles[-1])

# message = f"My first bicycle was a {bicycles[0].title()}."
# print(message)

##リストに追加するときは、　append 
# bicycles.append('aaa')
# print(bicycles)

##追加する位置を指定して追加するときは、　insert 
# bicycles.insert(0, 'aaa')
# print(bicycles)

##削除するときは、 del
# del bicycles[0]
# print(bicycles)

##リストの最後の要素を取り出してリストから削除するときは、 pop()
popped_bicycle = bicycles.pop()
print(popped_bicycle)

## popのあとに取り出す要素の位置を指定することもできる　pop(0)

