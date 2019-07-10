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