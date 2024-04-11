import pandas as pd
import time
import os


def get_nba_pace(year):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}.html"

    # Read Advanced Table (3rd last table)
    table_number = -3
    if year < 1997:
        table_number = -1  # Shooting stats started tracking in 1997

    table = pd.read_html(url, header=1)[table_number]

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    table = table[['Team', 'Pace']]
    table['Team'] = table['Team'].str.replace('*', '')
    table.set_index('Team', inplace=True)
    table = table['Pace']

    table.to_json(os.path.join('data', f'{year}-pace.json'))
    return table


def main():
    for year in range(1980, 2025):
        print(get_nba_pace(year))

        # Sleep 6 seconds to avoid throttling
        time.sleep(6)


if __name__ == '__main__':
    main()