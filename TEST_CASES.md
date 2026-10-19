# Automated Test Cases

Automated tests are in `inventory/tests.py`.

| ID | Scenario | Expected behavior |

| TC-01 | Single product fits the cheapest box | Recommend the cheapest qualifying box |
| TC-02 | Product requires axis-aligned rotation | Packing succeeds if the rotated dimensions fit |
| TC-03 | Product is too large for candidate box | Candidate is rejected |
| TC-04 | Order exceeds a box's weight limit | Box is rejected and a later candidate may be selected |
| TC-05 | Multiple items fit without overlap | Return a placement for every item |
| TC-06 | No available box can fit item | Return `found: false` |
| TC-07 | Empty order | Return HTTP 400 |
| TC-08 | Unknown product ID | Return HTTP 400 |
| TC-09 | Duplicate product entries | Return HTTP 400 and request one entry with quantity |
| TC-10 | Quantity is zero | Return HTTP 400 |
| TC-11 | Product and box list endpoints | Return HTTP 200 |

Run with `python manage.py test`. Add additional tests after you manually review edge cases.


# Manual API Test Cases

1. Valid Order

- Input: One smartphone and two headphones.
- Expected: Recommend the lowest-cost box the packing heuristic can fit all items into.
- Actual: Medium Box recommended at ₹50.
- Status: Passed.

2. Zero Quantity

- Input: Product ID 1 with quantity 0.
- Expected: HTTP 400 validation error.
- Actual: HTTP 400; quantity must be at least 1.
- Status: Passed.

3. Unknown Product ID

- Input: Product ID 15, which does not exist.
- Expected: HTTP 400 validation error.
- Actual: HTTP 400; unknown product ID reported.
- Status: Passed.

4. Oversized Product

- Input: Oversized Monitor (100 × 80 × 60 cm).
- Expected: No box recommendation if the packing heuristic cannot fit the product.
- Actual: HTTP 200; `found: false`.
- Status: Passed, with heuristic limitation noted.

5. Order Exceeds Weight Capacity

- Input: Heavy Test Item weighing 26 kg.
- Expected: No box recommendation because every box has a maximum weight below 26 kg.
- Actual: HTTP 200; `found: false`. All five boxes were rejected for exceeding weight capacity.
- Status: Passed.
