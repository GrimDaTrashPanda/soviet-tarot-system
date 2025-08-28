#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox, scrolledtext
import random
import time
import threading
from typing import List, Dict, Tuple

class SovietTarotCard:
    def __init__(self, name: str, suit: str, upright_meaning: str, reversed_meaning: str, 
                 soviet_name: str = "", soviet_symbolism: str = ""):
        self.name = name
        self.suit = suit
        self.upright_meaning = upright_meaning
        self.reversed_meaning = reversed_meaning
        self.soviet_name = soviet_name or name
        self.soviet_symbolism = soviet_symbolism
    
    def __str__(self):
        return f"{self.name} of {self.suit}" if self.suit else self.name
    
    def get_soviet_name(self):
        return f"{self.soviet_name} of {self.suit}" if self.suit else self.soviet_name

class SovietTarotDeck:
    def __init__(self):
        self.cards = self._create_soviet_deck()
        self.shuffle()
    
    def _create_soviet_deck(self) -> List[SovietTarotCard]:
        cards = []
        
        # Revolutionary Major Arcana
        major_arcana = [
            ("The Fool", "The Young Pioneer", 
             "New socialist beginnings, revolutionary spirit, leap of faith into communism",
             "Counter-revolutionary tendencies, bourgeois hesitation, lack of class consciousness",
             "Represents the youth embracing the revolutionary cause with innocent enthusiasm"),
            
            ("The Magician", "The Party Secretary", 
             "Manifestation of the People's Will, organizational power, revolutionary leadership",
             "Bureaucratic corruption, abuse of party position, disconnection from masses",
             "Channels the collective power of the proletariat to transform reality"),
            
            ("The High Priestess", "The Babushka Oracle", 
             "Ancient wisdom of the motherland, intuitive understanding of socialist principles",
             "Superstition over science, resistance to progressive thought, mystical confusion",
             "Keeper of traditional knowledge adapted to serve the socialist cause"),
            
            ("The Empress", "Mother Russia", 
             "Abundant motherland, nurturing the collective, fertility of socialist ideals",
             "Nationalist excess, maternal smothering of individual growth, resource hoarding",
             "The fertile land that provides for all her children equally"),
            
            ("The Emperor", "The Chairman", 
             "Strong socialist leadership, structure of the planned economy, paternal guidance",
             "Authoritarian excess, rigid bureaucracy, disconnection from worker needs",
             "Provides order and structure necessary for building communist society"),
            
            ("The Hierophant", "The Ideological Instructor", 
             "Orthodox Marxist-Leninist teaching, conformity to party line, collective wisdom",
             "Dogmatic thinking, resistance to dialectical development, intellectual stagnation",
             "Transmits the sacred knowledge of scientific socialism to the masses"),
            
            ("The Lovers", "The Collective Marriage", 
             "Unity of purpose, choice between individual and collective good, socialist love",
             "Bourgeois individualism, broken solidarity, choosing self over community",
             "The harmonious relationship between individual desires and collective needs"),
            
            ("The Chariot", "The Five Year Plan", 
             "Triumphant progress toward communist goals, willpower of the masses, economic victory",
             "Failed quotas, lack of coordination, industrial stagnation",
             "The unstoppable advance of socialist production and social development"),
            
            ("Strength", "The Woman Tractor Driver", 
             "Inner strength of the proletariat, gentle guidance of revolutionary force, courage",
             "Weakness in face of reaction, loss of revolutionary spirit, bourgeois softness",
             "Feminine strength taming the forces of production for socialist construction"),
            
            ("The Hermit", "The Siberian Exile", 
             "Inner reflection on revolutionary principles, wisdom gained through struggle, introspection",
             "Isolation from the collective, withdrawal from social responsibility, pessimism",
             "Solitary contemplation leading to deeper understanding of socialist truth"),
            
            ("Wheel of Fortune", "The Historical Dialectic", 
             "Inevitable progress of history toward communism, cycles of revolutionary development",
             "Reactionary forces temporarily ascendant, loss of historical perspective",
             "The great wheel of historical materialism turning toward socialist victory"),
            
            ("Justice", "The People's Court", 
             "Revolutionary justice, equality before socialist law, truth serving the people",
             "Class justice favoring bourgeoisie, corruption of revolutionary tribunals",
             "Justice administered by and for the working class, not bourgeois abstractions"),
            
            ("The Hanged Man", "The Sacrificial Comrade", 
             "Sacrifice for the collective good, martyrdom for socialist cause, suspended judgment",
             "Useless sacrifice, resistance to necessary change, inability to act decisively",
             "Voluntary sacrifice of individual comfort for the advancement of all humanity"),
            
            ("Death", "The End of Capitalism", 
             "Death of bourgeois society, transformation to socialist mode of production",
             "Resistance to necessary social change, clinging to outdated economic forms",
             "The inevitable death of exploitative systems and birth of socialist relations"),
            
            ("Temperance", "The Planned Economy", 
             "Balance of production and consumption, moderation in resource use, economic harmony",
             "Economic imbalance, waste of collective resources, lack of central coordination",
             "Harmonious balance achieved through scientific economic planning"),
            
            ("The Devil", "The Capitalist Exploiter", 
             "Bondage to bourgeois ideology, addiction to profit, material temptation",
             "Liberation from capitalist chains, rejection of consumerist values, freedom",
             "The false consciousness that keeps workers chained to exploitative systems"),
            
            ("The Tower", "The Fall of the Winter Palace", 
             "Revolutionary overthrow of old order, sudden collapse of bourgeois power",
             "Failed revolution, premature uprising, restoration of reactionary forces",
             "The violent but necessary destruction of oppressive class structures"),
            
            ("The Star", "The Red Star of Hope", 
             "Hope for communist future, guidance by revolutionary ideals, international solidarity",
             "Loss of revolutionary hope, nationalism over internationalism, despair",
             "The guiding light of socialist ideals illuminating the path to liberation"),
            
            ("The Moon", "The Fog of False Consciousness", 
             "Bourgeois illusions, confusion caused by capitalist propaganda, unclear class relations",
             "Clearing away ideological confusion, seeing through bourgeois lies, class clarity",
             "The deceptive appearance of capitalist 'freedom' hiding exploitation beneath"),
            
            ("The Sun", "The Dawn of Communism", 
             "Joy of liberated humanity, success of socialist construction, enlightened consciousness",
             "Premature celebration, incomplete revolution, bourgeois restoration",
             "The radiant future of fully realized communist society where all humanity thrives"),
            
            ("Judgement", "The Final Revolution", 
             "Ultimate judgment on class society, resurrection of human potential, final awakening",
             "Incomplete consciousness, failure to achieve full human liberation, judgment postponed",
             "The final revolutionary transformation that liberates all human creative potential"),
            
            ("The World", "The Global Soviet", 
             "Achievement of world socialism, completion of human historical development",
             "Incomplete internationalism, failure to achieve global solidarity, isolation",
             "The fulfilled promise of international socialism embracing all humanity")
        ]
        
        for name, soviet_name, upright, reversed, symbolism in major_arcana:
            cards.append(SovietTarotCard(name, "", upright, reversed, soviet_name, symbolism))
        
        # Proletarian Minor Arcana
        suits_data = {
            "Hammers": ("Industrial Labor", "creativity, labor, industrial production, worker solidarity", 
                       "labor unrest, industrial accidents, worker alienation"),
            "Sickles": ("Agricultural Collective", "harvest, rural cooperation, food security, peasant wisdom", 
                       "crop failure, rural reaction, kulak resistance"),
            "Red Stars": ("Military Defense", "protection of revolution, international solidarity, struggle", 
                         "militarism, aggressive war, loss of defensive spirit"),
            "Wheat Sheaves": ("Material Abundance", "socialist prosperity, equal distribution, planned economy", 
                             "scarcity, hoarding, economic mismanagement")
        }
        
        for suit, (english_suit, theme, rev_theme) in suits_data.items():
            # Ace
            cards.append(SovietTarotCard(
                "Ace", suit, 
                f"Pure essence of {theme.split(',')[0]}, new socialist beginning",
                f"Blocked potential, {rev_theme}",
                f"The Revolutionary Seed", 
                f"The pure potential of {english_suit.lower()} in service of the people"
            ))
            
            # Numbers 2-10
            for i in range(2, 11):
                cards.append(SovietTarotCard(
                    str(i), suit,
                    f"Development of {theme}, collective progress",
                    f"Setbacks in {theme}, {rev_theme}",
                    f"The {i} Comrades",
                    f"Collective development in {english_suit.lower()}"
                ))
            
            # Court cards
            court_soviet = {
                "Page": ("Young Pioneer", "enthusiasm for socialist learning", "misdirected youth energy"),
                "Knight": ("Shock Worker", "heroic labor achievements", "reckless overproduction"),
                "Queen": ("Brigade Leader", "maternal guidance of collective", "authoritarian management"),
                "King": ("Factory Director", "masterful economic leadership", "bureaucratic disconnection")
            }
            
            for court, (soviet_title, court_up, court_rev) in court_soviet.items():
                cards.append(SovietTarotCard(
                    court, suit,
                    f"{court_up}, {theme}",
                    f"{court_rev}, {rev_theme}",
                    soviet_title,
                    f"Leadership role in {english_suit.lower()}"
                ))
        
        return cards
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self) -> Tuple[SovietTarotCard, bool]:
        if not self.cards:
            self.cards = self._create_soviet_deck()
            self.shuffle()
        
        card = self.cards.pop()
        is_reversed = random.choice([True, False])
        return card, is_reversed

