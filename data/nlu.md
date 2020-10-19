## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:pizza
- i want a pizza
- pizza
- can you take pizza order?

## intent:meal_category
- i want [vegetarian](meal_category:veg_pizza) pizza
- i want [non-vegetarian](meal_category:non_veg_pizza) pizza
- [vegetarian](meal_category:veg_pizza) 
- [non-vegetarian](meal_category:non_veg_pizza)
- [veg](meal_category:veg_pizza)
- [non-veg](meal_category:non_veg_pizza)

## intent:select_pizza
- [panner](pizza_type)
- [farmhouse](pizza_type)
- [chicken](pizza_type)
- [pepperoni](pizza_type)

## intent:size
- [regular](pizza_size)
- [medium](pizza_size)
- [large](pizza_size)

## intent:seek_confirmation
- [CONFIRM](confirm_state)
- [REBUILD](confirm_state)

## intent:customer_info
- [Amogh](customer_name)
- [Axvbv](customer_name)
- [1234567890](phone_number)
- [1278162790](phone_number)
- [9663202338](phone_number)
- [123456](pincode)
- [612379](pincode)
- [560040](pincode)
- [Koramangala](address)
- [MGRoad](address)

## intent:my_order_status
- my order status
- i want my order status
- i would like to get my order status

## intent:order_status
- [JP6D7](order_id)
- [ABC12](order_id)
- [BJ654](order_id)


## regex:pincode
- [0-9]{6}

## regex:phone_number
- [0-9]{10}

## regex:customer_name
- [A-Za-z]{5,50}

## regex:address
- [A-Za-z]{5,50}

## regex:order_status
- [A-Z0-9]{5}

## synonym:veg_pizza
- veg
- vegetarian

## synonym:non_veg_pizza
- non-veg
- non-vegetarian