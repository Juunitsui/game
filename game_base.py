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

    def use(self, user: 'Character', target: 'Character'):
        """Placeholder for skill execution logic."""
        # Implement damage and effect calculations here
        raise NotImplementedError


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
