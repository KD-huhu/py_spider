'''
python操作mongo
模块：pymongo
'''
import pymongo
# 1、创建连接
client = pymongo.MongoClient()
# 用这个client连接数据库
db = client['shop']
# 使用这个db选择一个集合取做CRUD

# 插入
# people = {'name':'aaa','age':10}
# result = db['goods'].insert(people)
# print(result)
# 5ead2dc81cc58c8557950329
# 返回这条数据的_id

# 查找
# result = db['goods'].find({'name':'aaa'})
# print(result)
# <pymongo.cursor.Cursor object at 0x0000022635320408>
# 查询操作返回的都是一个游标对象。
# 游标对象是可以遍历的，遍历出来的数据就是文档所对应的字典。

# for i in result:
#     print(i)
    # {'_id': ObjectId('5ead2dc81cc58c8557950329'), 'name': 'aaa', 'age': 10}

# 查询每个栏目下 价格大于50元的商品个数 #并筛选出"满足条件的商品个数" 大于等于3的栏目
# 聚合操作
result = db['goods'].aggregate([{'$match':{'shop_price':{'$gt':50}}},
                                {'$group':{'_id':'cat_id','t':{'$sum':1}}},
                                {'$match':{'t':{'$gt':3}}}])
print(result)
# <pymongo.command_cursor.CommandCursor object at 0x0000027265E09808>
for i in result:
    print(i)
    # {'_id': 'cat_id', 't': 25}