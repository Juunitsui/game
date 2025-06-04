# game

This repository contains a simple game template. Character-related data is
stored in the `characters` package so that new characters can be added
without modifying the core engine.

## Damage calculation

Skills now implement a basic damage formula. Damage is based on the user's
level, the skill's element, power and the stats of the user and target. The
formula is:

```
(112 / 9) * attack * (level + 9) * skill_power / defense
```

When the skill's element is one of `FIRE`, `ICE`, `VOLT` or `WIND`, magic
attack and defense stats are used. Otherwise physical stats are used.
