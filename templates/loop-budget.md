# Loop Budget Configuration

**Daily Budget Cap:** $5.00  
**Current Daily Spend:** $0.00  
**Last Updated:** 2026-06-30 00:00:00  
**Kill Switch Triggered:** False  

---

## Limits by Loop Category

| Category | Daily Limit | Warning Threshold | Max Iterations |
| :--- | :--- | :--- | :--- |
| Core | $2.00 | $1.50 | 5 |
| Engineering | $1.50 | $1.00 | 5 |
| Platform | $1.00 | $0.80 | 5 |
| Governance | $0.50 | $0.40 | 3 |
| Release | $0.50 | $0.40 | 3 |

---

## Action Policies
- If **Kill Switch Triggered** is set to `True`, all active loops must halt immediately before starting any token-consuming agent steps.
- If **Current Daily Spend** exceeds **Daily Budget Cap**, the Kill Switch is set to `True` automatically by the `loop-budget` skill.
