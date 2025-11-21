# Gratta e Vinci Script 🎰

---

## 🇬🇧 🇺🇸 English

### What Does This Code Do?

This is an **interactive Scratch Card game** built in Python that simulates the Italian "Gratta e Vinci" lottery experience. The script provides a fun, text-based game where players can scratch virtual cards and win prizes.

### Features

- **Player Name Input**: The game collects the player's name for personalization
- **Random Prize Generation**: Uses weighted probability distribution to determine prizes:
  - 20% chance to win 150 coins
  - 10% chance to win 350 coins
  - 5% chance to win 700 coins
  - 65% chance to win nothing
  
- **Animated ASCII Art**: Beautiful card visualization with step-by-step animation effects that simulate the scratching process
  - Displays a covered scratch card before revealing
  - Creates an animated "scratching" effect with delays
  - Reveals the prize with celebratory ASCII art

- **Game Statistics**: Shows a summary with the player's name and total prize amount

- **Replay Feature**: Players can choose to play multiple times in the same session

- **Bilingual Interface**: Full support for both English and Italian

- **Error Handling**: Gracefully handles invalid inputs and keyboard interruptions (Ctrl+C)

### How It Works

1. The script prompts for the player's name
2. A random prize is generated based on the probability distribution
3. An ASCII art scratch card is displayed with animation
4. The player presses Enter to "scratch" the card
5. The prize is revealed with visual effects
6. Game statistics are displayed
7. Player can choose to play again or exit

### Code Structure

- **`get_participant_name()`**: Collects player name with validation
- **`generate_prize()`**: Generates random prize using weighted selection
- **`display_scratch_card()`**: Shows animated ASCII art card with scratching effect
- **`display_statistics()`**: Displays game results summary
- **`main()`**: Orchestrates the entire game flow and handles replay logic

### Requirements

- Python 3.6+
- No external dependencies required (uses only standard library)

### How to Run

```bash
python gratta_e_vinci.py
```

Then follow the on-screen prompts to play!

---

## 🇮🇹 Italiano

### Cosa Fa Questo Codice?

Questo è un **gioco interattivo di Gratta e Vinci** creato in Python che simula l'esperienza della lotteria "Gratta e Vinci" italiana. Lo script fornisce un gioco divertente basato su testo dove i giocatori possono grattare carte virtuali e vincere premi.

### Caratteristiche

- **Input del Nome del Giocatore**: Il gioco raccoglie il nome del giocatore per la personalizzazione
- **Generazione di Premi Casuali**: Utilizza una distribuzione di probabilità ponderata per determinare i premi:
  - 20% di probabilità di vincere 150 monete
  - 10% di probabilità di vincere 350 monete
  - 5% di probabilità di vincere 700 monete
  - 65% di probabilità di non vincere nulla
  
- **ASCII Art Animata**: Bellissima visualizzazione della carta con effetti di animazione passo dopo passo che simulano il processo di grattamento
  - Visualizza una carta gratta e vinci coperta prima della rivelazione
  - Crea un effetto di "grattamento" animato con ritardi
  - Rivela il premio con ASCII art celebrativo

- **Statistiche di Gioco**: Mostra un riepilogo con il nome del giocatore e l'importo totale dei premi

- **Funzione di Replay**: I giocatori possono scegliere di giocare più volte nella stessa sessione

- **Interfaccia Bilingue**: Supporto completo sia per l'inglese che per l'italiano

- **Gestione degli Errori**: Gestisce con eleganza gli input non validi e le interruzioni da tastiera (Ctrl+C)

### Come Funziona

1. Lo script richiede il nome del giocatore
2. Un premio casuale viene generato in base alla distribuzione di probabilità
3. Una carta gratta e vinci in ASCII art viene visualizzata con animazione
4. Il giocatore preme Invio per "grattare" la carta
5. Il premio viene rivelato con effetti visivi
6. Le statistiche del gioco vengono visualizzate
7. Il giocatore può scegliere di giocare di nuovo o uscire

### Struttura del Codice

- **`get_participant_name()`**: Raccoglie il nome del giocatore con validazione
- **`generate_prize()`**: Genera premio casuale usando la selezione ponderata
- **`display_scratch_card()`**: Mostra la carta ASCII art animata con effetto di grattamento
- **`display_statistics()`**: Visualizza il riepilogo dei risultati di gioco
- **`main()`**: Orchestra l'intero flusso del gioco e gestisce la logica di replay

### Requisiti

- Python 3.6+
- Nessuna dipendenza esterna richiesta (utilizza solo la libreria standard)

### Come Eseguire

```bash
python gratta_e_vinci.py
```

Quindi segui i prompt sullo schermo per giocare!

---

**Enjoy the game! / Divertiti a giocare! 🎮**
