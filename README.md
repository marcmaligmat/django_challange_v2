### Required Libraries/Modules are in requirements.txt
### Models Created [Customer, Account, Transfer]
### Answers of Given Tasks
  - Create a new bank account for a customer, with an initial deposit amount. 
    ANSWER: endpoint:'/api/customers/' METHOD:POST
            The initial deposit amount is on another model (account), which is
            auto created via signals.

  - A single customer may have multiple bank accounts.
    ANSWER endpoint: '/api/accounts/' METHOD:POST


  - Transfer amounts between any two accounts, including those owned by
    different customers.
    ANSWER endpoint: '/api/transfers/' METHOD:POST

  - Retrieve balances for a given account.
    ANSWER endpoint: '/api/accounts/<int:pk> METHOD:GET

  - Retrieve transfer history for a given account.
    ANSWER endpoint: '/api/accounts/<int:pk>/transfers METHOD:GET

  - Write tests for your business logic
    ANSWER run "python manage.py test"
        Included testing for customer creation and signals for account creation

  - Documentation: is the API well-documented?
    ANSWER added Swagger OpenAPI for pretty documentation.
    endpoint '/'


### Objective

Your assignment is to build an internal API for a fake financial institution using Python and Django.

### Brief

While modern banks have evolved to serve a plethora of functions, at their core, banks must provide certain basic features. Today, your task is to build the basic HTTP API for one of those banks! Imagine you are designing a backend API for bank employees. It could ultimately be consumed by multiple frontends (web, iOS, Android etc).

### Tasks
- Implement assignment using:
  - Language: **Python**
  - Framework: **Django**
- There should be API routes that allow them to:
  - Create a new bank account for a customer, with an initial deposit amount. A
    single customer may have multiple bank accounts.
  - Transfer amounts between any two accounts, including those owned by
    different customers.
  - Retrieve balances for a given account.
  - Retrieve transfer history for a given account.
- Write tests for your business logic

Feel free to pre-populate your customers with the following:

```json
[
  {
    "id": 1,
    "name": "Arisha Barron"
  },
  {
    "id": 2,
    "name": "Branden Gibson"
  },
  {
    "id": 3,
    "name": "Rhonda Church"
  },
  {
    "id": 4,
    "name": "Georgina Hazel"
  }
]
```

You are expected to design any other required models and routes for your API.

### Evaluation Criteria

- **Python** best practices
- Completeness: did you complete the features?
- Correctness: does the functionality act in sensible, thought-out ways?
- Maintainability: is it written in a clean, maintainable way?
- Testing: is the system adequately tested?
- Documentation: is the API well-documented?

### CodeSubmit

Please organize, design, test and document your code as if it were going into production - then push your changes to the master branch. After you have pushed your code, you may submit the assignment on the assignment page.

All the best and happy coding,

The Snake Charmer Limited Team


