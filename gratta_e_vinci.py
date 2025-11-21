#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gratta e Vinci Script / Scratch Card Script
============================================
A simple interactive scratch card game with ASCII art visualization
Un semplice gioco di gratta e vinci interattivo con visualizzazione ASCII art
"""

import random
import time

# ============================================================================
# CONFIGURATION / CONFIGURAZIONE
# ============================================================================

# Probability distribution for prize winnings / Distribuzione probabilità
PRIZE_PROBABILITIES = {
    "150_coins": 0.10,  # 10% chance for 150 coins / 10% probabilità 150 monete
    "350_coins": 0.05,  # 5% chance for 350 coins / 5% probabilità 350 monete
    "700_coins": 0.025,  # 2.5% chance for 700 coins / 2.5% probabilità 700 monete
    "no_prize": 0.825,   # 82.5% chance for no prize / 82.5% probabilità nessun premio
}

# Prize values mapping / Mappatura valori premi
PRIZE_VALUES = {
    "150_coins": 150,
    "350_coins": 350,
    "700_coins": 700,
    "no_prize": 0,
}

# ============================================================================
# FUNCTIONS / FUNZIONI
# ============================================================================

def get_participant_name():
    """
    Get the participant name from user input.
    Collects the player's name for personalization.
    
    Ottiene il nome del partecipante dall'input dell'utente.
    Raccoglie il nome del giocatore per la personalizzazione.
    
    Returns:
        str: The participant's name
        str: Il nome del partecipante
    """
    print("\n" + "=" * 60)
    print("  BENVENUTO AL GRATTA E VINCI - WELCOME TO SCRATCH CARD GAME")
    print("=" * 60 + "\n")
    
    name = input("Inserisci il tuo nome (Enter your name): ").strip()
    
    # Validate input / Valida input
    if not name:
        name = "Giocatore Misterioso / Mystery Player"
        print(f"❌ Nome non valido! Usa il nome generico: {name}")
        print(f"❌ Invalid name! Using generic name: {name}")
    
    return name


def generate_prize():
    """
    Generate a random prize based on defined probabilities.
    Uses weighted random selection for fair prize distribution.
    
    Genera un premio casuale in base alle probabilità definite.
    Utilizza una selezione casuale ponderata per una distribuzione equa dei premi.
    
    Returns:
        str: The prize key (e.g., "150_coins", "700_coins", "no_prize")
        str: La chiave del premio (es. "150_coins", "700_coins", "no_prize")
    """
    # Prepare lists for random.choices / Prepara liste per random.choices
    prizes = list(PRIZE_PROBABILITIES.keys())
    probabilities = list(PRIZE_PROBABILITIES.values())
    
    # Select a prize based on probabilities / Seleziona un premio in base alle probabilità
    selected_prize = random.choices(prizes, weights=probabilities, k=1)[0]
    
    return selected_prize


def display_scratch_card(participant_name, prize):
    """
    Display an animated ASCII art scratch card that is revealed step by step.
    Creates a visual effect of scratching to reveal the prize.
    
    Visualizza una carta gratta e vinci ASCII art animata rivelata passo dopo passo.
    Crea un effetto visivo di grattamento per rivelare il premio.
    
    Args:
        participant_name (str): Name of the participant / Nome del partecipante
        prize (str): The winning prize key / La chiave del premio vincente
    """
    prize_value = PRIZE_VALUES[prize]
    
    # Covered card design (before scratching) / Design della carta coperta (prima del grattamento)
    covered_card = [
        "   ╔════════════════════════════════╗",
        "   ║                                ║",
        "   ║   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ║",
        "   ║   ▓▓▓▓▓ GRATTA E VINCI ▓▓▓▓▓   ║",
        "   ║   ▓▓▓▓▓  SCRATCH CARD  ▓▓▓▓▓   ║",
        "   ║   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ║",
        "   ║                                ║",
        "   ║     Gratta qui! / Scratch!     ║",
        "   ║                                ║",
        "   ╚════════════════════════════════╝",
    ]
    
    # Revealed card design (after scratching) / Design della carta scoperta (dopo il grattamento)
    revealed_card = [
        "   ╔════════════════════════════════╗",
        "   ║                                ║",
        f"   ║         {participant_name:^24} ║",
        "   ║                                ║",
        "   ║        🎉 CONGRATULAZIONI! 🎉  ║",
        "   ║       🎊  CONGRATULATIONS! 🎊  ║",
        "   ║                                ║",
    ]
    
    # Add prize information / Aggiungi informazioni del premio
    if prize_value == 0:
        revealed_card.append("   ║        ❌ NESSUN PREMIO ❌     ║")
        revealed_card.append("   ║           ❌ NO PRIZE ❌       ║")
    else:
        revealed_card.append(f"   ║     💰 HAI VINTO {prize_value} MONETE 💰 ║")
        revealed_card.append(f"   ║        💰 YOU WON {prize_value} COINS 💰 ║")
    
    revealed_card.extend([
        "   ║                                ║",
        "   ╚════════════════════════════════╝",
    ])
    
    # Display covered card / Visualizza carta coperta
    print("\n" + "─" * 40)
    print("  Ecco il tuo biglietto! / Here's your ticket!")
    print("─" * 40 + "\n")
    
    for line in covered_card:
        print(line)
        time.sleep(0.2)  # Animation delay / Ritardo animazione
    
    # Pause before revealing / Pausa prima della rivelazione
    print("\n⏳ Premi INVIO per grattare il biglietto...")
    print("⏳ Press ENTER to scratch the ticket...\n")
    input()
    
    # Clear screen effect / Effetto pulizia schermo
    print("\n" * 2)
    
    # Display revealed card with animation / Visualizza carta scoperta con animazione
    print("🎰 🎰 🎰 GRATTAMENTO IN CORSO... / SCRATCHING IN PROGRESS... 🎰 🎰 🎰\n")
    
    for line in revealed_card:
        print(line)
        time.sleep(0.15)  # Animation delay / Ritardo animazione
    
    # Final animation / Animazione finale
    time.sleep(1)
    print("\n" + "=" * 40)
    
    if prize_value == 0:
        print("   😢 GRAZIE PER AVER GIOCATO! / THANKS FOR PLAYING! 😢")
    else:
        print("   🎉 GRANDE VINCITA! / BIG WIN! 🎉")
    
    print("=" * 40 + "\n")


def display_statistics(participant_name, prize_value):
    """
    Display game statistics and results summary.
    Shows the player's name and final prize amount.
    
    Visualizza statistiche di gioco e riepilogo dei risultati.
    Mostra il nome del giocatore e l'importo del premio finale.
    
    Args:
        participant_name (str): Name of the participant / Nome del partecipante
        prize_value (int): The value of the prize won / Il valore del premio vinto
    """
    print("📊 RIEPILOGO DEL GIOCO / GAME SUMMARY 📊")
    print("─" * 40)
    print(f"Giocatore / Player: {participant_name}")
    print(f"Premio Totale / Total Prize: {prize_value} monete / coins")
    print("─" * 40 + "\n")


def main():
    """
    Main function - orchestrates the entire game flow.
    Coordinates all game functions and manages the game logic.
    
    Funzione principale - orchestra l'intero flusso del gioco.
    Coordina tutte le funzioni di gioco e gestisce la logica di gioco.
    """
    try:
        # Get participant name / Ottiene il nome del partecipante
        participant_name = get_participant_name()
        
        # Generate random prize / Genera premio casuale
        prize = generate_prize()
        
        # Display scratch card animation / Visualizza animazione gratta e vinci
        display_scratch_card(participant_name, prize)
        
        # Display game statistics / Visualizza statistiche di gioco
        prize_value = PRIZE_VALUES[prize]
        display_statistics(participant_name, prize_value)
        
        # Ask to play again / Chiedi di giocare di nuovo
        print("\n🎮 VUOI GIOCARE DI NUOVO? / WANT TO PLAY AGAIN? 🎮\n")
        while True:
            play_again = input("Sì (S) / No (N) - Yes (Y) / No (N): ").strip().upper()
            
            if play_again in ["S", "Y"]:
                # Recursive call to play again / Chiama ricorsivamente per giocare di nuovo
                print("\n" * 3)
                main()
                break
            elif play_again in ["N"]:
                print("\n👋 ARRIVEDERCI! / GOODBYE! 👋\n")
                break
            else:
                print("❌ Scelta non valida! / Invalid choice!")
                print("❌ Per favore digita S (Sì/Yes) o N (No): / Please type S (Yes) or N (No):\n")
    
    except KeyboardInterrupt:
        # Handle user interruption (Ctrl+C) / Gestisce interruzione dell'utente (Ctrl+C)
        print("\n\n⚠️  Gioco interrotto! / Game interrupted! ⚠️ \n")
        print("👋 Grazie per aver giocato! / Thanks for playing! 👋\n")


# ============================================================================
# SCRIPT ENTRY POINT / PUNTO DI INGRESSO DELLO SCRIPT
# ============================================================================

if __name__ == "__main__":
    # Ensures main() only runs when script is executed directly
    # Assicura che main() viene eseguito solo quando lo script viene eseguito direttamente
    main()
