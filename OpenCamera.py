# Form implementation generated from reading ui file 'OpenCamera.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import cv2

class CameraControl:
    def __init__(self):
        self.capture = None
        self.camera_running = False

    def start(self):
        if not self.camera_running:
            self.capture = cv2.VideoCapture(0)  # 0 corresponds to the default camera
            if self.capture.isOpened():
                self.camera_running = True
                print("Camera turned ON")
                self.read_camera()
            else:
                print("Failed to open the camera")
        else:
            print("Camera is already ON")

    def stop(self):
        if self.camera_running:
            self.camera_running = False
            print("Camera turned OFF")
            if self.capture:
                self.capture.release()
        else:
            print("Camera is already OFF")

    def read_camera(self):
        while self.camera_running:
            ret, frame = self.capture.read()
            if ret:
                # Convert the BGR image to RGB format
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Convert the image to QImage
                q_image = QtGui.QImage(
                    rgb_image.data, rgb_image.shape[1], rgb_image.shape[0],
                    QtGui.QImage.Format.Format_RGB888  # Use Format_RGB888 directly
                )

                # Create a pixmap from the QImage
                pixmap = QtGui.QPixmap.fromImage(q_image)

                # Set the pixmap to the QLabel to display the camera feed
                ui.label_camera.setPixmap(pixmap)

                # Adjust the size of the QLabel to fit the image
                ui.label_camera.setScaledContents(True)

                # Break the loop if the user presses the 'q' key
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.stop()
            else:
                print("Error reading from the camera")
                self.stop()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # QLabel for displaying the camera feed
        self.label_camera = QtWidgets.QLabel(self.centralwidget)
        self.label_camera.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_camera.setObjectName("label_camera")

        # QVBoxLayout for centering the QLabel
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.addWidget(self.label_camera)

        # QPushButton for starting the camera
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        layout.addWidget(self.pushButton)

        # QPushButton for stopping the camera
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        layout.addWidget(self.pushButton_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to functions
        self.pushButton.clicked.connect(self.start_camera)
        self.pushButton_2.clicked.connect(self.stop_camera)

    def start_camera(self):
        ui.camera_control.start()

    def stop_camera(self):
        ui.camera_control.stop()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Camera Control"))
        self.pushButton.setText(_translate("MainWindow", "On"))
        self.pushButton_2.setText(_translate("MainWindow", "Off"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    # Create an instance of CameraControl
    ui.camera_control = CameraControl()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
