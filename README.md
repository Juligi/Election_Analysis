# Election_Analysis
Election Analysis using Python for learning purposes


# Election Audit Project Overview:

This project required aiding a mock Colorado Board of Elections Employee, Tom, in an election audit of the tabulated results for a US Congressional precinct in Colorado.  As a team member, I am tasked with:
1) reporting the total number of votes cast
2) the total number of votes for each candidate
3) the percentage of votes for each candidate
4) the winner of the election based on the popular vote

While historically, this tabulation has occurred in excel, the election management wants to automate the process using Python for this election and re-use the code for future elections, including senatorial districts and local elections.  The key goal is to generate a vote count report to certify the U.S. Congressional race.  

# Election Results Summary

The audit showed that a total of **360,711** votes were cast in the Congressional Election.

The following table view is a breakdown of the number of votes & the percentage of total votes for each county in the precinct:

| County        | Votes Cast | % of Total Votes |
| ------------- | ------------- | -----------------|
| Denver        | 306,055       | 82.8%            |
| Jefferson     | 38,855        | 10.5%            |
| Arapahoe      | 24,801        | 6.7%             |

Denver County was the county with the largest voter turnout, taking over 80% of the vote.  Jefferson and Arapahoe struggled with voter turnout, both accounting for the rest of 17.2% of the voter turnout.


## Candidate & Associated Vote Breakdown

Diana DeGette won the congressional race by a landslide.  Ms. Degette received 73.8% of the vote for a total of 272,892 the winning vote count. Below is a full breakdown of the 2nd and 3rd place candidates, depicting a full breakdown of the number of votes and the percentage of each candidate's total votes. 

|Candidate Name           | Votes Cast | % of Total Votes |
| -------------           | ------------- | -----------------|
| Diana Degette           | 272,892       | 73.8%            |
| Charles Casper Stockham | 85,213        | 23%              |
| Raymon Anthony Doane    | 11,606        | 3.1%             |


# Election-Audit Summary & Future Recommendations:
 
Overall the election audit was a success and a fundamental effort for future simplification and establishment of an ongoing standard operating procedure (SOP).  Simply, by re-using an election file template, the commission can re-use loops, repetition, and conditional statements with membership and logical operators to find the requested results for various and unique future elections across the state.   

## Future SOP:

The simplest method would be to create an ongoing election results template for each election. When a new election is run, the existing Pypoll script can be modified in the variable to load the new and specific election file from the saved path.  Code examples are added below for reference:

_(This is code instruction for future election audit developers: add a variable to load the specific election file from a path)_

```
file_to_load = os.path.join("Resources", "election_results.csv")
```
_(This is code instruction for future election audit developers: Add a variable to save the file to a path.)_

```
 file_to_save = os.path.join("analysis", "election_analysis.txt")
```

Lastly, the script and election_result.csv file can be easily modified for future usage and election-audit analysis by simply changing the variables, and changing/creating new state, county or city list, and city or state dictionaries, to now go from 
```
# Create a county list and county votes dictionary.
county_names = []
county_votes = {}
```

to a new, a city list and city votes dictionary for example:
```
# Create a city list and city votes dictionary.
city_names = []
city_votes = {}
```

In conclusion,the election commission can use [this Pypoll_challenge script](https://github.com/Juligi/Election_Analysis/blob/main/PyPoll_Challenge.py) with some modifications—for any future election.
