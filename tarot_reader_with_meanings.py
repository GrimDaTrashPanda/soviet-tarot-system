#!/usr/bin/env python3
import random
from typing import List, Dict, Tuple

class TarotCard:
    def __init__(self, name: str, suit: str, upright_meaning: str, reversed_meaning: str, 
                 upright_keywords: List[str], reversed_keywords: List[str], 
                 description: str, symbolism: str = ""):
        self.name = name
        self.suit = suit
        self.upright_meaning = upright_meaning
        self.reversed_meaning = reversed_meaning
        self.upright_keywords = upright_keywords
        self.reversed_keywords = reversed_keywords
        self.description = description
        self.symbolism = symbolism
    
    def __str__(self):
        return f"{self.name} of {self.suit}" if self.suit else self.name
    
    def get_detailed_meaning(self, is_reversed: bool) -> str:
        orientation = "Reversed" if is_reversed else "Upright"
        keywords = ", ".join(self.reversed_keywords if is_reversed else self.upright_keywords)
        meaning = self.reversed_meaning if is_reversed else self.upright_meaning
        
        detail = f"🔮 {self} ({orientation}) 🔮\n"
        detail += f"{'='*50}\n"
        detail += f"Keywords: {keywords}\n\n"
        detail += f"Meaning: {meaning}\n\n"
        detail += f"Description: {self.description}\n"
        if self.symbolism:
            detail += f"\nSymbolism: {self.symbolism}\n"
        detail += f"{'='*50}"
        
        return detail

