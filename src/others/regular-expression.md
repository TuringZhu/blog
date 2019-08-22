# Regular Expression

## Metacharacters

| Character | Description | Example |
| --- | --- | --- |
| [] | A set of characters | "[abcd]", "[a-zA-Z0-9]" |
| \	| Signals a special sequence(Can also be used to escape special characters)	| "\d" |
| .	| Any character(except newline character) | "he..o" |
| ^	| starts with | "^hello" |
| $	| ends with	| "world$" |
| *	| zero or more occurrences | "aix\*" |
| +	| one or more occurrences  | "aix+" |
| {} | Exactly the specified number of occurrences | "al{2}" |
| \| | Either or | "falls |
| () | capture and group |	

## Special sequences
| Character | Description | Example |
| --- | --- | --- |
| \A | |
| \b | |
| \B | |
| \d | 单个数字, 等同于[0-9] |
| \D | 单个非数字 |
| \s | 单个空白字符 |
| \S | 单个非空白字符 |
| \w | 一个单词, 等同于 [0-9a-zA-Z\_]+ |
| \W | 与\w 相反功能 |
| \Z |

