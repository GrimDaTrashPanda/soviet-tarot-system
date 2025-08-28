#!/usr/bin/env python3
import random
from typing import List, Dict, Tuple

class TarotCard:
    def __init__(self, name: str, suit: str, upright_meaning: str, reversed_meaning: str):
        self.name = name
        self.suit = suit
        self.upright_meaning = upright_meaning
        self.reversed_meaning = reversed_meaning
    
    def __str__(self):
        return f"{self.name} of {self.suit}" if self.suit else self.name

class TarotDeck:
    def __init__(self):
        self.cards = self._create_deck()
        self.shuffle()
    
    def _create_deck(self) -> List[TarotCard]:
        cards = []
        
        # Major Arcana
        major_arcana = [
            ("The Fool", "New beginnings, innocence, adventure", "Recklessness, fear, poor judgment"),
            ("The Magician", "Manifestation, willpower, desire", "Manipulation, poor planning, untapped talents"),
            ("The High Priestess", "Intuition, sacred knowledge, divine feminine", "Secrets, disconnected from intuition, withdrawal"),
            ("The Empress", "Femininity, beauty, nature, abundance", "Creative block, dependence on others"),
            ("The Emperor", "Authority, establishment, structure, father figure", "Domination, excessive control, lack of discipline"),
            ("The Hierophant", "Spiritual wisdom, religious beliefs, conformity", "Personal beliefs, freedom, challenging tradition"),
            ("The Lovers", "Love, harmony, relationships, values alignment", "Self-love, disharmony, imbalance, misalignment"),
            ("The Chariot", "Control, willpower, success, determination", "Self-discipline, opposition, lack of direction"),
            ("Strength", "Strength, courage, persuasion, influence", "Self doubt, low energy, raw emotion"),
            ("The Hermit", "Soul searching, introspection, inner guidance", "Isolation, loneliness, withdrawal"),
            ("Wheel of Fortune", "Good luck, karma, life cycles, destiny", "Bad luck, lack of control, clinging to control"),
            ("Justice", "Justice, fairness, truth, cause and effect", "Unfairness, lack of accountability, dishonesty"),
            ("The Hanged Man", "Waiting, surrender, letting go, new perspective", "Delays, resistance, stalling, indecision"),
            ("Death", "Endings, change, transformation, transition", "Resistance to change, personal transformation, inner purging"),
            ("Temperance", "Balance, moderation, patience, purpose", "Imbalance, excess, self-healing, re-alignment"),
            ("The Devil", "Bondage, addiction, sexuality, materialism", "Releasing limiting beliefs, exploring dark thoughts, detachment"),
            ("The Tower", "Sudden change, upheaval, chaos, revelation", "Personal transformation, fear of change, averting disaster"),
            ("The Star", "Hope, faith, purpose, renewal, spirituality", "Lack of faith, despair, self-trust, disconnection"),
            ("The Moon", "Illusion, fear, anxiety, subconscious, intuition", "Release of fear, repressed emotion, inner confusion"),
            ("The Sun", "Positivity, fun, warmth, success, vitality", "Inner child, feeling down, overly optimistic"),
            ("Judgement", "Judgement, rebirth, inner calling, absolution", "Self-doubt, inner critic, ignoring the call"),
            ("The World", "Completion, integration, accomplishment, travel", "Seeking personal closure, short-cut to success, stagnation")
        ]
        
        for name, upright, reversed in major_arcana:
            cards.append(TarotCard(name, "", upright, reversed))
        
        # Minor Arcana
        suits = ["Wands", "Cups", "Swords", "Pentacles"]
        suit_meanings = {
            "Wands": ("creativity, spirituality, determination", "lack of energy, lack of passion, boredom"),
            "Cups": ("emotion, intuition, relationships", "repressed emotion, emotional loss, blocked creativity"),
            "Swords": ("thought, communication, conflict", "confusion, miscommunication, hostility"),
            "Pentacles": ("material world, career, money", "financial loss, poor investments, lack of planning")
        }
        
        court_cards = {
            "Page": ("curiosity, excitement, new ideas", "lack of direction, procrastination, creative blocks"),
            "Knight": ("action, adventure, fearlessness", "anger, impulsiveness, recklessness"),
            "Queen": ("confidence, self-assured, water", "self-respect, inner feelings"),
            "King": ("leadership, calm, diplomatic", "dictatorial, inflexible, overwhelming")
        }
        
        # Number cards (Ace through 10)
        for suit in suits:
            base_upright, base_reversed = suit_meanings[suit]
            
            # Ace
            cards.append(TarotCard("Ace", suit, f"New beginning in {suit.lower()}, {base_upright}", f"Blocked beginning, {base_reversed}"))
            
            # Numbers 2-10
            for i in range(2, 11):
                cards.append(TarotCard(str(i), suit, f"{base_upright}, progression", f"{base_reversed}, setbacks"))
            
            # Court cards
            for court, (court_up, court_rev) in court_cards.items():
                cards.append(TarotCard(court, suit, f"{court_up}, {base_upright}", f"{court_rev}, {base_reversed}"))
        
        return cards
    
    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)
    
    def draw_card(self) -> Tuple[TarotCard, bool]:
        """Draw a single card and determine if it's reversed"""
        if not self.cards:
            self.cards = self._create_deck()
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
    
    def single_card_reading(self) -> str:
        """Perform a single card reading"""
        card, is_reversed = self.deck.draw_card()
        orientation = "Reversed" if is_reversed else "Upright"
        meaning = card.reversed_meaning if is_reversed else card.upright_meaning
        
        reading = f"🔮 SINGLE CARD READING 🔮\n"
        reading += f"{'='*40}\n"
        reading += f"Card: {card}\n"
        reading += f"Orientation: {orientation}\n"
        reading += f"Meaning: {meaning}\n"
        return reading
    
    def three_card_reading(self) -> str:
        """Perform a three card reading (Past, Present, Future)"""
        cards = self.deck.draw_cards(3)
        positions = ["Past", "Present", "Future"]
        
        reading = f"🔮 THREE CARD READING 🔮\n"
        reading += f"{'='*40}\n"
        
        for i, (card, is_reversed) in enumerate(cards):
            orientation = "Reversed" if is_reversed else "Upright"
            meaning = card.reversed_meaning if is_reversed else card.upright_meaning
            
            reading += f"\n{positions[i]}: {card} ({orientation})\n"
            reading += f"Meaning: {meaning}\n"
        
        return reading
    
    def celtic_cross_reading(self) -> str:
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
        reading += f"{'='*50}\n"
        
        for i, (card, is_reversed) in enumerate(cards):
            orientation = "Reversed" if is_reversed else "Upright"
            meaning = card.reversed_meaning if is_reversed else card.upright_meaning
            
            reading += f"\n{i+1}. {positions[i]}: {card} ({orientation})\n"
            reading += f"   Meaning: {meaning}\n"
        
        return reading

def main():
    reader = TarotReader()
    
    print("✨ Welcome to the Tarot Card Reader! ✨\n")
    
    while True:
        print("\nChoose your reading:")
        print("1. Single Card Reading")
        print("2. Three Card Reading (Past, Present, Future)")
        print("3. Celtic Cross Reading (10 cards)")
        print("4. Shuffle deck")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            print(reader.single_card_reading())
        elif choice == '2':
            print(reader.three_card_reading())
        elif choice == '3':
            print(reader.celtic_cross_reading())
        elif choice == '4':
            reader.deck.shuffle()
            print("🔄 Deck shuffled!")
        elif choice == '5':
            print("🌟 Thank you for using the Tarot Card Reader! Blessed be! 🌟")
            break
        else:
            print("❌ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
