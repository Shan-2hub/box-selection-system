# AI-Assisted Box Selection System

A Django REST API that recommends the lowest-cost shipping box accepted by a deterministic 3D corner-point packing heuristic. Products and shipping boxes are stored in SQLite and managed through Django admin.

## Features

- Product and shipping-box inventory models
- Django admin for managing inventory
- JSON endpoints to list products and boxes
- Recommendation endpoint supporting multiple products and quantities
- Axis-aligned rotations and overlap/bounds checks
- Maximum total order-weight check
- Lowest-cost feasible box selection with deterministic tie-breaking
- Automated unit and API tests

## Technology

- Python 3.11+ recommended
- Django 5.2
- Django REST Framework
- SQLite

## Setup

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/admin/` and add Products and Shipping boxes. For local development only, the API has no authentication; do not expose this configuration publicly.

## API

### List products

`GET /api/products/`

### List shipping boxes

`GET /api/boxes/`

### Recommend a box

`POST /api/recommend/`

Example request (replace `product_id` with an ID from `/api/products/`):

```json
{
  "items": [
    {"product_id": 1, "quantity": 2},
    {"product_id": 2, "quantity": 1}
  ]
}
```

A successful recommendation returns `found: true`, the chosen box, total weight, item placements, and the packing method. If no candidate is accepted, the response returns `found: false` and rejection reasons. Invalid requests return HTTP 400.

### Example using curl

```bash
curl -X POST http://127.0.0.1:8000/api/recommend/ \
  -H "Content-Type: application/json" \
  -d '{"items":[{"product_id":1,"quantity":1}]}'
```

## Algorithm

1. Expand requested quantities into individual item instances.
2. Sort items by descending volume.
3. For each box in ascending cost order, reject it if the order weight exceeds capacity.
4. Try unique axis-aligned rotations at corner points generated from the origin and the positive faces of placed items.
5. Ensure each placement remains within the box and does not overlap prior placements.
6. Return the first box for which the heuristic places every item.

The tie-breaker for equal costs is the box database ID. The algorithm is deterministic for a given input and inventory.

## Limitations and assumptions

- This is a heuristic, not a complete 3D bin-packing solver. A failed attempt does not prove that no valid arrangement exists.
- It handles rectangular cuboid items and boxes, with axis-aligned rotations only.
- It does not model fragile items, packaging material, orientation restrictions, dimensional tolerances, or packing safety margins.
- Products are treated as rigid rectangular cuboids; product dimensions are assumed to be accurate.
- Lowest cost means lowest box cost only, not shipping charges or total fulfilment cost.
- API endpoints are intentionally unauthenticated for local assignment demonstration. Production deployment needs authentication, permissions, secure settings, and appropriate input limits.

## Run tests

```bash
python manage.py test
```

Record your actual terminal output in `TEST_OUTPUT.md` after running the command. Do not claim tests passed until you have run them.

## Assignment submission checklist

- [ ] Push the reviewed code to your own GitHub repository.
- [ ] Include the actual `AI_USAGE.md` reflecting tools and assistance used.
- [ ] Export the actual chat transcript yourself from the ChatGPT interface and include the unaltered export in the repository and ZIP. Do not fabricate or AI-generate it.
- [ ] Write the “What I learned” reflection yourself, based on your own experience.
- [ ] Run tests and paste actual output into `TEST_OUTPUT.md`.
- [ ] Include test cases and all required files in one ZIP.
