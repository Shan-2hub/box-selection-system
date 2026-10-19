# AI Usage Disclosure

> Review and edit this file so it accurately reflects your actual work before submission. Do not claim that you independently wrote, tested, or verified code unless you did so.

## AI tools used

- ChatGPT (OpenAI): used in this conversation to compare design options, propose a Django REST API architecture, scaffold implementation files, and suggest tests/documentation.
- Other tools: fill in only if actually used.

## Prompts used

The prompts in this project conversation included:
- “Before going to code gimme all the possible solutions ... finalize the one that'll be the best suit for this project.”
- “Finalize the box selection assignment design. Packing approach: 3D packing heuristic supporting multiple products; interface: Django REST API plus admin panel. Now guide me through implementing the project step by step, with complete files, tests, and honest assignment documentation.”

Add any further prompts you actually use.

## Outputs accepted or adapted

The current scaffold uses a Django REST API, Django ORM models, SQLite, admin pages, a separate packing module, and Django tests. The packing method is a deterministic corner-point heuristic. Review every file and be prepared to explain each design choice before submission.

## Outputs rejected or changed

Record each specific AI suggestion or generated code change that you personally rejected or modified. Do not invent examples. Suggested format:
- Suggestion/output:
- Why I rejected or changed it:
- What I implemented instead:

## Mistakes identified

After reviewing and running the project, record real issues you identify. Possible areas to inspect include heuristic limitations, invalid dimensions, weight boundaries, placement overlaps, API validation, and environment/setup issues. Do not list a mistake as discovered unless you actually checked it.

## Verification performed

Fill this section only after doing the work:
- [ ] Installed dependencies in a clean virtual environment.
- [ ] Ran database migrations.
- [ ] Ran `python manage.py check`.
- [ ] Ran `python manage.py test` and reviewed the output.
- [ ] Manually tested the API with valid and invalid requests.
- [ ] Reviewed placements for box-boundary and non-overlap correctness.
- [ ] Reviewed every generated/AI-assisted file and understand it.
- [ ] Confirmed the README commands work on my environment.

## Human review

Explain which parts you personally reviewed, changed, tested, and can explain in an interview. Keep this section factual.
