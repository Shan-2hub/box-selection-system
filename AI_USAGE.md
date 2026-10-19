AI Usage Disclosure

1. AI Tools Used

Tool: ChatGPT (OpenAI)

Purpose: Used to understand the assignment requirements, compare possible solution approaches, plan the Django REST API architecture, assist with implementation and debugging, and review testing and documentation.

Other tools: No other AI tools are listed unless they were actually used during development.

2. Prompts Used

The following are examples of prompts and requests made during the project. Some descriptions are summaries rather than exact quotations.

Asked ChatGPT to explore possible solutions before choosing an approach for the box-selection assignment.

Asked ChatGPT to finalize the design using a 3D packing heuristic supporting multiple products, with a Django REST API and admin panel.

Requested step-by-step assistance with implementation, project files, tests, and documentation.

Asked for help investigating the serializer validation warning:

UserWarning: min_value should be an integer or Decimal instance.

Requested assistance understanding test cases, reviewing test results, and preparing the required submission documentation.

These examples describe the main areas of assistance used during development. The original conversation transcript is included separately in the submission.

3. AI Outputs Accepted or Adapted

I used AI assistance to explore implementation options, plan the project structure, troubleshoot issues, and improve testing and documentation.

The resulting application uses Django REST Framework for the API, Django ORM models for storing products and boxes, SQLite as the database, Django admin for managing records, and a separate packing module for the recommendation logic.

The packing module uses a deterministic 3D corner-point heuristic to evaluate box suitability and provide product placement information. The recommendation considers product dimensions, box dimensions, weight capacity, and box cost.

I reviewed and tested the implementation rather than relying solely on AI-generated explanations or suggestions.

4. Outputs Rejected or Modified

I reviewed the AI-assisted implementation and made changes where necessary. The following are examples of modifications and verification activities performed during development.

Serializer validation: I investigated a warning concerning the min_value argument and updated the relevant validation values to use explicit Decimal values.

Input validation: I tested requests containing a zero quantity and an unknown product ID to check that invalid inputs were rejected with appropriate validation errors.

Box recommendation: I tested orders for which the available boxes could not accommodate the product dimensions or weight, and checked how the API reported that no suitable box was found.

The input-validation and box-recommendation examples above describe testing activities, not necessarily rejected AI suggestions. I have not classified a suggestion as rejected unless I actually rejected or changed it.

5. Mistakes and Limitations Identified

The recommendation method uses a heuristic rather than an exhaustive search of all possible packing arrangements. Therefore, it does not guarantee that the selected arrangement is globally optimal.

I also tested invalid inputs and orders that exceeded available box dimensions or weight limits to examine how the application handled these scenarios.

Any additional AI-generated mistakes identified during review should be documented here only if they were actually observed. I have not assumed that a potential limitation or test scenario was an AI mistake without evidence.

6. Verification of the Final Code

I used Django's system check, automated tests, and manual API requests to verify the implementation.

Commands executed:

python manage.py check

python manage.py test

The recorded test run reported 11 automated tests, all passing. The Django system check also reported no issues.

Manual API test scenarios:

1. Submitted a valid order containing multiple products.
2. Submitted a request with a quantity of zero.
3. Submitted a request containing an unknown product ID.
4. Tested a product whose dimensions exceeded the available boxes.
5. Tested an order whose weight exceeded the available boxes' weight limits.

I reviewed the API responses to check validation behaviour and whether the recommendation endpoint correctly handled orders for which no suitable box was available.

These checks provide evidence for the scenarios tested; they do not establish that every possible input or packing arrangement has been verified.

7. Human Review and Responsibility

I used ChatGPT as an assistance tool during development. I reviewed the implementation, ran tests, investigated validation issues, and examined the limitations of the recommendation approach.

I am responsible for understanding the submitted code and being able to explain the design decisions, validation rules, testing approach, and limitations of the system.