class TarotDeck:
    def __init__(self):
        self.cards = self._create_detailed_deck()
        self.shuffle()
    
    def _create_detailed_deck(self) -> List[TarotCard]:
        cards = []
        
        # Major Arcana with detailed meanings
        major_arcana_data = [
            ("The Fool", "", 
             "New beginnings, innocence, adventure, spontaneity, free spirit",
             "Recklessness, taken advantage of, inconsideration, foolishness",
             ["beginnings", "innocence", "spontaneity", "free spirit", "adventure"],
             ["recklessness", "carelessness", "risk-taking", "foolishness", "chaos"],
             "The Fool represents new beginnings and having faith in the future. This card encourages you to have an open, curious mind and a sense of excitement. Embrace the unknown and trust in the journey ahead.",
             "The Fool carries a white rose (purity), stands at cliff's edge (leap of faith), with a small bag (untapped knowledge) and loyal dog (instincts)."
            ),
            
            ("The Magician", "",
             "Manifestation, resourcefulness, power, inspired action, willpower",
             "Manipulation, poor planning, latent talents, trickery, illusions",
             ["manifestation", "power", "skill", "concentration", "resourcefulness"],
             ["manipulation", "cunning", "trickery", "wasted talent", "illusion"],
             "The Magician is about taking action and having the skills and tools to accomplish your goals. You have the power to manifest your desires through focused will and determination.",
             "One hand points to heaven, one to earth (as above, so below). The infinity symbol above his head represents unlimited potential. The four suit symbols represent mastery of all elements."
            ),
            
            ("The High Priestess", "",
             "Intuition, sacred knowledge, divine feminine, the subconscious mind",
             "Secrets, disconnected from intuition, withdrawal and silence",
             ["intuition", "wisdom", "divine feminine", "subconscious", "mystery"],
             ["hidden motives", "superficiality", "confusion", "cognitive dissonance"],
             "The High Priestess sits between the conscious and subconscious realms. She encourages you to trust your intuition and look beyond the obvious. Inner wisdom and spiritual insight guide you.",
             "Seated between two pillars (duality), pomegranates on curtain (feminine fertility), crescent moon at feet (intuition), Torah scroll (hidden knowledge)."
            ),
            
            ("The Empress", "",
             "Femininity, beauty, nature, abundance, nurturing, creativity",
             "Creative block, dependence on others, smothering, lack of growth",
             ["abundance", "nurturing", "fertility", "creativity", "beauty"],
             ["dependence", "smothering", "emptiness", "creative block"],
             "The Empress represents the abundant, fertile, life-giving Mother archetype. She suggests a time of growth, creativity, and material abundance. Connect with your nurturing side.",
             "Surrounded by nature, wheat symbolizes fertility, Venus symbol represents love and beauty, crown of 12 stars represents connection to mystical realm."
            ),
            
            ("The Emperor", "",
             "Authority, father-figure, structure, solid foundation, stability",
             "Domination, excessive control, lack of discipline, inflexibility",
             ["authority", "structure", "control", "leadership", "father figure"],
             ["domination", "rigidity", "coldness", "lack of discipline"],
             "The Emperor represents authority, structure, and control. He suggests that you take a leadership role and create order from chaos. Establish boundaries and take responsibility.",
             "Sits on throne with ram heads (Aries/leadership), holds ankh (life) and orb (world), red robes (passion), armor (protection), barren mountains (masculine energy)."
            ),
            
            ("The Hierophant", "",
             "Spiritual wisdom, religious beliefs, conformity, tradition, institutions",
             "Personal beliefs, freedom, challenging the status quo, unconventional",
             ["tradition", "conformity", "morality", "ethics", "knowledge"],
             ["rebellion", "unconventional", "freedom", "personal beliefs"],
             "The Hierophant represents traditional learning and spiritual guidance. He suggests seeking wisdom from established institutions or mentors, following conventional paths.",
             "Religious figure between two pillars, two acolytes (learning/teaching), triple crown (conscious/subconscious/superconscious), keys at feet (unlocking mysteries)."
            ),
            
            ("The Lovers", "",
             "Love, harmony, relationships, values alignment, choices, unity",
             "Self-love, disharmony, imbalance, misalignment of values, broken relationship",
             ["love", "relationships", "choices", "values", "harmony"],
             ["disharmony", "imbalance", "misalignment", "broken relationships"],
             "The Lovers represents deep connections and important choices. It's about finding harmony and balance in relationships and aligning your values with your actions.",
             "Adam and Eve beneath angel Raphael (healing/communication), tree of knowledge (conscious decisions), tree of life (subconscious), mountains (higher guidance)."
            ),
            
            ("The Chariot", "",
             "Control, willpower, success, determination, focus, hard work",
             "Lack of control, lack of direction, aggression, powerlessness",
             ["control", "willpower", "success", "determination", "victory"],
             ["lack of control", "aggression", "powerlessness", "defeat"],
             "The Chariot represents triumph through maintaining focus and determination. Success comes through balancing opposing forces and staying true to your path despite obstacles.",
             "Sphinx pulling in opposite directions (opposing forces), canopy of stars (celestial influence), city behind (civilization), armor (protection)."
            ),
            
            ("Strength", "",
             "Strength, courage, patience, control, compassion, inner power",
             "Self-doubt, weakness, low energy, lack of confidence, feeling powerless",
             ["inner strength", "courage", "patience", "compassion", "control"],
             ["self-doubt", "weakness", "lack of confidence", "aggression"],
             "Strength represents inner power and the ability to overcome challenges through patience and compassion rather than force. True strength comes from within.",
             "Woman gently closing lion's mouth (taming beast through love), infinity symbol (unlimited potential), white robes (purity), flower garland (nature's blessing)."
            ),
            
            ("The Hermit", "",
             "Soul searching, introspection, inner guidance, seeking truth, wisdom",
             "Isolation, loneliness, withdrawal, lost your way, seeking external answers",
             ["introspection", "guidance", "wisdom", "soul searching", "inner light"],
             ["isolation", "loneliness", "withdrawal", "lost", "stubbornness"],
             "The Hermit suggests a time of introspection and inner soul searching. Step back from the external world to find answers within. Seek your inner wisdom and truth.",
             "Holds lantern (inner wisdom lighting the way), star in lantern (guidance), staff (authority/support), mountain peak (spiritual achievement), gray robes (invisibility)."
            ),
            
            ("Wheel of Fortune", "",
             "Good luck, karma, life cycles, destiny, turning point, fortune",
             "Bad luck, lack of control, clinging to control, unwanted changes",
             ["luck", "karma", "cycles", "destiny", "change"],
             ["bad luck", "lack of control", "setbacks", "unwanted change"],
             "The Wheel of Fortune represents the cyclical nature of life and fate. What goes up must come down, and vice versa. Accept the natural cycles and flow of life.",
             "Wheel with Hebrew letters YHVH (Tetragrammaton), TARO/ROTA (Tarot/Wheel), sphinx on top (riddle of life), snake descending (underworld), Anubis ascending (afterlife)."
            ),
            
            ("Justice", "",
             "Justice, fairness, truth, cause and effect, law, balance, accountability",
             "Unfairness, lack of accountability, dishonesty, retribution, bias",
             ["justice", "fairness", "truth", "law", "balance"],
             ["unfairness", "bias", "dishonesty", "lack of accountability"],
             "Justice represents fairness, truth, and the law of cause and effect. Decisions should be made with careful consideration and moral clarity. Truth will prevail.",
             "Scales (balanced judgment), sword (swift justice), red robes (passion for justice), crown (authority), pillars (law and structure)."
            ),
            
            ("The Hanged Man", "",
             "Waiting, surrender, letting go, new perspective, sacrifice, release",
             "Delays, resistance, stalling, indecision, avoiding sacrifice",
             ["sacrifice", "waiting", "letting go", "new perspective", "surrender"],
             ["delays", "resistance", "stalling", "indecision"],
             "The Hanged Man suggests a time of voluntary surrender and suspension. Sometimes you must let go and see things from a different perspective to gain enlightenment.",
             "Hanging upside down by one foot (voluntary sacrifice), serene expression (inner peace), halo (enlightenment), red pants (human passion), blue shirt (calm wisdom)."
            ),
            
            ("Death", "",
             "Endings, change, transformation, transition, new beginnings, letting go",
             "Resistance to change, fear of change, stagnation, decay, inability to move on",
             ["transformation", "change", "endings", "rebirth", "transition"],
             ["resistance to change", "stagnation", "fear", "inability to let go"],
             "Death represents transformation and the end of a major phase in life. This is about letting go of the old to make way for the new. Embrace change and transformation.",
             "Skeleton in black armor (death comes to all), white horse (purity), black flag with white rose (beauty after death), rising sun (rebirth), people of all classes (equality in death)."
            ),
            
            ("Temperance", "",
             "Balance, moderation, patience, purpose, meaning, divine guidance",
             "Imbalance, excess, lack of long-term vision, discord, recklessness",
             ["balance", "moderation", "patience", "harmony", "guidance"],
             ["imbalance", "excess", "discord", "impatience"],
             "Temperance is about finding balance and moderation in all aspects of life. Take a patient, measured approach and seek to harmonize opposing forces within yourself.",
             "Angel mixing water between cups (balance of conscious/subconscious), one foot on land/one in water (material/emotional balance), triangle on chest (alchemy), iris flowers (goddess messenger)."
            ),
            
            ("The Devil", "",
             "Bondage, addiction, sexuality, materialism, feeling trapped, temptation",
             "Releasing limiting beliefs, exploring dark thoughts, detachment, freedom",
             ["bondage", "temptation", "sexuality", "materialism", "addiction"],
             ["freedom", "release", "detachment", "breaking chains"],
             "The Devil represents feeling trapped by material desires or negative patterns. Recognize that these chains are often self-imposed and can be broken through awareness.",
             "Horned devil (pan/natural instincts), inverted pentagram (material over spiritual), chained couple (self-imposed bondage), loose chains (freedom is possible), torch (passion/temptation)."
            ),
            
            ("The Tower", "",
             "Sudden change, upheaval, chaos, revelation, awakening, disaster",
             "Averting disaster, delaying the inevitable, fear of change, trauma recovery",
             ["upheaval", "revelation", "awakening", "disaster", "change"],
             ["averting disaster", "fear of change", "trauma", "recovery"],
             "The Tower represents sudden change that shakes the very foundation of your life. Though disruptive, this destruction clears the way for new growth and understanding.",
             "Tower struck by lightning (divine intervention), crown knocked off (ego destroyed), people falling (humbling experience), 22 flames (Hebrew letters), rocky ground (unstable foundation)."
            ),
            
            ("The Star", "",
             "Hope, faith, purpose, renewal, spirituality, inspiration, healing",
             "Lack of faith, despair, self-trust, disconnection, pessimism",
             ["hope", "faith", "inspiration", "healing", "renewal"],
             ["despair", "lack of faith", "disconnection", "pessimism"],
             "The Star brings hope and spiritual guidance after hardship. It represents faith in the future and connection to divine wisdom. Trust in the universe's plan for you.",
             "Naked woman (vulnerable truth), pouring water on land and in pool (conscious/subconscious nourishment), seven small stars (chakras), one large star (guidance), ibis bird (wisdom)."
            ),
            
            ("The Moon", "",
             "Illusion, fear, anxiety, subconscious, intuition, dreams, deception",
             "Release of fear, repressed emotion, inner confusion, unveiling illusion",
             ["illusion", "intuition", "dreams", "subconscious", "mystery"],
             ["fear", "confusion", "deception", "repressed emotion"],
             "The Moon represents the realm of illusion and the subconscious mind. Things are not as they seem. Trust your intuition to guide you through uncertainty and confusion.",
             "Full moon (illusion/intuition), wolf and dog (tamed/wild nature), crayfish (emerging from subconscious), path between towers (journey through unknown), 18 rays (chai/life)."
            ),
            
            ("The Sun", "",
             "Positivity, fun, warmth, success, vitality, joy, enlightenment",
             "Inner child, feeling down, overly optimistic, lack of success, sadness",
             ["joy", "success", "vitality", "positivity", "enlightenment"],
             ["sadness", "lack of success", "pessimism", "inner child issues"],
             "The Sun represents joy, success, and positive energy. This is a time of happiness, vitality, and achievement. Embrace your inner child and celebrate life's simple pleasures.",
             "Bright sun (enlightenment/joy), naked child on horse (innocence/new growth), sunflowers (life/fertility), red banner (passion/action), brick wall (strength/stability)."
            ),
            
            ("Judgement", "",
             "Judgement, rebirth, inner calling, absolution, second chances, awakening",
             "Self-doubt, inner critic, ignoring the call, lack of self-awareness",
             ["rebirth", "awakening", "calling", "absolution", "renewal"],
             ["self-doubt", "inner critic", "ignoring calling", "lack of awareness"],
             "Judgement represents spiritual rebirth and answering a higher calling. It's time for self-reflection, forgiveness, and making amends. Embrace your true purpose.",
             "Angel Gabriel (messenger of God), trumpet (divine calling), people rising from graves (rebirth), mountains (higher consciousness), cross on flag (sacrifice/redemption)."
            ),
            
            ("The World", "",
             "Completion, integration, accomplishment, travel, fulfillment, success",
             "Seeking personal closure, stagnation, lack of achievement, incomplete goals",
             ["completion", "success", "fulfillment", "integration", "achievement"],
             ["stagnation", "incomplete", "lack of closure", "unfulfilled"],
             "The World represents the completion of a major life cycle and the achievement of your goals. You have reached a state of wholeness and fulfillment. Celebrate your accomplishments.",
             "Dancing figure (celebration/movement), laurel wreath (victory), four creatures in corners (four evangelists/elements), purple cloth (royalty/achievement), twin wands (balance)."
            )
        ]
        
        for name, suit, upright, reversed, up_keywords, rev_keywords, description, symbolism in major_arcana_data:
            cards.append(TarotCard(name, suit, upright, reversed, up_keywords, rev_keywords, description, symbolism))
        
        # Minor Arcana with detailed meanings
        suits_data = {
            "Wands": {
                "element": "Fire",
                "theme": "creativity, passion, spirituality, energy, career, growth",
                "reversed_theme": "lack of energy, lack of passion, boredom, stagnation"
            },
            "Cups": {
                "element": "Water", 
                "theme": "emotions, intuition, relationships, love, spirituality",
                "reversed_theme": "emotional loss, blocked creativity, bad relationships"
            },
            "Swords": {
                "element": "Air",
                "theme": "thought, communication, conflict, logic, ideas",
                "reversed_theme": "confusion, miscommunication, hostility, mental fog"
            },
            "Pentacles": {
                "element": "Earth",
                "theme": "material world, career, money, health, manifestation",
                "reversed_theme": "financial loss, poor investments, lack of planning"
            }
        }
        
        # Add detailed minor arcana
        for suit, suit_info in suits_data.items():
            element = suit_info["element"]
            theme = suit_info["theme"]
            rev_theme = suit_info["reversed_theme"]
            
            # Ace
            cards.append(TarotCard(
                "Ace", suit,
                f"New beginning in {theme.split(',')[0]}, raw potential, opportunity, spiritual energy",
                f"Missed opportunity, {rev_theme}, blocked potential",
                ["new beginning", "potential", "opportunity", "raw energy"],
                ["missed opportunity", "blocked potential", "delays"],
                f"The Ace of {suit} represents a new beginning in the realm of {element.lower()}. This is raw, untapped potential waiting to be developed. A gift from the universe.",
                f"Hand emerging from cloud offering {suit[:-1].lower()}, representing divine gift of {element.lower()} energy."
            ))
            
            # Number cards 2-10 with specific meanings
            number_meanings = {
                2: ("balance, partnership, cooperation, duality", "imbalance, broken partnership, lack of cooperation"),
                3: ("creativity, collaboration, teamwork, growth", "lack of teamwork, creative blocks, scattered energy"),
                4: ("stability, structure, foundation, manifestation", "instability, lack of foundation, stagnation"),
                5: ("conflict, change, challenge, instability", "avoiding conflict, fear of change, inner conflict"),
                6: ("harmony, generosity, sharing, community", "selfishness, lack of support, imbalance"),
                7: ("perseverance, spiritual growth, inner wisdom", "lack of progress, giving up, misdirection"),
                8: ("mastery, achievement, success, recognition", "lack of recognition, amateur efforts, failure"),
                9: ("near completion, wisdom, experience, independence", "lack of experience, dependence, incomplete projects"),
                10: ("completion, fulfillment, achievement, legacy", "incomplete, seeking recognition, burden")
            }
            
            for num in range(2, 11):
                up_meaning, rev_meaning = number_meanings[num]
                cards.append(TarotCard(
                    str(num), suit,
                    f"{up_meaning}, {theme}",
                    f"{rev_meaning}, {rev_theme}",
                    up_meaning.split(", "),
                    rev_meaning.split(", "),
                    f"The {num} of {suit} represents {up_meaning.split(', ')[0]} in the realm of {element.lower()}. This card shows progression and development in {theme.split(',')[0]}.",
                    f"The number {num} represents {up_meaning.split(', ')[0]} and development in the {element.lower()} element."
                ))
            
            # Court cards with detailed meanings
            court_data = {
                "Page": ("curiosity, excitement, new ideas, student, messenger", "lack of direction, procrastination, immaturity", 
                        "The Page represents a student or messenger, eager to learn and explore new aspects"),
                "Knight": ("action, adventure, impulsiveness, determination", "recklessness, haste, lack of planning",
                          "The Knight represents action and movement, sometimes impulsive but always determined"),
                "Queen": ("nurturing, intuitive, emotionally mature, supportive", "self-care needed, emotional manipulation, moodiness",
                         "The Queen represents emotional maturity and nurturing energy, deeply intuitive"),
                "King": ("leadership, mastery, authority, mature wisdom", "abuse of power, lack of leadership, immaturity",
                        "The King represents mastery and mature leadership in his suit's domain")
            }
            
            for court, (up_meaning, rev_meaning, description) in court_data.items():
                cards.append(TarotCard(
                    court, suit,
                    f"{up_meaning}, mastery of {theme}",
                    f"{rev_meaning}, misuse of {theme}",
                    up_meaning.split(", "),
                    rev_meaning.split(", "),
                    f"{description} of {suit.lower()}. They embody the {element.lower()} element in human form.",
                    f"Court card representing human mastery of {element.lower()} energy and {theme.split(',')[0]}."
                ))
        
        return cards
    
    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)
    
    def draw_card(self) -> Tuple[TarotCard, bool]:
        """Draw a single card and determine if it's reversed"""
        if not self.cards:
            self.cards = self._create_detailed_deck()
            self.shuffle()
        
        card = self.cards.pop()
        is_reversed = random.choice([True, False])
        return card, is_reversed
    
    def draw_cards(self, num_cards: int) -> List[Tuple[TarotCard, bool]]:
        """Draw multiple cards"""
        return [self.draw_card() for _ in range(num_cards)]

