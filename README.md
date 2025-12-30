# Healthcare Access Simulator

## Project Overview
This project is a Python-based simulation of role-based access control (RBAC) in a healthcare environment.  
It models realistic access rules for different roles such as doctors, nurses, biomedical scientists, and administrators.

The goal is to explore how healthcare data access can be structured securely and clearly using core software development principles.



## Motivation
I am transitioning into software development from a healthcare background and wanted to build a project that reflects:
- real-world healthcare workflows
- cybersecurity fundamentals (access control, least privilege)
- clean Python design using data structures and object-oriented programming

This project is being developed incrementally as part of my software development bootcamp.



## Learning Goals
- Practice Python fundamentals and data structures
- Apply object-oriented programming concepts
- Understand and model role-based access control (RBAC)
- Use Git and GitHub with clear, incremental commits
- Bridge healthcare domain knowledge with software development



## Current Progress
- Repository initialised and connected to GitHub
- Core healthcare roles defined (Doctor, Nurse, Biomedical Scientist, Admin)
- Permissions modelled using a role-permission mapping (RBAC)
- User class implemented with name and role validation
- Role-based add-on test requests implemented with fine-grained restrictions
- Lab result amendment logic implemented with mandatory amendment reasons
- Permissions enforced using both role permissions and policy checks

## Notes
- Doctors can request multiple add-on tests (e.g. reticulocytes, iron studies)
- Biomedical Scientists can request blood film only
- Only Biomedical Scientists can amend lab results, and must provide a valid reason

## Planned Next Steps
- Simulate access attempts and audit logging
- Refine permissions to reflect real-world healthcare scenarios


## Disclaimer
This project is a learning exercise and does not represent a real clinical system.

