# SHA-256

## Algorithm's steps

### Step 1 - preliminary work

* Convert the input string to binary
* Add 1
* Padding the code with zeros until the data is 512 bits, minus 64 bits (resulting in 448 bits)
* Add 64 bits to the end as a big-endian integer representing the length of the input message in binary

Now we have an input that will be divisible by 512 without a remainder.

### Step 2 - Initialize the hash values (h)

* We are now generating 8 hash values
* These are hard-coded constants that represent the first 32 bits of the fractional parts of the square roots of the first eight primes: 2, 3, 5, 7, 11, 13, 17, 19

### Step 3 - Initializing the rounded constants (k)

* As in the previous step, we will create a few more constants
* This time there will be 64
* Each value (0-63) represents the first 32 bits of the fractional parts of the cube roots of the first 64 primes (2-311)

### Step 4 - Loop Fragments

### Step 5 - Create a Message Schedule (w = message_schedule)

* Copy the input from step 1 into a new array where each entry is a 32-bit word
* Add 48 more words, initialized to zero, so that we get an array w [0 ... 63]
* Change the zeroed out indices at the end of the array using the following algorithm:<br>

For i from w [16 ... 63]:

s0 = (w [i-15] rightrotate 7) xor (w [i-15] rightrotate 18) xor (w [i-15] rightshift 3)<br>
s1 = (w [i- 2] rightrotate 17) xor (w [i- 2] rightrotate 19) xor (w [i- 2] rightshift 10)<br>
w [i] = w [i-16] + s0 + w [i-7] + s1

### Step 6 - Compression

* Initialize the variables a, b, c, d, e, f, g, h and set them equal to the current values of the hash function, 
respectively, h0, h1, h2, h3, h4, h5, h6, h7

* A compression cycle that will change the values of a-h. It looks like this:

For i from 0 to 63: <br>
S1 = (e rightrotate 6) xor (e rightrotate 11) xor (e rightrotate 25)<br>
ch = (e and f) xor ((not e) and g)<br>
temp1 = h + S1 + ch + k [i] + w [i]<br>
S0 = (a rightrotate 2) xor (a rightrotate 13) xor (a rightrotate 22)<br>
maj = (a and b) xor (a and c) xor (b and c)<br>
temp2: = S0 + maj<br>
h = g<br>
g = f<br>
e = d + temp1<br>
d = c<br>
c = b<br>
b = a<br>
a = temp1 + temp2<br>

* Addition is calculated by mod 2 ^ 32
* All calculations 64 times, changing variables a-h

### Step 7 - Change the final values

After the compression cycle, during the chunk cycle, we change the hash values by adding the corresponding a-h variables to them.<br>
As before, all addition is done modulo 2 ^ 32

### Step 8 - Final Hash

Finally, we put everything together