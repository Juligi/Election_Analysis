# Election_Analysis
Election Analysis using Python for learning purposes


# Election Audit Project Overview:

This project required aiding a mock Colorado Board of Elections Employee, Tom, in an election audit of the tabulated results for US Congressional precinct in Colorado.  As the team-member, I am tasked with with:
1) reporting the total number of votes cast
2) the total number of votes for each candidate
3) the percentage of votes for each candidate
4) the winner of the election based on the popular vote

While historically, this tabulation has occured in excel, the election management wants to automate the process using Python for this election and re-use the code for future elections, to include senatorial districts and local elections.  The key goal is to generate a vote count report to certify the U.S. Congressional race.  

# Election Results Summary

The audit showed that a total of **360,711** votes were casted in the Congressional Election.

The following table view is a breakdown of the number of votes & the percentage of total votes for each county in the precinct:

| County        | Votes Casted  | % of Total Votes |
| ------------- | ------------- | -----------------|
| Denver        | 306,055       | 82.8%            |
| Jefferson     | 38,855        | 10.5%            |
| Arapahoe      | 24,801        | 6.7%             |

Denver county was the county with the largest voter turnout by far taking over 80% of the vote.  Jefferson and Arapahoe struggled with voter turnout, both accounting for the rest of 17.2% of the voter turnout.


## Candidate & Associated Vote Breakdown

Diana Degette won the congressional race by landslide.  Ms. Degette received 73.8% of the vote for a total of 272,892 the winning vote count. Below is a full breakdown of the 2nd and 3rd place candidates, depicting a full breakdown of the number of votes and the percentage of the total votes each candidate received. 

|Candidate Name           | Votes Casted  | % of Total Votes |
| -------------           | ------------- | -----------------|
| Diana Degette           | 272,892       | 73.8%            |
| Charles Casper Stockham | 85,213        | 23%              |
| Raymon Anthony Doane    | 11,606        | 3.1%             |


#Election-Audit Summary & Future Recommendations:
 
Overall the election-audit was a success and a fundmental effort for future simplication and establishment of an ongoing standard operating procedure (SOP).  Simply,  re-using an election file template, the commission can re-use for loops, repetition and conditional statements with membership and logical operators to find the requested results for various and unique future elections across the state.   

##For future usage & SOP:

* The simplest method, would to create an ongoing election results template for each election, and when a new election is ran, the exisiting Pypoll script can be modified in the variable to load the specific election file from the saved path.  Code example below:
- 
_(Code instruction for developer) add a variable to load a file from a path_.
**Code to Change** **_file_to_load = os.path.join("Resources", "election_results.csv")_**
_(Code instruction for developer) Add a variable to save the file to a path._
**Code to Change** **_file_to_save = os.path.join("analysis", "election_analysis.txt")_**
 
# Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
