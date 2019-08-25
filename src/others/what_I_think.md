# What I think

> things that I currently Consider.

###  How to maintaince API documentation and how to keep Synchronization with code? 
> 2019-07-02 10:59:25.600106000 Tue  1562036365

```text
最好的方式是类似在之前深圳公司中，大师的做法，
所不同的是，大师的做法是规定代码中函数注释中接口文档规范，
现在是用golang gin框架或beego框架获其他框架，一般会绑定请求参数，无论PUT GET POST 等请求，都会，
那么可以这样做：定义一些基本规范，然后根据代码生成接口文档
2019-07-02 15:23:29.804891000 Tue  1562052209
```

下面是一个gin的示例

```golang
package main

import (
    "github.com/gin-gonic/gin"
)

type StructA struct {
    FieldA string `form:"field_a"`
}

type StructB struct {
    NestedStruct StructA
    FieldB string `form:"field_b"`
}

func GetDataB(c *gin.Context) {
    var b StructB
    c.Bind(&b)
    c.JSON(200, gin.H{
        "a": b.NestedStruct,
        "b": b.FieldB,
    })
}

func main() {
    r := gin.Default()
    r.GET("/getb", GetDataB)
    r.Run()
}


// curl "http://localhost:8080/getb?field_a=hello&field_b=world"

```

那么就可以根据传入参数StructB的结构与所定义的struct tag来获取 请求参数，

根据路由r.GET("/getb", GetDataB) 来获取请求方法和请求路由

`那么剩余问题: 如何解决返回数据示例，错误示例？`(2019-07-02 15:53:00.772866000 Tue  1562053980)

如果需要实现的话，考虑下GoLand里面是如何做到函数跳转的？(2019-07-02 18:40:45.997645000 Tue  1562064045)


### Why we do not consider memory size,permance and so on when we coding now?(我们现在编程为什么不再考虑性能、内存大小等问题了呢？)
> 2019-07-02 13:02:27.14529000 Tue  1562043747

```text

```

### how recurive query in mysql ?

> assume that there is a tree which all nodes stored in a table.


table:

| nodeId | parentId | other fields |
| --- | --- | --- |
| 1 |  | | 
| 2 | 1 | 
| 3 | 1 | 
| 4 | 2 |
| 5 | 2 |
| 6 | 3 | 
| 7 | 5

```
1
├── 2
│   ├── 4
|   └── 5
|       └── 7
└── 3
    └── 6
```

- how to find parent from current node?
- how to find all children from current node? 

### Question about consistency between cache and database.

第一，之前想错了，


之前认为，cache是为了提供更快速的查询而提供服务的，所以，如果cache挂掉，那么，只不过是DB层有压力而已，应用应该正常对外服务。

第二：现在纠正过来如果下：

查询：优先查询cache，不存在则查询DB，同时同步写到cache里面。

更新，删除，插入：同步更新db和cache，保证同时成功和同时失败。

所以有以下几个情况

1. 更新cache成功，更新db失败：则删除cache里面的数据，置状态为失败
2. 更新cache成功，更新db成功：置状态为成功
3. 更新cache失败，更新db失败：置状态为失败
4. 更新cache失败，更新db成功：置状态为失败，同时db中回滚或删除对应数据


新的问题：

1. 针对上述 情况1，如果删除cache失败，情况应该如何处理，这样的话，db和cache无法保持数据一致性。
2. 针对上述 情况2，如果删除或回滚db失败，情况又应该如何处理，这样的话，db和cache无法保持数据一致性。
3. 场景1


### json vs. msgpack

1. msgpack相对于json优点在哪里？目前发现是序列化后的数据比json短
2. msgpack的解释是`MessagePack is an efficient binary serialization format. It's like JSON. but fast and small.`
3. msgpack 是否适合在项目中使用？目前感觉是不适合，主要是因为以接口为主，对前端后端进行交互，json来自于javascript，所以前端解析后端传输数据上比较方便，json广泛被使用，非常成熟，msgpack还在发展中，相关技术还不成熟，
4. so msgpack存在的意义是什么？
5. 看懂[https://github.com/msgpack/msgpack/blob/master/spec.md](https://github.com/msgpack/msgpack/blob/master/spec.md)的数据格式即可，甚至是可以自己实现
6. 协议 [msgpack](https://github.com/msgpack/msgpack)
7. golang实现 [vmihailenco/msgpack](https://github.com/vmihailenco/msgpack)
