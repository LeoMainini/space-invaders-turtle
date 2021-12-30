from turtle import Turtle


class Scoreboard:

    def __init__(self, score, lives) -> None:
        self.lives = lives
        self.score = score
        self.display = {}
        self.positions = [(-380, -250), (380, -250)]
        for i in range(2):
            turtle = Turtle()
            turtle.type = "scoreboard"
            turtle.hideturtle()
            turtle.color("white")
            turtle.penup()
            turtle.setpos(self.positions[i])
            if self.positions[i][0] > 0:
                turtle.write(f"Score: {self.score}", move=True,
                             align="right", font=('Arial', 16, 'bold'))
                self.display['score'] = turtle
            else:
                turtle.write(f"Lives: {self.lives}", move=False,
                             align="left", font=('Arial', 16, 'normal'))
                self.display['lives'] = turtle

    def write(self):
        score = self.display['score']
        lives = self.display['lives']
        score.clear()
        score.setpos(self.positions[1])
        score.write(f"Score: {self.score}", move=True,
                    align="right", font=('Arial', 16, 'bold'))
        lives.clear()
        lives.setpos(self.positions[0])
        lives.write(f"Lives: {self.lives}", move=False,
                    align="left", font=('Arial', 16, 'normal'))

    def update_sb(self, score, lives):
        self.lives = lives
        self.score = score
        self.write()

    def game_over(self, timedelta):
        for key in self.display.keys():
            self.display[key].clear()
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.color("white")
        game_over.setpos(0, 0)
        if self.lives > 0:
            game_over.write("YOU WON", align="center",
                            font=('Arial', 24, 'normal'))
        else:
            game_over.write("GAME OVER", align="center",
                            font=('Arial', 24, 'normal'))
        game_over.setpos(0, -75)
        final_score = round((self.score + self.lives*50)*(60/timedelta))
        game_over.write(f"final score: {final_score} in {timedelta} seconds.\nClick anywhere to exit.", align="center", font=(
            'Arial', 14, 'normal'))
