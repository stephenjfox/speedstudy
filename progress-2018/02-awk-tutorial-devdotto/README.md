## Learn the basics of the Awk programming language with [this dev.to tutorial](https://dev.to/rrampage/awk---a-useful-little-language-2fhf)

### Key take-aways

1. Most people just use `awk` to get at something with columnar output

    + `ls -l | awk '{print $10}'`

2. Awk __wants__ to parse your input, but it will hang strangely:

    + `awk 'BEGIN{ print "Hello, World!" }'` works just fine
    - `awk 'BEGINI{ print "Hello, World!" }'` doesn't report an error, but goes
      unresponsive and non-terminating.


> To be continued