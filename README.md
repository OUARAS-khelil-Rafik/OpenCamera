# **OpenCamera GUI Application**
# **Overview**
This Python script, OpenCamera.py, creates a graphical user interface (GUI) application using PyQt6 for camera control and real-time display. The application utilizes the OpenCV library for capturing and processing camera frames.

# **Dependencies**
- PyQt6: UI development library for Python.
- OpenCV: Computer vision library for camera access and image processing.
- How to Run
- Install Dependencies:

```bash
pip install PyQt6
pip install opencv-python
```
- Run the Script:
```bash
python OpenCamera.py
```
# **Usage**
- Press the "On" button to start the camera feed.
- Press the "Off" button to stop the camera feed.
- The real-time camera feed is displayed in the main window.

# **Features**

**CameraControl Class:**
- Manages camera control operations such as starting, stopping, and reading frames.
- Converts camera frames to a format suitable for display in the PyQt6 GUI.

**Ui_MainWindow Class:**
- Implements the UI design using PyQt6.
- Defines the layout, buttons, and connections to the camera control functions.
- Buttons

**On (Start Camera):**
- Initiates the camera feed.

**Off (Stop Camera):**
- Stops the camera feed.

# **Important Notes**
- Ensure that the default camera (index 0) is accessible.
- Press the 'q' key to stop the camera feed.

# **Code Structure**

**Imports:**
- PyQt6 and OpenCV libraries are imported.

**CameraControl Class:**
- Manages camera-related operations.

**Ui_MainWindow Class:**
- Defines the GUI layout and button functionalities.

**Main Script:**
- Initializes the PyQt6 application and sets up the main window.
- Creates an instance of CameraControl.
- Connects UI buttons to camera control functions.

# **Additional Information**
- The UI is generated from a .ui file using the PyQt6 UI code generator (pyuic6).
- Manual changes to the generated UI file will be lost when regenerated.

## Auteur 
**OUARAS Khelil Rafik**
