from datetime import datetime
import pandas as pd


def listRecentDeaths(individuals, days=30):
    recent_deaths = []
    current_date = datetime.now()

    for index, row in individuals.iterrows():
        # Check if the death_date is available in the data
        if not pd.isnull(row['DEATH']):
            # Parse the death_date
            death_date = datetime.strptime(row['DEATH'], "%d %b %Y")
            # Calculate the number of days between death_date and current date
            days_since_death = (current_date - death_date).days

            if days_since_death <= days:
                # If the condition is met, add the individual's ID, death_date, and name to the recent_deaths list
                recent_deaths.append((row['ID'], row['DEATH'], row['NAME']))

    if len(recent_deaths) > 0:

        return f"US36: List of Recent Deaths in the (last', {days}, 'days): {recent_deaths}"
    else:
        return f"US36: No recent deaths found in the last {days} days."
