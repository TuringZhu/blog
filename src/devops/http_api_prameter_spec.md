# HTTP API Paramaters Specification

> NOTE: generally speaking, we pass json data to server when using a post request. in json data structure, it support basic type of string, integer, float, bool and null type, and support compliex object and array type. 
> 
> How ever, it is not enough. and how check parameter when the server get the parameter
>
> [govalidator](https://github.com/asaskevich/govalidator)
>
> [go-playground/validator](https://github.com/go-playground/validator)


## Parameters' Data Type

basic data type: bool int float string nulll

| type | comment | xx |
| --- | --- | --- |
| IP
| alpha | | |
| alpha_dash | 
| alpha_space | 可以不要
| alpha_num |
| int | between |
| numeric |
| bool |
| credit_card |
| date |
| date:dd-mm-yyyy
| date-time
| date-time:user defined format |
| email |
| float |
| mac_address
| phone
| idCard |
| ip
| ip_v4
| ip_v6
| url 
| uuid | v3, v4, v5
| enum |
| not in | 
| json


## regular

- between for int 
- length range for string
- regular expression
- 