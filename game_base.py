from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional


class Element(Enum):
    FIRE = auto()
    ICE = auto()
    VOLT = auto()
    WIND = auto()
    SLASH = auto()
    STRIKE = auto()
    PIERCE = auto()


MAGIC_ELEMENTS = {Element.FIRE, Element.ICE, Element.VOLT, Element.WIND}
PHYSICAL_ELEMENTS = {Element.SLASH, Element.STRIKE, Element.PIERCE}


@dataclass
class Stats:
    hp: int
    physical_attack: int
    magic_attack: int
    physical_defense: int
    magic_defense: int
    speed: int


@dataclass
class Skill:
    name: str
    element: Element
    power: int
    cost: int

    def use(self, user: 'Character', target: 'Character', *, level: int = 1) -> int:
        """Calculate and apply damage to ``target`` using this skill.

        Parameters
        ----------
        user:
            Character using the skill.
        target:
            Character receiving the attack.
        level:
            The level of the user. Defaults to ``1``.

        Returns
        -------
        int
            The amount of damage dealt.
        """

        if self.element in MAGIC_ELEMENTS:
            attack = user.stats.magic_attack
            defense = target.stats.magic_defense
        else:
            attack = user.stats.physical_attack
            defense = target.stats.physical_defense

        base = (112 / 9) * attack * (level + 9) * self.power
        damage = int(base / max(defense, 1))

        target.take_damage(damage)
        return damage


@dataclass
class Character:
    name: str
    stats: Stats
    skill1: Skill
    skill2: Skill
    ultimate: Skill
    element: Optional[Element] = None

    def take_damage(self, amount: int):
        self.stats.hp = max(0, self.stats.hp - amount)

    def is_defeated(self) -> bool:
        return self.stats.hp <= 0


# Example usage
if __name__ == "__main__":
    from characters.hero import create_hero

    hero = create_hero()
    print(hero)
