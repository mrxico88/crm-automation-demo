# crm-automation-demo
## Prerequisite 

Please install python 3, pip and virtualenv in your local machine.

Read [this guide](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/blob/master/Customer%20Service/Testing/Automation/Samples/automation/selectors/caseCRUDSelectors.json) for an example on MSDynamic365 automation.

## Setup project 

Navigate to your project directory:

```
cd <project_path>
```

Create your virtual environment

```
python3 -m venv venv
```

Activate your virtual environment:

````
source venv/bin/activate
````

Install required packages:

```
pip install -r requirement.txt
```

Install Robot Framework browser dependencies. For reference check https://robotframework-browser.org/#installation

```
rfbrowser init
```

Run your tests

```
python -m robot test_suite/microsoft_365_tests.robot
```