class SovietTarotGUI:
    def __init__(self, root):
        self.root = root
        self.deck = SovietTarotDeck()
        self.setup_window()
        self.setup_widgets()
        
    def setup_window(self):
        self.root.title("☭ ГОСУДАРСТВЕННАЯ СИСТЕМА ТАРО ☭ (State Tarot System)")
        self.root.geometry("1400x900")
        self.root.configure(bg='#001100')
        
        # Soviet color scheme: dark green background, bright green text
        self.colors = {
            'bg': '#001100',
            'fg': '#00FF00', 
            'button_bg': '#003300',
            'button_fg': '#00FF00',
            'text_bg': '#002200',
            'text_fg': '#00FF00',
            'red': '#FF0000'
        }
        
    def setup_widgets(self):
        # Main title with Soviet flair - across top
        title_frame = tk.Frame(self.root, bg=self.colors['bg'])
        title_frame.pack(fill=tk.X, pady=10)
        
        title = tk.Label(title_frame, 
                        text="☭ ГОСУДАРСТВЕННАЯ СИСТЕМА ТАРО ☭\n"
                             "STATE BUREAU OF MYSTICAL AFFAIRS - Scientific Prediction of Socialist Future",
                        bg=self.colors['bg'], fg=self.colors['red'],
                        font=('Courier New', 14, 'bold'),
                        justify=tk.CENTER)
        title.pack()
        
        # Propaganda subtitle
        subtitle = tk.Label(title_frame,
                           text="★ Serving the Dialectical Needs of the Proletariat Since 1917 ★",
                           bg=self.colors['bg'], fg=self.colors['fg'],
                           font=('Courier New', 9, 'italic'))
        subtitle.pack(pady=2)
        
        # Main content frame - split left/right
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # LEFT SIDE: Control Panel
        control_frame = tk.Frame(main_frame, bg=self.colors['bg'], width=350)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        control_frame.pack_propagate(False)  # Maintain fixed width
        
        # Control panel title
        control_title = tk.Label(control_frame,
                                text="═══ CONTROL TERMINAL ═══\n⚡ ДИАЛЕКТИЧЕСКИЙ БЛОК ⚡",
                                bg=self.colors['bg'], fg=self.colors['red'],
                                font=('Courier New', 11, 'bold'),
                                justify=tk.CENTER)
        control_title.pack(pady=10)
        
        # Soviet-themed buttons - more compact
        buttons = [
            ("🌟 SINGLE CARD\nANALYSIS", self.single_reading),
            ("⚒️ THREE CARD\nDIALECTIC", self.three_reading), 
            ("☭ FULL CENTRAL\nCOMMITTEE", self.celtic_reading),
            ("🔄 SHUFFLE DECK\nFOR MOTHERLAND", self.shuffle_deck),
            ("📋 PARTY CARD\nMEANINGS", self.show_meanings),
            ("⚡ EMERGENCY\nCAPITALIST SCAN", self.emergency_reading)
        ]
        
        for text, command in buttons:
            btn = tk.Button(control_frame, text=text,
                           command=command,
                           bg=self.colors['button_bg'], 
                           fg=self.colors['button_fg'],
                           font=('Courier New', 10, 'bold'),
                           width=25, height=3,
                           relief='raised', bd=3,
                           wraplength=200)
            btn.pack(pady=4, padx=10, fill=tk.X)
        
        # Status display in control panel
        status_frame = tk.Frame(control_frame, bg=self.colors['bg'])
        status_frame.pack(pady=15, fill=tk.X)
        
        status_title = tk.Label(status_frame,
                               text="═══ SYSTEM STATUS ═══",
                               bg=self.colors['bg'], fg=self.colors['red'],
                               font=('Courier New', 10, 'bold'))
        status_title.pack()
        
        self.status_label = tk.Label(status_frame,
                                    text="★ SYSTEM READY ★\nAWAITING COMRADE\nINSTRUCTIONS",
                                    bg=self.colors['bg'], fg=self.colors['fg'],
                                    font=('Courier New', 9),
                                    justify=tk.CENTER)
        self.status_label.pack(pady=5)
        
        # Party propaganda at bottom of control panel
        propaganda = tk.Label(control_frame,
                             text="WORKERS OF THE\nWORLD, UNITE!\n\n"
                                  "\"The future belongs\nto those who believe\nin the beauty of\ntheir dreams.\"\n- Eleanor Roosevelt\n(Modified for Socialist Use)",
                             bg=self.colors['bg'], fg=self.colors['fg'],
                             font=('Courier New', 8, 'italic'),
                             justify=tk.CENTER)
        propaganda.pack(side=tk.BOTTOM, pady=10)
        
        # RIGHT SIDE: Large Results Display
        results_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        results_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Results title
        results_title = tk.Label(results_frame,
                                text="═══════════════ ГЛАВНЫЙ ДИСПЛЕЙ ═══════════════\n"
                                     "MAIN ANALYSIS DISPLAY TERMINAL",
                                bg=self.colors['bg'], fg=self.colors['red'],
                                font=('Courier New', 11, 'bold'),
                                justify=tk.CENTER)
        results_title.pack(pady=5)
        
        # Large results display area
        self.results_text = scrolledtext.ScrolledText(results_frame,
                                                     width=85, height=40,
                                                     bg=self.colors['text_bg'],
                                                     fg=self.colors['text_fg'],
                                                     font=('Courier New', 10),
                                                     insertbackground=self.colors['fg'],
                                                     wrap=tk.WORD)
        self.results_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Initial welcome message
        self.show_welcome()
        
    def show_welcome(self):
        welcome = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    ☭ WELCOME TO THE STATE TAROT SYSTEM ☭                   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  ATTENTION COMRADES:                                                         ║
