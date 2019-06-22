# What Problems should API Documention consider？

```
Author: Turing Zhu
Date: 2019-06-14 12:05:12
Description: API Document Specification

```


## Method
- GET
- POST
- PUT
- DELETE
- HEAD
- PATCH

## URI
> Please reference [restcookbook.com][restcookbook]

[restcookbook]: http://restcookbook.com/

## Parameter

| name | data type | comment | required | default |
| --- | --- | --- | --- | --- |
| | | | 

## Response

### SUCCESS
```json
```
### Failed 1
```json
```
### Failed 2
```json
```
### ...
```json
```

## Note
- all data store in "data" field.
- "error" field tell user error type(parameter,network,database...)
- "message" field tell user error Detail information.
- if request failed, "data" field should set to null.
- "code" field specifed an error. "code","error","message" defiend in error packages. divieded with common error, project common error and specific error.
- you should provide at least one success and one error example for your api documention reader.
- all fields in request parameter && uri should be lower case and '_'.

# Example

## Get Users

> GET /api/v1/users

### Paramaters
| name | data type | comment | required | default | 
| --- | --- | --- | --- | --- |
| page | int | page | no | 1 |
| page_size | int | page size | no | 20 |
| sort_by | string | sort by specified field | no | id | 

### Response

#### SUCCESS
```json
{
    "code": 0,
    "message": "success",
    "error": "success",
    "data": [],
    "page": 1,
    "page_size": 20
    "total": 100
}
```

#### ERROR: Parameter Error
```json
{
    "code": 5001,
    "message": "invalid parameter: parameter page should be an unsingned integer and littler"
    "error": "parameter error",
    "data": null,
}
```
#### ERROR: Network
```json
{
}
```
#### ERROR: Database
```json
{
}
```
#### ERROR: Logic
```json
{
}
```

### ERROR: ...
