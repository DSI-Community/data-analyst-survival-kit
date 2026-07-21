import matplotlib.pyplot as plt
import pandas as pd
 
 
def scatter_preis_alter(df: pd.DataFrame, alter: str = "alter", preis: str = "preis"):
    """Zeichnet Preis gegen Alter und gibt (fig, ax) zurueck.
 
    Die Rueckgabe von fig und ax erlaubt es dem Aufrufer, den Plot
    weiter anzupassen oder zu speichern, statt ihn direkt anzuzeigen.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
 
    # alpha < 1, weil sich bei vielen Datenpunkten sonst Ueberlagerungen
    # verstecken und dichte Bereiche nicht als solche erkennbar sind
    ax.scatter(df[alter], df[preis], alpha=0.5, edgecolor="none")
 
    ax.set_xlabel("Alter (Jahre)")
    ax.set_ylabel("Preis (EUR)")
    ax.set_title("Preis vs. Alter")
    ax.grid(True, alpha=0.3)
 
    return fig, ax
 
 
if __name__ == "__main__":
    df = pd.read_csv("daten.csv")
 
    # Korrelation als Zahl neben dem visuellen Eindruck: der Plot zeigt die
    # Form des Zusammenhangs, der Koeffizient nur dessen lineare Staerke
    print(f"Korrelation Alter/Preis: {df['alter'].corr(df['preis']):.3f}")
 
    fig, ax = scatter_preis_alter(df)
    fig.savefig("assets/scatter_preis_alter.png", dpi=150, bbox_inches="tight")
    plt.show()
