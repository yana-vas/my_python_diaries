class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = Player.DEFAULT_GUILD

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        message = f"Name: {self.name}"
        message += '\n' + f"Guild: {self.guild}"
        message += '\n' + f"HP: {self.hp}"
        message += '\n' + f"MP: {self.mp}"
        for name, mana in self.skills.items():
            message += '\n' + f"==={name} - {mana}"
        return message



