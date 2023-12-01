# Pet Adoption Trends in Austin, Texas: Impact & Analysis

## Data:
1. Introduction: The data is collected and provided by the [City of Austin, Texas](https://data.austintexas.gov/), spanning from October 1st, 2013, to the present day (updated daily). These datasets track the journey of animals from intake to eventual adoption, including those still awaiting adoption.
2. Source: [Austin Animal Center Intakes](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Intakes/wter-evkm), [Austin Animal Center Outcomes](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes/9t4d-g238)
3. Description:

**Austin Animal Center Intake:**

| Column Name        | Description                   | Data Type            |
|--------------------|-------------------------------|:---------------------|
| `animal_id`        | ID of Animal                  | text                 |
| `name`             | name of Animal                | text                 |
| `datetime`         | intake datetime               | floating timestamp   |
| `datetime2`        | intake month & year           | floating timestamp   |
| `found_location`   | location the animal was found | text                 |
| `date_of_birth`    | date of birth of animal       | floating timestamp   |
| `intake_type`      | intake type of animal         | text                 |
| `intake_condition` | condition upon intake         | text                 |
| `animal_type`      | type of animal                | text                 |
| `sex_upon_intake`  | sex of animal                 | text                 |
| `age_upon_intake`  | age upon outcome of animal    | text                 |
| `breed`            | breed of animal               | text                 |
| `color`            | color of animal               | text                 |


**Austin Animal Center Outcomes:**

| Column Name        | Description                      | Data Type            |
|--------------------|----------------------------------|----------------------|
| `animal_id`        | ID of Animal                     | text                 |
| `name`             | name of Animal                   | text                 |
| `datetime`         | outcome datetime                 | floating timestamp   |
| `monthyear`        | outcome month & year             | floating timestamp   |
| `date_of_birth`    | date of birth of animal          | floating timestamp   |
| `outcome_type`     | outcome type of animal           | text                 |
| `outcome_subtype`  | outcome subtype of animal        | text                 |
| `animal_type`      | type of animal                   | text                 |
| `sex_upon_outcome` | sex of animal                    | text                 |
| `age_upon_outcome` | age upon outcome of animal       | text                 |
| `breed`            | breed of animal                  | text                 |
| `color`            | color of animal                  | text                 |