class TarotReader:
    def __init__(self):
        self.deck = TarotDeck()
    
    def single_card_reading(self, show_details: bool = True) -> str:
        """Perform a single card reading with optional detailed meanings"""
        card, is_reversed = self.deck.draw_card()
        
        if show_details:
            return card.get_detailed_meaning(is_reversed)
        else:
            orientation = "Reversed" if is_reversed else "Upright"
            meaning = card.reversed_meaning if is_reversed else card.upright_meaning
            
            reading = f"🔮 SINGLE CARD READING 🔮\n"
            reading += f"{'='*40}\n"
            reading += f"Card: {card}\n"
            reading += f"Orientation: {orientation}\n"
            reading += f"Meaning: {meaning}\n"
            return reading
    
    def three_card_reading(self, show_details: bool = True) -> str:
        """Perform a three card reading (Past, Present, Future)"""
        cards = self.deck.draw_cards(3)
        positions = ["Past", "Present", "Future"]
        
        reading = f"🔮 THREE CARD READING 🔮\n"
        reading += f"{'='*50}\n"
        
        if show_details:
            for i, (card, is_reversed) in enumerate(cards):
                reading += f"\n📍 {positions[i].upper()} POSITION:\n"
                reading += card.get_detailed_meaning(is_reversed) + "\n"
        else:
            for i, (card, is_reversed) in enumerate(cards):
                orientation = "Reversed" if is_reversed else "Upright"
                meaning = card.reversed_meaning if is_reversed else card.upright_meaning
                
                reading += f"\n{positions[i]}: {card} ({orientation})\n"
                reading += f"Meaning: {meaning}\n"
        
        return reading
    
    def celtic_cross_reading(self, show_details: bool = False) -> str:
        """Perform a Celtic Cross reading (10 cards)"""
        cards = self.deck.draw_cards(10)
        positions = [
            "Present Situation",
            "Challenge/Cross",
            "Distant Past/Foundation", 
            "Recent Past",
            "Possible Outcome",
            "Near Future",
            "Your Approach",
            "External Influences",
            "Hopes and Fears",
            "Final Outcome"
        ]
        
        reading = f"🔮 CELTIC CROSS READING 🔮\n"
        reading += f"{'='*60}\n"
        
        if show_details:
            for i, (card, is_reversed) in enumerate(cards):
                reading += f"\n📍 {positions[i].upper()}:\n"
                reading += card.get_detailed_meaning(is_reversed) + "\n"
        else:
            for i, (card, is_reversed) in enumerate(cards):
                orientation = "Reversed" if is_reversed else "Upright"
                meaning = card.reversed_meaning if is_reversed else card.upright_meaning
                keywords = ", ".join(card.reversed_keywords if is_reversed else card.upright_keywords)
                
                reading += f"\n{i+1}. {positions[i]}: {card} ({orientation})\n"
                reading += f"   Keywords: {keywords}\n"
                reading += f"   Meaning: {meaning}\n"
        
        return reading
    
    def card_meanings_lookup(self) -> str:
        """Show all card meanings for reference"""
        lookup = "📚 TAROT CARD MEANINGS REFERENCE 📚\n"
        lookup += "="*60 + "\n"
        
        # Major Arcana
        lookup += "\n🌟 MAJOR ARCANA:\n" + "-"*30 + "\n"
        major_cards = [card for card in self.deck._create_detailed_deck() if not card.suit]
        for card in major_cards:
            lookup += f"\n{card.name}:\n"
            lookup += f"  Upright: {', '.join(card.upright_keywords)}\n"
            lookup += f"  Reversed: {', '.join(card.reversed_keywords)}\n"
        
        # Minor Arcana by suit
        suits = ["Wands", "Cups", "Swords", "Pentacles"]
        suit_elements = {"Wands": "Fire", "Cups": "Water", "Swords": "Air", "Pentacles": "Earth"}
        
        for suit in suits:
            lookup += f"\n🔥 {suit.upper()} ({suit_elements[suit]} Element):\n" + "-"*30 + "\n"
            suit_cards = [card for card in self.deck._create_detailed_deck() if card.suit == suit]
            for card in sorted(suit_cards, key=lambda x: (x.name == "Ace", x.name.isdigit() and int(x.name), x.name)):
                lookup += f"{card.name} of {suit}: {', '.join(card.upright_keywords[:3])}\n"
        
        return lookup

