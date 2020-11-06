## Project Proposal

### Overview

A webapp where users can generate a daily physical therapy routine, based on constraints like time, equipment available, and target area(s).

### Technologies required (besides typical Hackbright tech stack)

- Web scraping (probably Beautiful Soup)
- Calendar API (2.0)

### Data

- Exercise descriptions, time, equipment needed, target area
    - Visual reference would be great
- User needs
- Routine (list of exercises for the day)
- Past routines generated

### Roadmap

#### MVP

- users can enter amount of time (drop-down menu, I think?)
- users can choose whether they have equipment or not
- users can select a target area (leg, foot, arm, etc.) to focus their exercises on
- users can view a list of exercises (the routine) based on the above constraints
- users can log in


#### 2.0

- users can save # of times per week to complete each exercise
- routine generator will take intended weekly frequency into account
- users can schedule reminders to do their routine
- users can view past routines (how far back? is this me shooting myself in the foot?)
- users can save individual exercises 
- users can indicate that they've completed a routine
- convert to React

#### 3.0

- Maybe activity logging (but I think this is feature creep)
- What else?