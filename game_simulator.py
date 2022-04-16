# A simulation ground - the game is played for 2000 times, and the data is collected.

from game_show import *
import pandas as pd
from sqlalchemy import create_engine


def simulate(num_games: int) -> pd.DataFrame:
    # Initialize the data frame
    game_data = play(1, 3, interactive=False)
    game_df = pd.DataFrame([game_data])
    for _ in range(1, num_games):
        game_data = play(1, 3, interactive=False)
        new_df = pd.DataFrame([game_data])
        game_df = pd.concat([game_df, new_df], ignore_index=True)

    return game_df

def write_to_sql(df: pd.DataFrame) -> None:
    engine = create_engine("sqlite://", echo=False)
    df.to_sql("game_data", con=engine)
    # df2 = pd.read_sql("SELECT * FROM game_data;", engine)
    # print(df2)

def write_to_csv(df: pd.DataFrame) -> None:
    df.to_csv("game_data.csv", index=True)


if __name__ == "__main__":
    df = simulate(100)
    # write_to_sql(df)
    write_to_csv(df)
