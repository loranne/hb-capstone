# PT Remix - Hackbright Academy capstone 2020 

Not yet deployed. 

### [View a short demo here!](https://youtu.be/YWSyoudovsI)

A physical therapy home companion that allows users to generate a routine of their assigned exercises. Routine generator bases decisions on the following constraints:

- injury/condition being treated
- length of time for routine
- user focus for exercises (strength, endurance, balance, and flexibility)
- whether user has equipment necessary

Exercises have set relationships with injuries in the database, narrowing down the pool from which the routine generator can choose.

Routine pages feature detailed descriptions of each exercise, number of reps, and visual aids, along with feedback buttons to record user experience of each exercise within the routine.

Exercises are tied to routines by an association table. Originally, this had just the IDs for routine and exercise (plus primary key), but as I expanded the project, the association table became the logical place to store data about a specific instance of an exercise as it applied to one routine: in particular, how many reps of that exercise were assigned in that routine, and the user's experience of that exercise (in terms of whether it caused them pain).

Future considerations include adding another user type for physical therapists, who would then be connected to core user type. PTs could assign and tweak details about exercises to better benefit their patients. 

## Planning phase

Would allow users to input variables like time and equipment available, pain levels/other movement restrictions, and generate a physical therapy routine for the day. Ideally would feature visual aids, and have access for therapist to add/modify exercises on their end (not likely to happen with v. 1). 

*Things I'll need/features to consider:*
- workout API. Look at Google Fit API. This might be better than the alternative, which is:
- or way for user to input exercise details
- Timer
- Visual representations of each exercise and equipment item