def main():
    reader = TarotReader()
    
    print("✨ Welcome to the Enhanced Tarot Card Reader! ✨")
    print("🔮 Complete with detailed meanings, symbolism, and interpretations 🔮\n")
    
    while True:
        print("\n" + "="*60)
        print("🃏 Choose your reading:")
        print("1. Single Card Reading (Detailed)")
        print("2. Single Card Reading (Quick)")
        print("3. Three Card Reading (Detailed)")
        print("4. Three Card Reading (Quick)")
        print("5. Celtic Cross Reading (Full)")
        print("6. Celtic Cross Reading (Summary)")
        print("7. Card Meanings Reference")
        print("8. Shuffle deck")
        print("9. Exit")
        print("="*60)
        
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == '1':
            print("\n" + reader.single_card_reading(show_details=True))
        elif choice == '2':
            print("\n" + reader.single_card_reading(show_details=False))
        elif choice == '3':
            print("\n" + reader.three_card_reading(show_details=True))
        elif choice == '4':
            print("\n" + reader.three_card_reading(show_details=False))
        elif choice == '5':
            print("\n" + reader.celtic_cross_reading(show_details=True))
        elif choice == '6':
            print("\n" + reader.celtic_cross_reading(show_details=False))
        elif choice == '7':
            print("\n" + reader.card_meanings_lookup())
        elif choice == '8':
            reader.deck.shuffle()
            print("\n🔄 Deck shuffled! The cards have been mixed with fresh energy.")
        elif choice == '9':
            print("\n🌟 Thank you for using the Enhanced Tarot Card Reader!")
            print("✨ May the wisdom of the cards guide you on your journey! ✨")
            break
        else:
            print("❌ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()