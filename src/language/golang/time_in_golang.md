# time struct in golang

> [type Time struct {](https://github.com/golang/go/blob/1a7c15fa6d5ce2d78d0f9f5050ee9dd1e29485df/src/time/time.go#L127)

```golang
type Time struct {
	// wall and ext encode the wall time seconds, wall time nanoseconds,
	// and optional monotonic clock reading in nanoseconds.
	//
	// From high to low bit position, wall encodes a 1-bit flag (hasMonotonic),
	// a 33-bit seconds field, and a 30-bit wall time nanoseconds field.
	// The nanoseconds field is in the range [0, 999999999].
	// If the hasMonotonic bit is 0, then the 33-bit field must be zero
	// and the full signed 64-bit wall seconds since Jan 1 year 1 is stored in ext.
	// If the hasMonotonic bit is 1, then the 33-bit field holds a 33-bit
	// unsigned wall seconds since Jan 1 year 1885, and ext holds a
	// signed 64-bit monotonic clock reading, nanoseconds since process start.
	wall uint64
	ext  int64

	// loc specifies the Location that should be used to
	// determine the minute, hour, month, day, and year
	// that correspond to this Time.
	// The nil location means UTC.
	// All UTC times are represented with loc==nil, never loc==&utcLoc.
	loc *Location
}
```

## example
time: 2019-08-25 08:15:30.547833 +0000 UTC

```
wall: 547833000
0000 0000 0000 0000 0000 0000 0000 0000 0010 0000 1010 0111 0100 0100 1010 1000
01-bit flag(hasMonotonic): 0
33-bit seconds field:  0 0000 0000 0000 0000 0000 0000 0000 0000
30-bit wall time nanoseconds field(0-999999999): 10 0000 1010 0111 0100 0100 1010 1000

ext: 63702317730
0000 0000 0000 0000 0000 0000 0000 1110 1101 0100 1111 0100 0011 1010 1010 0010

# 1 flag=0
wall
01-bit: 0
33-bit: 0
30-bit: wall time nanoseconds

ext: seconds since 0001-01 00:00:00.000000


# 2 flag=1
wall
01-bit: 1
33-bit: seconds since 1985-01-01 00:00:00.0000

ext: ?? a signed 64-bit monotonic clock reading, nanoseconds since process start
```


golang 为什么要这样处理时间? python调用的好像是c语言的
