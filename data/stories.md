## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
 
## meal_category happy path
* greet
   - utter_greet
* pizza
   - utter_meal_category
* meal_category
   - action_meal_category
* select_pizza
   - utter_pizza_size
* size
   - utter_current_order
   - utter_confirmation_message
* seek_confirmation{"confirm_state":"CONFIRM"}
   - customer_details_form
   - form{"name": "customer_details_form"}
   - form{"name":null}
   - utter_confirmation_message
* seek_confirmation{"confirm_state":"CONFIRM"}
   - action_place_order


## order status happy path
* greet
  - utter_greet
* my_order_status
  - utter_order_status
* order_status
  - action_order_status
* goodbye
  - utter_goodbye