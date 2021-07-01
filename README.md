**Sejal Kargal**
**SAP Next Talent - Rotational Program Task**

This is a basic Flask web application with a `Dockerfile` and `docker-compose` included.

**Running instructions**
In the project directory (`SAPTaskApp`) run
    `docker-compose up`

**Features:**
- 1. `/<int:number>` will display integers from 1 to that number
- 2. `/<int:number>/odd` will display only odd numbers in that range
- 3. `/<int:number>/even` will display only even numbers in that range
- 4. `/<int:number>/prime` will display only prime numbers in that range
- 5. Run `python3 app.test.py` to run basic unit test suite

**Decisions**
I decided to use list comprehensions to implement the functions inside of `app.py` for features 1-4 because not only is it a nice syntactic sugar I enjoy, but Python will allocate the list’s memory first, before adding the elements to it, instead of having to resize on runtime. It’ll also avoid having to make calls to ‘append’, which may be cheap but add up. Lastly, code using comprehensions is considered more ‘Pythonic’ — better fitting Python’s style guidelines.

I used `map()` because it is a built-in function that allows you to process and transform all the items in an iterable without using an explicit for loop. `map()` is useful when you need to apply a transformation function to each item in an iterable and transform them into a new iterable. `map()` is one of the tools that support a functional programming style in Python and it was useful for typecasting the integers to strings.

I used `join()` because it takes an iterable as an argument and returns a string which is a concatenation of all the string objects in the iterable. It is a more efficient way to concatenate strings rather than using a “+”. The time complexity of using `join()` for strings is O(n) where n is the length of the string to be concatenated. However, this is significant when considering larger strings so a drawback may be entering a very large number in the app (as `int:number` approaches infinity, performance declines).

**Experience**
I am grateful for this opportunity and had a lot of fun quickly putting this Flask app together prior to the interview! This was a fun activity I did during my break. Looking forward to learning more about the SAP Next Talent program and speaking with you! Thank you.