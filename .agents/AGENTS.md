# Global Agent Rules

## Loop Authoring and Documentation Updates
Whenever you create or update a loop (`LOOP-XXX`) within this project, you **MUST diligently update all required documentation and references** across the repository. This is non-negotiable. 

This includes, but is not limited to:
- `docs/loop-catalog.md` (Add or modify the entry)
- `shared/SPEC-010-Loop-Catalog.md` (Add or modify the specification entry)
- `shared/loops-manifest.json` (Add the new loop to the relevant categories: Greenfield, Brownfield, Modernization)
- `docs/aeos-loop-instructions-by-project-type.md` (Ensure there's an instructional entry/explainer)
- `docs/project-loops-ready-reckoner.md` (Ensure the loop is listed in the ready reckoner tables)
- `USER_GUIDE.md` (If applicable)

Always do a final review to ensure that the newly created or updated loop does not result in an orphaned or untracked file. Use the loop ID (e.g., `LOOP-XXX`) to search across the codebase and verify that it has been properly linked and documented in these index/catalog documents.
