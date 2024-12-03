
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QStackedLayout
)
from PyQt6.QtGui import QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt
from os import path

def pyblock_instuction_GUI(brick_data):

    total_bricks = len(brick_data)

    # Get the directory of the current script
    script_dir = path.dirname(path.abspath(__file__))

    # Construct the full paths to the image files
    two_by_two_file_path = path.join(script_dir, '2x2.png')
    two_by_three_file_path = path.join(script_dir, '2x3.png')
    three_by_two_file_path = path.join(script_dir, '3x2.png')
    two_by_four_file_path = path.join(script_dir, '2x4.png')
    four_by_two_file_path = path.join(script_dir, '4x2.png')
    two_by_two_normal_file_path = path.join(script_dir, '2x2normal.png')
    two_by_three_normal_file_path = path.join(script_dir, '2x3normal.png')
    three_by_two_normal_file_path = path.join(script_dir, '3x2normal.png')
    two_by_four_normal_file_path = path.join(script_dir, '2x4normal.png')
    four_by_two_normal_file_path =  path.join(script_dir, '4x2normal.png')
    blank_file_path = path.join(script_dir, 'blank.png')

    class MyMainWindow(QMainWindow):
        
        def __init__(self):
            # must always call super().__init__() to start window
            super().__init__()

            # Set the title and size of the main window
            self.setWindowTitle('PyBlock Instructional Guide')
            self.setGeometry(300, 300, 800, 400)

            # setting the window's background color
            palette = self.palette()
            palette.setColor(QPalette.ColorRole.Window, QColor("#d2ecfb"))
            self.setPalette(palette)

            # Set layout arrangement
            # page layout is a vertical arrangment
            # with sub horizontal layouts
            page_layout = QVBoxLayout()
            brick_layout = QHBoxLayout()
            progress_layout = QHBoxLayout()
            button_layout = QHBoxLayout()
            
            page_layout.addLayout(brick_layout)
            page_layout.addLayout(progress_layout)
            page_layout.addLayout(button_layout)

            # setting initial brick index
            self.brick_index = 0

            # set brick image boxes (label with pixmap)
            self.previous_brick_img = QLabel()
            self.previous_brick_img.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            self.current_brick_img = QLabel()
            self.current_brick_img.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            self.next_brick_img = QLabel()
            self.next_brick_img.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            brick_layout.addWidget(self.previous_brick_img)
            brick_layout.addWidget(self.current_brick_img)
            brick_layout.addWidget(self.next_brick_img)
            # setting initial images
            self.change_brick_images(self.brick_index)

            # set progress bar and brick index
            self.progress_bar = QProgressBar()
            self.progress_bar.setMinimum(0)
            self.progress_bar.setMaximum(total_bricks)
            self.progress_bar.setValue(1)
            progress_layout.addWidget(self.progress_bar)

            self.brick_index_label = QLabel('Brick ' + str(self.brick_index + 1) + ' / ' + str(total_bricks))
            progress_layout.addWidget(self.brick_index_label)
            
            # set previous and next buttons
            back_button = QPushButton('Previous Brick')
            back_button.clicked.connect(self.back_button_was_clicked)
            button_layout.addWidget(back_button)

            next_button = QPushButton('Next Brick')
            next_button.clicked.connect(self.next_button_was_clicked)
            button_layout.addWidget(next_button)

            # setting the full page layout as the central widget
            widget = QWidget()
            widget.setLayout(page_layout)
            self.setCentralWidget(widget)

        def change_brick_images(self, brick_index):
            # image sizes
            center_img_width = 400
            center_img_height = 400
            next_img_width = 200
            next_img_height = 200
            prev_img_width = 200
            prev_img_height = 200
            
            # setting the brick type and orientation for the given brick index
            # [0] is 2x2, [1,0] is 2x3, [1,1] is 3x2, [2,0] is 2x4, and [2,1] is 4x2
            current_brick_type = brick_data[brick_index][0]

            # since 2x2 has no orientation, then only brick orientation will be set
            # for 2x3 and 2x4 bricks
            if current_brick_type:
                brick_orientation = brick_data[brick_index][1]

            # PyQT6 uses labels and sets them as Pixmaps to add images
            # checking for type and orientation to set the right image for the current brick
            if current_brick_type == 1 and brick_orientation == 0:
                pixmap = QPixmap(two_by_three_file_path)
                scaled_pixmap = pixmap.scaled(center_img_width, center_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.current_brick_img.setPixmap(scaled_pixmap)
            elif current_brick_type == 1 and brick_orientation == 1:
                pixmap = QPixmap(three_by_two_file_path)
                scaled_pixmap = pixmap.scaled(center_img_width, center_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.current_brick_img.setPixmap(scaled_pixmap)
            elif current_brick_type == 2 and brick_orientation == 0:
                pixmap = QPixmap(two_by_four_file_path)
                scaled_pixmap = pixmap.scaled(center_img_width, center_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.current_brick_img.setPixmap(scaled_pixmap)
            elif current_brick_type == 2 and brick_orientation == 1:
                pixmap = QPixmap(four_by_two_file_path)
                scaled_pixmap = pixmap.scaled(center_img_width, center_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.current_brick_img.setPixmap(scaled_pixmap)
            elif current_brick_type == 0:
                pixmap = QPixmap(two_by_two_file_path)
                scaled_pixmap = pixmap.scaled(center_img_width, center_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.current_brick_img.setPixmap(scaled_pixmap)

            # setting previous and next brick types
            # PyQT6 uses labels and sets them as Pixmaps to add images
            # setting the next or previous images blank if at start or end
            if brick_index == 0:
                pixmap = QPixmap(blank_file_path)
                scaled_pixmap = pixmap.scaled(prev_img_width, prev_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.previous_brick_img.setPixmap(scaled_pixmap)
                prev_brick_type = None
            else:
                prev_brick_type = brick_data[brick_index - 1][0]

                if prev_brick_type:
                    prev_brick_orientation = brick_data[brick_index - 1][1]

                if prev_brick_type == 0:
                    pixmap = QPixmap(two_by_two_normal_file_path)
                    scaled_pixmap = pixmap.scaled(prev_img_width, prev_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.previous_brick_img.setPixmap(scaled_pixmap)
                elif prev_brick_type == 1 and prev_brick_orientation == 0:
                    pixmap = QPixmap(two_by_three_normal_file_path)
                    scaled_pixmap = pixmap.scaled(prev_img_width, prev_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.previous_brick_img.setPixmap(scaled_pixmap)
                elif prev_brick_type == 1 and prev_brick_orientation == 1:
                    pixmap = QPixmap(three_by_two_normal_file_path)
                    scaled_pixmap = pixmap.scaled(prev_img_width, prev_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.previous_brick_img.setPixmap(scaled_pixmap)
                elif prev_brick_type == 2 and prev_brick_orientation == 0:
                    pixmap = QPixmap(two_by_four_normal_file_path)
                    scaled_pixmap = pixmap.scaled(prev_img_width, prev_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.previous_brick_img.setPixmap(scaled_pixmap)
                elif prev_brick_type == 2 and prev_brick_orientation == 1:
                    pixmap = QPixmap(four_by_two_normal_file_path)
                    scaled_pixmap = pixmap.scaled(prev_img_width, prev_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.previous_brick_img.setPixmap(scaled_pixmap)

            if brick_index == total_bricks - 1:
                pixmap = QPixmap(blank_file_path)
                scaled_pixmap = pixmap.scaled(next_img_width, next_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.next_brick_img.setPixmap(scaled_pixmap)
                next_brick_type = None
            else:
                next_brick_type = brick_data[brick_index + 1][0]

                if next_brick_type:
                    next_brick_orientation = brick_data[brick_index + 1][1]

                if next_brick_type == 0:
                    pixmap = QPixmap(two_by_two_normal_file_path)
                    scaled_pixmap = pixmap.scaled(next_img_width, next_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.next_brick_img.setPixmap(scaled_pixmap)
                elif next_brick_type == 1 and next_brick_orientation == 0:
                    pixmap = QPixmap(two_by_three_normal_file_path)
                    scaled_pixmap = pixmap.scaled(next_img_width, next_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.next_brick_img.setPixmap(scaled_pixmap)
                elif next_brick_type == 1 and next_brick_orientation == 1:
                    pixmap = QPixmap(three_by_two_normal_file_path)
                    scaled_pixmap = pixmap.scaled(next_img_width, next_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.next_brick_img.setPixmap(scaled_pixmap)
                elif next_brick_type == 2 and next_brick_orientation ==  0:
                    pixmap = QPixmap(two_by_four_normal_file_path)
                    scaled_pixmap = pixmap.scaled(next_img_width, next_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.next_brick_img.setPixmap(scaled_pixmap)
                elif next_brick_type == 2 and next_brick_orientation ==  1:
                    pixmap = QPixmap(four_by_two_normal_file_path)
                    scaled_pixmap = pixmap.scaled(next_img_width, next_img_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.next_brick_img.setPixmap(scaled_pixmap)

        # setting functions for button actions when clicked
        def back_button_was_clicked(self):
            # show_previous_brick_function
            if self.brick_index != 0:
                self.brick_index -= 1
                self.progress_bar.setValue(self.brick_index + 1)
                self.brick_index_label.setText('Brick ' + str(self.brick_index + 1) + ' / ' + str(total_bricks))
                self.change_brick_images(self.brick_index)

        def next_button_was_clicked(self):
            # show_next_brick_function
            if self.brick_index != total_bricks - 1:
                self.brick_index += 1
                self.progress_bar.setValue(self.brick_index + 1)
                self.brick_index_label.setText('Brick ' + str(self.brick_index + 1) + ' / ' + str(total_bricks))
                self.change_brick_images(self.brick_index)

    app = QApplication([])
    main_window = MyMainWindow()
    main_window.show()
    app.exec()

# brick_data = [[0],[1,0],[2,1],[2,0],[0],[1,1]]

# pyblock_instuction_GUI(brick_data)