║                                                                              ║
║  This scientifically advanced mystical apparatus has been developed by      ║
║  the Central Committee's Department of Dialectical Divination to serve      ║
║  the fortune-telling needs of the proletariat.                              ║
║                                                                              ║
║  All readings are performed in accordance with Marxist-Leninist            ║
║  principles and are guaranteed to reveal the scientifically inevitable      ║
║  triumph of socialism.                                                       ║
║                                                                              ║
║  WARNING: Bourgeois interpretations of card meanings are strictly           ║
║  prohibited and will result in immediate referral to ideological           ║
║  re-education facilities.                                                   ║
║                                                                              ║
║  ★ FOR THE GLORY OF THE SOVIET UNION ★                                     ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

>>> Please select your desired method of socialist divination from the menu above.
>>> The State Bureau of Mystical Affairs is standing by to serve you, comrade!

"""
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, welcome)
        
    def update_status(self, message):
        self.status_label.config(text=f"★ {message[:15]} ★\n{message[15:30]}\n{message[30:45] if len(message) > 30 else ''}")
        self.root.update()
        
    def simulate_processing(self, messages):
        """Simulate Soviet computer processing with delays"""
        self.results_text.delete(1.0, tk.END)
        
        for message in messages:
            self.update_status(message)
            self.results_text.insert(tk.END, f">>> {message}...\n")
            self.root.update()
            time.sleep(0.8)
        
    def single_reading(self):
        self.simulate_processing([
            "INITIALIZING DIALECTICAL ANALYSIS MODULE",
            "CONSULTING CENTRAL PLANNING COMMITTEE",
            "APPLYING MARXIST-LENINIST INTERPRETATION PROTOCOLS",
            "READING COMPLETE - DISPLAYING RESULTS"
        ])
        
        card, is_reversed = self.deck.draw_card()
        orientation = "COUNTER-REVOLUTIONARY (Reversed)" if is_reversed else "REVOLUTIONARY (Upright)"
        meaning = card.reversed_meaning if is_reversed else card.upright_meaning
        
        result = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                        🌟 SINGLE CARD ANALYSIS 🌟                          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  DRAWN CARD: {card.get_soviet_name():<58} ║
║  ORIENTATION: {orientation:<56} ║
║                                                                              ║
║  OFFICIAL PARTY INTERPRETATION:                                              ║
║  {meaning:<76} ║
║                                                                              ║
║  SYMBOLIC MEANING:                                                           ║
║  {card.soviet_symbolism:<76} ║
║                                                                              ║
║  ★ This reading has been approved by the Committee for Mystical Affairs ★  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        self.results_text.insert(tk.END, result)
        self.update_status("ANALYSIS COMPLETE - GLORY TO THE UNION")
        
    def three_reading(self):
        self.simulate_processing([
            "ACTIVATING THREE-STAGE DIALECTICAL ENGINE",
            "CONSULTING HISTORICAL MATERIALISM DATABASE",
            "ANALYZING PAST-PRESENT-FUTURE SOCIALIST DEVELOPMENT",
            "TRIANGULATION COMPLETE"
        ])
        
        cards = [self.deck.draw_card() for _ in range(3)]
        positions = ["HISTORICAL FOUNDATION", "CURRENT CLASS STRUGGLE", "INEVITABLE COMMUNIST FUTURE"]
        
        result = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                     ⚒️ THREE CARD DIALECTICAL ANALYSIS ⚒️                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
"""
        
        for i, (card, is_reversed) in enumerate(cards):
            orientation = "Counter-Rev." if is_reversed else "Revolutionary"
            meaning = card.reversed_meaning if is_reversed else card.upright_meaning
            
            result += f"""║  {positions[i]}:                                        ║
║    Card: {card.get_soviet_name():<59} ║
║    Status: {orientation:<57} ║
║    Meaning: {meaning[:65]:<65} ║
║             {meaning[65:130] if len(meaning) > 65 else "":<65} ║
║                                                                              ║
"""
        
        result += """║  ★ The dialectical progression toward socialism is confirmed ★             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        
        self.results_text.insert(tk.END, result)
        self.update_status("DIALECTICAL ANALYSIS COMPLETE")
        
    def celtic_reading(self):
        self.simulate_processing([
            "CONVENING EMERGENCY SESSION OF POLITBURO",
            "DEPLOYING ALL AVAILABLE MYSTICAL RESOURCES", 
            "ANALYZING COMPLEX SOCIO-ECONOMIC FACTORS",
            "CONSULTING LENIN'S COLLECTED WORKS",
            "CROSS-REFERENCING WITH FIVE-YEAR PLANS",
            "GENERATING COMPREHENSIVE REPORT"
        ])
        
        cards = [self.deck.draw_card() for _ in range(10)]
        positions = [
            "Current State of Revolution",
            "Bourgeois Obstacles", 
            "Historical Material Base",
            "Recent Class Developments",
            "Potential Socialist Outcome",
            "Immediate Tactical Situation",
            "Your Role in the Struggle",
            "International Solidarity",
            "Hopes of the Proletariat",
            "Final Victory of Communism"
        ]
        
        result = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                ☭ FULL CENTRAL COMMITTEE CONSULTATION ☭                     ║
║                      (Complete Revolutionary Analysis)                       ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
"""
        
        for i, (card, is_reversed) in enumerate(cards):
            orientation = "⚡" if is_reversed else "★"
            meaning = card.reversed_meaning if is_reversed else card.upright_meaning
            
            result += f"""║ {i+1:2d}. {positions[i]:<40} {orientation} ║
║     {card.get_soviet_name():<70} ║
║     {meaning[:70]:<70} ║
║                                                                              ║
"""
        
        result += """║                                                                              ║
║  ★★★ FINAL JUDGMENT OF THE CENTRAL COMMITTEE ★★★                          ║
║                                                                              ║
║  The scientific analysis reveals that the forces of history are            ║
║  inexorably moving toward the establishment of a classless society.        ║
║  The proletariat must remain vigilant against bourgeois deviation          ║
║  and maintain revolutionary discipline in all endeavors.                    ║
║                                                                              ║
║  CONCLUSION: SOCIALISM WILL TRIUMPH! WORKERS OF THE WORLD, UNITE!          ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        
        self.results_text.insert(tk.END, result)
        self.update_status("COMPLETE ANALYSIS DELIVERED - VICTORY ASSURED")
        
    def shuffle_deck(self):
        self.simulate_processing([
            "REDISTRIBUTING CARDS ACCORDING TO SOCIALIST PRINCIPLES",
            "ENSURING EQUAL OPPORTUNITY FOR ALL CARD POSITIONS",
            "ELIMINATING BOURGEOIS CARD PRIVILEGE"
        ])
        
        self.deck.shuffle()
        
        shuffle_msg = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                           🔄 DECK REDISTRIBUTED 🔄                          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  The tarot deck has been scientifically reorganized according to           ║
║  principles of dialectical materialism. All cards now have equal           ║
║  opportunity to serve the revolutionary cause.                              ║
║                                                                              ║
║  No card exploitation detected. Bourgeois randomness eliminated.            ║
║                                                                              ║
║  ★ The deck is now ready to serve the people! ★                           ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        self.results_text.insert(tk.END, shuffle_msg)
        self.update_status("DECK SUCCESSFULLY COLLECTIVIZED")
        
    def emergency_reading(self):
        """Special emergency reading for detecting capitalist influences"""
        self.simulate_processing([
            "🚨 ACTIVATING EMERGENCY PROTOCOLS 🚨",
            "SCANNING FOR COUNTER-REVOLUTIONARY ACTIVITY",
            "ANALYZING BOURGEOIS INFILTRATION PATTERNS",
            "DEPLOYING IDEOLOGICAL COUNTERMEASURES"
        ])
        
        # Draw a random card but give it special "emergency" interpretation
        card, is_reversed = self.deck.draw_card()
        
        # Generate silly emergency assessment
        threats = [
            "MINIMAL - Continue normal socialist activities",
            "MODERATE - Increase vigilance against petit-bourgeois tendencies", 
            "ELEVATED - Report suspicious individualistic behavior",
            "HIGH - Bourgeois elements detected in vicinity",
            "CRITICAL - Immediate ideological reinforcement required"
        ]
        
        threat_level = random.choice(threats)
        
        emergency_msg = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                      🚨 EMERGENCY THREAT ASSESSMENT 🚨                      ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  DETECTION CARD: {card.get_soviet_name():<54} ║
║  THREAT LEVEL: {threat_level:<59} ║
║                                                                              ║
║  RECOMMENDED ACTION:                                                         ║
║  - Increase consumption of state-approved literature                        ║
║  - Report any dreams of private property ownership                          ║
║  - Sing "The Internationale" at least twice daily                          ║
║  - Maintain constant vigilance against Western propaganda                   ║
║                                                                              ║
║  Remember comrade: The price of socialism is eternal vigilance!            ║
║                                                                              ║
║  ★ This assessment is certified by the Department of Internal Security ★   ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        
        self.results_text.insert(tk.END, emergency_msg)
        self.update_status("EMERGENCY ASSESSMENT COMPLETE - REMAIN VIGILANT")
        
    def show_meanings(self):
        """Display the party-approved card meanings"""
        self.update_status("ACCESSING CLASSIFIED CARD MEANINGS DATABASE")
        
        meanings_text = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    📋 PARTY-APPROVED CARD MEANINGS 📋                       ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  CLASSIFICATION LEVEL: RESTRICTED                                            ║
║  ACCESS AUTHORIZED FOR: Active Party Members Only                           ║
║                                                                              ║
║  🌟 REVOLUTIONARY MAJOR ARCANA:                                             ║
║                                                                              ║
║  The Young Pioneer (Fool) - Revolutionary enthusiasm, new socialist path    ║
║  The Party Secretary (Magician) - Organizational power, leading masses     ║  
║  The Babushka Oracle (High Priestess) - Traditional wisdom, Soviet insight ║
║  Mother Russia (Empress) - Abundant motherland, nurturing collective       ║
║  The Chairman (Emperor) - Strong leadership, planned economy structure      ║
║  The Ideological Instructor (Hierophant) - Orthodox teaching, party line   ║
║  The Collective Marriage (Lovers) - Unity of purpose, socialist love       ║
║  The Five Year Plan (Chariot) - Economic progress, triumphant advance      ║
║  The Woman Tractor Driver (Strength) - Proletariat power, gentle guidance  ║
║  The Siberian Exile (Hermit) - Revolutionary reflection, earned wisdom     ║
║                                                                              ║
║  ⚒️ PROLETARIAN MINOR ARCANA:                                              ║
║                                                                              ║
║  Hammers (Industrial Labor) - Worker solidarity, industrial production     ║
║  Sickles (Agricultural Collective) - Rural cooperation, peasant wisdom     ║
║  Red Stars (Military Defense) - Protection of revolution, struggle         ║
║  Wheat Sheaves (Material Abundance) - Socialist prosperity, equal sharing  ║
║                                                                              ║
║  ★ Remember: All interpretations must align with current party doctrine ★  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

WARNING: Unauthorized interpretation of these sacred socialist symbols 
may result in immediate referral to the Committee for Ideological Purity.

For complete meanings, consult your local Political Officer or 
the nearest Bureau of Mystical Affairs field office.

>>> End of classified document <<<
"""
        
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, meanings_text)
        self.update_status("CLASSIFIED MATERIALS DISPLAYED - MAINTAIN SECURITY")

def main():
    root = tk.Tk()
    app = SovietTarotGUI(root)
    
    # Add some final Soviet touches
    try:
        # Try to set window icon (won't work but shows the spirit!)
        root.iconbitmap("hammer_and_sickle.ico")
    except:
        pass
    
    root.mainloop()

if __name__ == "__main__":
    main()