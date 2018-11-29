# #练习处理json数据
import json


class JsonUtils:

    __mJson = None

    @classmethod
    def get_mJson(cls):
        return cls.__mJson

    # 将数组对象编码成JSON格式数据
    @classmethod
    def enjson_array(cls,array):
        jdata = None
        jdata = json.dumps(array,sort_keys=True,indent=4,separators=(',',':'))
        # print(cls.__mJson)
        return jdata

    @classmethod
    def enjson(cls,data):
        mdata = None
        mdata = json.loads(data)
        return mdata


arr = ["this","is","a","test",1]
a = [{'name':'jason','sex':'male','age':30}]
data = JsonUtils.enjson_array(arr)
data = JsonUtils.enjson_array(a)
print(data)

jsonData = '{"a":1,"b":32,"c":"傲血"}'
d = JsonUtils.enjson(jsonData)
print(d)
