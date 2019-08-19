```
Usage: shasum [OPTION]... [FILE]...
  -a, --algorithm   1 (default), 224, 256, 384, 512, 512224, 512256
  -b, --binary      read in binary mode
  -c, --check       read SHA sums from the FILEs and check them
  -t, --text        read in text mode (default)
  -p, --portable    read in portable mode
                        produces same digest on Windows/Unix/Mac
  -0, --01          read in BITS mode
                        ASCII '0' interpreted as 0-bit,
                        ASCII '1' interpreted as 1-bit,
                        all other characters ignored

The following two options are useful only when verifying checksums:
  -s, --status      don't output anything, status code shows success
  -w, --warn        warn about improperly formatted checksum lines

  -h, --help        display this help and exit
  -v, --version     output version information and exit

When verifying SHA-512/224 or SHA-512/256 checksums, indicate the
algorithm explicitly using the -a option, e.g.

  shasum -a 512224 -c checksumfile

The sums are computed as described in FIPS-180-4.  When checking, the
input should be a former output of this program.  The default mode is to
print a line with checksum, a character indicating type (`*' for binary,
` ' for text, `?' for portable, `^' for BITS), and name for each FILE.

```
