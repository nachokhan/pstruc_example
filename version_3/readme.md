
# Adding new behaviour

## User's Request

### Prompt
Considering the following project structure,  I would need some way of showing the pet's info when the person's info is being shown

```
[Content of structure file goes here]
```

## ChatGPT's Response

To display the pet's information alongside the person's information, you need to establish a link between the Person and Pet objects in your code. Here's a step-by-step guide to modify your existing code to achieve this:

1. Set the Pet for Each Person: In your main.py, after creating Person and Pet objects, use the set_pet method in the Person class to associate each person with their pet.

2. Modify the print_person_data Method: Ensure that the print_person_data method in the Person class prints the pet's information if the person has a pet.

3. Invoke print_person_data for Each Person: In your main.py, call the print_person_data method for each person to display their information along with their pet's information.

Here is how your modified main.py and person.py should look:

### Adjustments in `main.py`

![main.py Changes](/version_3/changes_main.png)

*Note: This image contains the modifications made to the `main.py` file.*

### Adjustments in `person.py` (moduleA)

![main.py Changes](/version_3/changes_person.png)

*Note: This image contains the modifications made to the `person.py` file in moduleA.*


With these modifications, when you run main.py, it will display information about both the person and their associated pet, if any.
