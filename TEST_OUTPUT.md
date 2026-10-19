# Test Run Output

## Environment

- OS: Windows 11
- Python version: Python 3.11.6
- Django version: 5.2.18

## Automated Test Results

Command: `python manage.py test`

(.venv) C:\Users\Shan\Downloads\box_selection_system_starter\box_selection_system>python manage.py test
Found 11 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...........
----------------------------------------------------------------------
Ran 11 tests in 0.042s

OK
Destroying test database for alias 'default'...

## Django System Check

Command: `python manage.py check`

(.venv) C:\Users\Shan\Downloads\box_selection_system_starter\box_selection_system>python manage.py check
System check identified no issues (0 silenced).

## Manual API Test Results

`Summarization` : In below are the test cases, that has been tested by giving the correct valid order values,  quantity as 0, unknown pr0duct id that is not mentioned or added in the product (product_id = 15), product that is too large for every box to carry by, the order exceeds every boxes weight limits here by these are the test cases conducted on this project.

# Actual terminal output:

1. Valid Order

HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept


    "found": true,
    "box": {
        "id": 2,
        "name": "Medium Box",
        "cost_inr": "50.00",
        "max_weight_kg": "5.000"
    },
    "total_order_weight_kg": "1.200",
    "packing_method": "3d_corner_point_heuristic",
    "placements": [
        {
            "item_key": "3-1",
            "position_cm": {
                "x": 0.0,
                "y": 0.0,
                "z": 0.0
            },
            "oriented_dimensions_cm": {
                "length": 8.0,
                "width": 18.0,
                "height": 20.0
            }
        },
        {
            "item_key": "3-2",
            "position_cm": {
                "x": 8.0,
                "y": 0.0,
                "z": 0.0
            },
            "oriented_dimensions_cm": {
                "length": 8.0,
                "width": 18.0,
                "height": 20.0
            }
        },
        {
            "item_key": "1-1",
            "position_cm": {
                "x": 16.0,
                "y": 0.0,
                "z": 0.0
            },
            "oriented_dimensions_cm": {
                "length": 2.0,
                "width": 8.0,
                "height": 15.0
            }
        }
    ],
    "note": "Lowest-cost box accepted by the packing heuristic; not a proof of globally optimal packing."

2. QUANTITY = 0

HTTP 400 Bad Request
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "error": "Invalid request",
    "details": {
        "items": [
            {
                "quantity": [
                    "Ensure this value is greater than or equal to 1."
                ]
            }
        ]
    }
}

3. UNKNOWN PRODUCT ID = 15

HTTP 400 Bad Request
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "error": "Invalid request",
    "details": {
        "items": [
            "Unknown product_id value(s): [15]"
        ]
    }
}

4. PRODUCT TOO LARGE FOR EVERY BOX - OVERSIZED MONITOR 

HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "found": false,
    "message": "No available box passed the weight check and packing heuristic.",
    "total_order_weight_kg": "3.000",
    "rejected_boxes": [
        {
            "box": "Small Box",
            "reason": "order_exceeds_weight_capacity"
        },
        {
            "box": "Medium Box",
            "reason": "heuristic_could_not_pack_all_items"
        },
        {
            "box": "Large Box",
            "reason": "heuristic_could_not_pack_all_items"
        },
        {
            "box": "Heavy Duty Box",
            "reason": "heuristic_could_not_pack_all_items"
        },
        {
            "box": "Extra Large Box",
            "reason": "heuristic_could_not_pack_all_items"
        }
    ],
    "packing_method": "3d_corner_point_heuristic",
    "limitation": "A heuristic failure does not prove that no feasible physical arrangement exists.
}

5. Additional validation check - QUANTITY - 101

HTTP 400 Bad Request
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "error": "Invalid request",
    "details": {
        "items": [
            {
                "quantity": [
                    "Ensure this value is less than or equal to 100."
                ]
            }
        ]
    }
}

# Weight - limit test 

HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept


    "found": false,
    "message": "No available box passed the weight check and packing heuristic.",
    "total_order_weight_kg": "26.000",
    "rejected_boxes": [
        {
            "box": "Small Box",
            "reason": "order_exceeds_weight_capacity"
        },
        {
            "box": "Medium Box",
            "reason": "order_exceeds_weight_capacity"
        },
        {
            "box": "Large Box",
            "reason": "order_exceeds_weight_capacity"
        },
        {
            "box": "Heavy Duty Box",
            "reason": "order_exceeds_weight_capacity"
        },
        {
            "box": "Extra Large Box",
            "reason": "order_exceeds_weight_capacity"
        }
    ],
    "packing_method": "3d_corner_point_heuristic",
    "limitation": "A heuristic failure does not prove that no feasible physical arrangement exists."

