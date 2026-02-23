import customtkinter as ctk
import Game.game
"""
Problème rencontré:
L'idée de départ était de faire des boutons cliquables par dessus la grille de jeu avec un bouton par colonne, pour
pouvoir récupérer l'action du joueur mais il aurait fallu que les boutons soient invisibles/transparents or l'attribut
transparent pour la couleur applique la couleur du parent ce qui rendait le bouton noir sur la grille plutôt que 
réellement transparent. Il a donc fallu repenser l'architecture en créant des canvas dans des frames auxquels nous
ajouterons des évènements pour récupérer nos informations.
"""
class Display(ctk.CTk):

    CELL_SIZE = 80
    PADDING = 2
    BOARD_COLOR = "#1a6fc4"

    def __init__(self, game: Game.game.Game):
        super().__init__()
        self.game = game

        self.title("Puissance 4")
        ctk.set_appearance_mode("dark")
        self.resizable(False, False)

        # Frame principale contenant la grille
        self.grid_frame = ctk.CTkFrame(self)
        self.grid_frame.pack(padx=20, pady=20)

        # Stockage des canvases (jetons et carrés les contenant)
        self.cells = []

        self._create_grid()
        self.after(1000, self.refresh)

    def _create_grid(self):
        rows = len(self.game.get_board())
        cols = len(self.game.get_board()[0])

        for i in range(rows):
            row_cells = []
            for j in range(cols):
                # Frame de la cellule (fond bleu et bordure blanche)
                cell = ctk.CTkFrame(
                    self.grid_frame,
                    width=self.CELL_SIZE,
                    height=self.CELL_SIZE,
                    fg_color=self.BOARD_COLOR,
                    border_color="white",
                    border_width=2,
                    corner_radius=0
                )
                cell.grid(row=i, column=j, padx=self.PADDING, pady=self.PADDING)
                cell.grid_propagate(False)

                # Canvas du jeton centré dans la cellule (case carrée contenant le jeton)
                canvas = ctk.CTkCanvas(
                    cell,
                    width=self.CELL_SIZE - 10,
                    height=self.CELL_SIZE - 10,
                    bg=self.BOARD_COLOR,
                    highlightthickness=0
                )
                canvas.place(relx=0.5, rely=0.5, anchor="center")

                # Dessin du jeton initial
                color = self._get_color(self.game.get_board()[i][j])
                canvas.create_oval(
                    5, 5,
                    self.CELL_SIZE - 15, self.CELL_SIZE - 15,
                    fill=color,
                    outline="",
                    tags="token"
                )

                row_cells.append(canvas)
            self.cells.append(row_cells)

    def refresh(self):
        for i in range(len(self.game.get_board())):
            for j in range(len(self.game.get_board()[0])):
                value = self.game.get_board()[i][j]
                color = self._get_color(value)
                # On supprime l'ancien jeton et on en refait un
                self.cells[i][j].delete("token")
                self.cells[i][j].create_oval(
                    5, 5,
                    self.CELL_SIZE - 15, self.CELL_SIZE - 15,
                    fill=color,
                    outline="",
                    tags="token"
                )

    def _get_color(self, value):
        colors = {
            0: "#0d3b6e",  # case vide (bleu foncé)
            1: "red",
            2: "yellow"
        }
        return colors.get(value, "white")


if __name__ == "__main__":
    jeu = Game.game.Game()
    display = Display(jeu)
    # display.mainloop()
    jeu.do_action(0,1)
    display.refresh()
    display.mainloop()