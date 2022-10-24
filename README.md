# DSA-Python ( Credits [CodeBasics](https://youtu.be/gDqQf4Ekr2A))
Data Structure and Algorithm practice questions and exercises from CodeBasics.

# Data Structures and Algorithms from Codebasics Channel

## Arrays
![image](https://user-images.githubusercontent.com/62849614/197442798-2e9db89c-b6cf-4ca7-bab9-d9dc7099847d.png)

2. Array elements are saved at a particular index inside the it.
	
	a. These indexes are nothing but specific places in memory represented by addresses as shown. Each box is of 4 bytes or 32 bit .
	
	b. Where 4 bytes is capacity of integer in many programming languages.
	
	![image](https://user-images.githubusercontent.com/62849614/197442885-ecd419d5-6cdf-4228-8513-cbf65feb9926.png)
	
	d. So in reality 298 a number is stored in this manner as shown.
		
### Scenario No 1
![image](https://user-images.githubusercontent.com/62849614/197442893-1ddadbb8-f2cc-4740-bd6e-14ff19dd8811.png)

a. If 298 is our first value at index zero ( 0 ) then to get the value 320, we add the index value 2 after its product with sizeOf(Integer) which is 4 bytes .
	
b. And finally getting the address.

### Scenario 2

![image](https://user-images.githubusercontent.com/62849614/197442913-1c93a359-c542-40f7-aab2-024f020dff6b.png)

a. The time complexity in this case is very simple as we can see here, because if we are finding we will take n no iterations to get to that value thus O(n) is time complexity.

### Scenario 3

![image](https://user-images.githubusercontent.com/62849614/197442934-53c63857-fd8c-403a-b15b-05f773ad4a40.png)

a. Again we have to take n iterations 

### Scenario 4 

![image](https://user-images.githubusercontent.com/62849614/197442951-b5a6fd25-670e-4462-a0c7-dd554aec8d44.png)
	
a. We are giving index value and value itself. The time complexity is when it has to swap values by one step for each thus take n steps for swapping values.

### Scenario 5
![image](https://user-images.githubusercontent.com/62849614/197442962-9801aa54-39b2-4427-9ce3-130edea136c5.png)

a. Similar case as above example.

### Static vs Dynamic Arrays

![image](https://user-images.githubusercontent.com/62849614/197443003-0a243adf-33d9-43af-a9a3-70f6621b84c1.png)

![image](https://user-images.githubusercontent.com/62849614/197443037-0899c772-1b4a-466c-9f6c-8747057602d2.png)

a. In case of static array, we may get error if put value at index greater than the array's size.

b. While in dynamic arrays no such thing happens.

![image](https://user-images.githubusercontent.com/62849614/197443050-f20be927-d0a4-4e42-b636-09edfb3d4af4.png)

a. In dynamic arrays some memory is pre-allocated in continuous memory with specific amount.
	
b. Dark gray are boxes already allotted.

c. After we have inserted 10 elements what now ? And wanna put 11th element 

![image](https://user-images.githubusercontent.com/62849614/197443068-6b5ab6d3-dd3c-4273-a0d3-c1e1fdd73fb2.png)

d. Our program assign new memory space ( 10 + 10 * 2 for instance ) at some new place and move previous values and does this every time allocated memory runs out which is overhead obviously.

### Python Dynamic Behaviour

![image](https://user-images.githubusercontent.com/62849614/197443127-68d79129-a773-4eae-9f5e-c4de199b2257.png)
	
Python infers data type on runtime and thus we can put any kind of data in it as shown here.

![image](https://user-images.githubusercontent.com/62849614/197443131-707d9d22-5396-451c-aae1-c0b1a8036338.png)	
	
Can also have a multi-dimensional array.
