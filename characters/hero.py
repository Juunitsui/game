from game_base import Character, Stats, Skill, Element


def create_hero() -> Character:
    """Return an instance of the default hero character."""
    fireball = Skill("Fireball", Element.FIRE, power=50, cost=10)
    ice_spike = Skill("Ice Spike", Element.ICE, power=45, cost=10)
    blazing_nova = Skill("Blazing Nova", Element.FIRE, power=100, cost=25)

    hero_stats = Stats(
        hp=100,
        physical_attack=20,
        magic_attack=30,
        physical_defense=15,
        magic_defense=10,
        speed=5,
    )

    return Character(
        name="Hero",
        stats=hero_stats,
        skill1=fireball,
        skill2=ice_spike,
        ultimate=blazing_nova,
        element=Element.FIRE,
    )
