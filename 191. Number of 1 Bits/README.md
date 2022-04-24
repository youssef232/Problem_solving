## 191. Number of 1 Bits
you get input in binary shape. target to calculate the NO. of 1 .

Bit manipulation.

solution idea:

    loop untile the number is 0
    then using AND logic (&) between n and least significatn bit
    if it 1, NO. ones will be increased. otherwise, it stays the same.
    then updating n with one shift right(>>).