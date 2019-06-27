# Code Clean & Code Style

## Naming

1. 名副其实，如果有更好的名称，则替换掉旧的
2. 避免与系统变量重名或其他常用名字中
3. 使用能读的出来的名字
4. 不要使用前缀
5. 明确是王道，专业程序眼善用其能，编写其他人能理解的代码
6. 类名、对象名应该是名词或名词短语
7. 方法名和函数名应该是动词或动词短语
8. 言道意到，意到言道
9. add insert append的区别，另外create
10. 只要短名称足够精确，就不要使用长名称
11. 驼峰式命名 & 蛇形命名

### Specipitation

| item | specipitation | comment | 
| --- | --- | --- |
| file  | snake | 
| database | snake |
| table | snake |
| field |snake | json and table in database |
| constant | all uppercase with '_' |
| variable | hump in go, snake in python | lower first letter, hump or snake |
| class | hump | upper first letter |
| method & function | hump in go, snake in python | lower first letter |
| instance | hump in go, snake in python | lower first letter, humpp or snake |


## Function

- 函数尽量短小
- if else while for 等语句缩进上不多于1层或2层
- 整体缩进能短则短
- 函数应该只做一件事，做好一件事，只做这一件事，判断是否只做一件事的标准是：看是否还能拆分出一个函数来
- 单一权责原则 Single Resonsibility Principle
- 开放闭合原则：Open Closed Priciple
- 函数参数：优先零参数，其次单一参数，其次双参数，尽量避免三个及三个以上的参数
- 参数多了的问题：1从函数名推断功能，从返回值和返回类型理解函数输出，从参数列表依次看参数名，参数类型，并理解其作用和怎么用
- 有些参数2-3个参数刚刚好，比如笛卡儿点，坐标点等
- 如果出现三个或三个以上的参数，请考虑封装成结构体
- 单一参数函数：建议形成 v+n 的形式
- 错误码集中问题：其他地方都得导入和使用它，当ERROR枚举修改时，所有其他类都必须重新编译和部署，这对ERROR类造成一定压力，导致程序员不愿意增加新的错误码而继续使用旧的错误码而导致无法区分错误，建议错误名+错误消息形式，错误码是否有必要？
- 消灭重复性的代码


## Comment

The best comment is no comment.

## Class Format

> the order of class member in a class defination


- public static constant
- private static constant
- private instance variable
- pulic method
- private method called by public method(followed by corresponding public method)
