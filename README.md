# Pet Adoption Trends in Austin, Texas: Impact & Analysis

## Data:
1. Introduction:
The data is collected and provided by the [City of Austin, Texas](https://data.austintexas.gov/), spanning from October 1st, 2013, to the present day (updated daily). These datasets track the journey of animals from intake to eventual adoption, including those still awaiting adoption.

2. Source:
[Austin Animal Center Intakes](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Intakes/wter-evkm), [Austin Animal Center Outcomes](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes/9t4d-g238)

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

## **Hypothesis**
### Hypothesis 1:
Is there a correlation between the neuter/spay rate of animals and their age?
 - $H0$: There is no significant relationship between neuter/spay rate and age in animals.
 - $H1$: There is a significant relationship between neuter/spay rate and age in animals.

### Hypothesis 2:
Has there been a significant change in the adoption rate of animals before and after the onset of COVID-19?

 - $H0$: There is no significant difference in the adoption rate of animals before and after the onset of COVID.
 - $H1$: There is a significant increase in the adoption rate of animals after the onset of COVID compared to before.

### Hypothesis 3:
Does intake condition influence the probability of adoption for animals?

 - $H0$: There is no significant relationship between the intake condition of animals at the shelter and their likelihood of adoption.
 - $H1$: There is a significant relationship between the intake condition of animals at the shelter and their likelihood of adoption.

### Hypothesis 4:
Does age influence the probability of adoption for animals?

 - $H0$: There is no significant relationship between animals' age and their likelihood of adoption.
 - $H1$: There is a significant relationship between animals' age and their likelihood of adoption.

## **Research Questions**
### Research Question 1:
Does the city of Austin maintain a save rate of **90%** or higher for animals, thereby meeting the criteria to be classified as a **no-kill city**?

## Citations:
1. Best Friends Animal Society. (2023). Animal Shelter Statistics: Map Methodology. Retrieved from https://bestfriends.org/no-kill-2025/animal-shelter-statistics/map-methodology
2. City of Austin. (2023). Austin Animal Center Intakes. Retrieved from [here](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Intakes/wter-evkm)
3. City of Austin. (2023). Austin Animal Center Outcomes. Retrieved from [here](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes/9t4d-g238)
4. City of Austin. (2020, March 20). New Orders to Align COVID-19 Restrictions Statewide. Retrieved from [here](https://web.archive.org/web/20201229180748/https://www.austintexas.gov/news/new-orders-align-covid-19-restrictions-statewide)
5. City of Austin, Texas. (n.d.). Austin Guide to Dogs and Cats. Retrieved from [here](https://www.austintexas.gov/sites/default/files/files/AAC/Austin%20Guide%20to%20Dogs%20and%20Cats.pdf)
6. Koschalk, K. (Chewy). (2023, October 25). The Pros and Cons of Spaying and Neutering an Older Dog. Retrieved from [here](https://be.chewy.com/all-about-spay-and-neuter-in-senior-dogs/)
7. Spring House Animal Hospital. (2022, June 15). How Old is Too Old to Spay or Neuter My Dog. Retrieved from [here](https://www.springhouseanimalhospital.com/site/blog/2022/06/15/how-old-is-too-old-to-spay-or-neuter-my-dog)

> [!NOTE]  
> The visualizations might be too large to show on GitHub, you can check the interactive visualizations on this [page](https://rebekah-chuang.quarto.pub/portfolio/posts/Pet_Adoption_Analysis_in_Austin/) if you want, though it's not the final version!