import customtkinter as ctk
import Game.game


class Display(ctk.CTk):

    CELL_SIZE = 60

    def __init__(self, game: Game.game.Game):
        super().__init__()
        self.game = game

        self.title("Puissance 4")
        self.geometry("600x500")

        ctk.set_appearance_mode("dark")

        # Frame principale contenant la grille
        self.grid_frame = ctk.CTkFrame(self)
        self.grid_frame.pack(padx=20, pady=20)

        # Stockage des cellules
        self.cells = []

        self._create_grid()


    def _create_grid(self):
        rows = len(self.game.get_board())
        cols = len(self.game.get_board()[0])

        for i in range(rows):
            row_cells = []
            for j in range(cols):

                cell = ctk.CTkFrame(
                    self.grid_frame,
                    width=self.CELL_SIZE,
                    height=self.CELL_SIZE,
                    corner_radius=0,
                    fg_color=self._get_color(self.game.get_board()[i][j])
                )

                cell.grid(row=i, column=j, padx=2, pady=2)
                cell.grid_propagate(False)

                row_cells.append(cell)

            self.cells.append(row_cells)



    def refresh(self):
        for i in range(len(self.game.get_board())):
            for j in range(len(self.game.get_board()[0])):
                value = self.game.get_board()[i][j]
                self.cells[i][j].configure(
                    fg_color=self._get_color(value)
                )


    def _get_color(self, value):
        colors = {
            0: "gray20",
            1: "red",
            2: "yellow"
        }
        return colors.get(value, "white") #Renvoie blanc par défaut si une valeur ne correspond pas

jeu=Game.game.Game()
display = Display(jeu)
# display.mainloop()
jeu.do_action(0,1)
display.refresh()
display.mainloop()