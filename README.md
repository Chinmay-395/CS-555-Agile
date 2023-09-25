# CS-555-Agile

**Overall Description of the Scrum Process and Roles:**

Scrum is an agile framework that organizes the development process into time-boxed iterations called sprints. Key roles in Scrum include:

1. **Product Owner:** Represents the stakeholders, defines the product backlog, and prioritizes features.

2. **Scrum Master:** Facilitates Scrum events, removes impediments, and ensures the team adheres to Scrum practices.

3. **Development Team:** A self-organizing, cross-functional group responsible for delivering increments of the product.

**Planning Process for Sprint 1:**

In Sprint 1, you are focusing on developing specific software and hardware features. The planning process typically includes the following steps:

- **Participants:** The Product Owner, Scrum Master, and Development Team are involved.

- **Work Products:** The key work products include a refined product backlog with user stories for the selected software and hardware features, and detailed acceptance criteria for these stories.

- **Roles and Deliverables:**

  - **Product Owner:** Defines the user stories related to Cruise Control, Lane Departure Warning, CAN buses, Adaptive Cruise Control, Tilt-and-Telescoping Steering Wheel, Radars, LiDAR, Ultrasonic sensors, IMU, Cameras, Smart-phone as a dashcam, and Actuators and Motors. Prioritizes these stories based on business value.

  - **Scrum Master:** Facilitates the sprint planning meeting, ensuring that the Development Team understands the scope and goals of Sprint 1. Assists the team in identifying tasks and dependencies.

  - **Development Team:** Selects user stories from the product backlog based on their capacity and commitment for the sprint. They may further break down the user stories into tasks, estimate effort, and create a sprint backlog.

**Day-to-Day Activities During Sprint 1:**

- **Participants:** The primary participants in day-to-day activities are the members of the Development Team.

- **Work Products:** Daily progress and task status are tracked on a Scrum board or using digital tools.

During Sprint 1:

- The Development Team collaboratively works on implementing the selected software and hardware features, following the acceptance criteria defined during sprint planning.

- Daily stand-up meetings (daily scrum) are conducted, where each team member provides updates on their progress, discusses impediments, and plans the day's work.

- The Development Team continuously refines the design, codes, tests, and reviews the software and hardware components to ensure they meet the defined criteria.

**End of Sprint 1:**

- **Participants:** The Development Team, Scrum Master, and Product Owner are involved in the sprint review and sprint retrospective.

- **Work Products:**

  - In the sprint review, the Development Team demonstrates the completed software and hardware features to the Product Owner and stakeholders.

  - In the sprint retrospective, the team reflects on the sprint, discusses what went well and what could be improved, and identifies action items for process enhancement.

**Measurement of Progress:**

Progress in Scrum is measured using various metrics, including:

- **Burn-Down Chart:** Tracks the remaining work in the sprint backlog, providing a visual representation of progress.

- **Velocity:** Calculated based on the amount of work completed in previous sprints, helping estimate the team's capacity for the current sprint.

- **Daily Stand-Up Meetings:** Daily updates and discussions in the stand-up meetings provide real-time insights into progress and potential impediments.

**Adjusting Priorities:**

- **Who Sets Priorities:** The Product Owner sets priorities based on stakeholder needs and business value.

- **When Changes Can Be Made:** Priorities can be adjusted at any time but are typically refined during sprint planning meetings. Adjustments should consider the impact on the current sprint and overall project goals. Major changes may be deferred to the next sprint planning meeting to maintain sprint focus.

## Folder structure:

- main.py : the top most file, where the code should start.
- printOutput.py: This will print output of the code on the console as well as in text file.
- filters.py: Data filtering based on different aspects should be merged here.
- Initialparser.py: Tagging of each of the input based on "valid" tag. ("valid" tags are the once which will be used for the ouputing all the relevant data in
  the console or in the text file).

## Installation and Execution:

Step-1: **Create a virtual environment** <br>

For Linux/Mac:
`virtualenv -p /usr/bin/python3 vir_env` <br>

`source vir_env/bin/activate` <br>

<hr>
For Windows: <br>
`python -m venv vir_env` <br>
`vir_env\Scripts\activate` <br>

Step-2: **Installing dependencies** <br>

execute the command: `pip install -r requirements.txt`

Step-3: **Running the code** <br>

For Linux/Mac:<br>
in the console execute the command `python3 main.py` <br>

For windows: <br>
in the console execute the command `python main.py` <br>
