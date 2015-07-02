__authors__ = 'Ramshah Khan, Fatima Zohra, and Adnan Niazi'

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.phonon import Phonon
from my_gui import Ui_MainWindow

class MyMainGui(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainGui, self).__init__(parent)
        self.setupUi(self)

        self.mediaObject = Phonon.MediaObject()

        self.mediaObject.setTickInterval(1000)
        self.mediaObject.tick.connect(self.tick)            # on each tick of the video, call the tick function

        self.videoWidget = self.videoPlayer.videoWidget()
        Phonon.createPath(self.mediaObject, self.videoWidget)

        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.mediaObject, self.audioOutput)

        self.seekSlider.setMediaObject(self.mediaObject)    # take the video and assign to seekslider
        self.volumeSlider.setAudioOutput(self.audioOutput)  # take the audio and assign it to volume slider

        self.actionLoad.triggered.connect(self.load_and_play_files)
        self.actionMy_playlist.triggered.connect(self.show_hide_playlist)
        self.actionMy_playlist.setText('Hide my playlist')
        self.dockWidget.visibilityChanged.connect(self.change_show_hide_menu_text)

        self.actionExit.triggered.connect(self.exit_gui)

        self.toolButton_play_pause.clicked.connect(self.play_or_pause)
        self.toolButton_next.clicked.connect(self.next_track)
        self.toolButton_previous.clicked.connect(self.previous_track)
        self.toolButton_stop.clicked.connect(self.stop)
        self.listWidget.clicked.connect(self.play_item_clicked_in_playlist)
        self.mediaObject.totalTimeChanged.connect(self.calculate_total_video_time)

        self.current_source_index = 0
        app.setStyle(QStyleFactory.create('Plastique'))

        self.shortcutFull = QShortcut(self)
        self.shortcutFull.setKey(QKeySequence('Esc'))
        self.shortcutFull.setContext(Qt.ApplicationShortcut)
        self.shortcutFull.activated.connect(self.handleFullScreen)
        self.toolButton_fullscreen.clicked.connect(self.handleFullScreen)

        self.stage = 'GUI just started'
        self._enable_disable_buttons()

    def handleFullScreen(self):
        """Whenever Esc button on the keyboard or full-screen button on the GUI is pressed,
        toggle between full-screen and normal mode"""

        if self.videoWidget.isFullScreen():
            self.videoWidget.exitFullScreen()
        else:
            self.videoWidget.enterFullScreen()

    def load_and_play_files(self):
        """Presents user with a Dialog box to choose media files. Once selected, it then plays the first
        file among the selected files"""

        files = QFileDialog.getOpenFileNames(self, None, '',
                                             'Media file(*.mp4 *.wmv *.avi *.3gp *.oog *.mpeg *.mp2 *.wma *.mp3)'
                                             ';;All files(*.*)')
        if files == []:
            # If no media files have been selected then don't execute the rest of the code.
            return

        self.media_sources = []
        for file in files:
            self.populate_playlist(file)
            self.media_sources.append(Phonon.MediaSource(file))

        self.mediaObject.setQueue(self.media_sources)  # automatically run all selected file one after the other
        self.mediaObject.play()

        self.stage = 'Track loaded and playing'
        self._enable_disable_buttons()

    def populate_playlist(self, file):
        """Displays name of selected tracks in the playlist"""

        self.qfile_info = QFileInfo(file)
        self.listWidget.addItem(self.qfile_info.fileName())

    def change_show_hide_menu_text(self):
        """If the user manually closes the dock widget then it changes the show/hide playlist text
        in the view menu"""

        if self.dockWidget.isVisible() == True:
            self.actionMy_playlist.setText('Hide my playlist')
        else:
            self.actionMy_playlist.setText('Show my playlist')

    def show_hide_playlist(self):
        """Toggles the visibility of My playlist dock widget"""

        if self.dockWidget.isVisible() == True:
            self.dockWidget.setVisible(False)
            self.actionMy_playlist.setText('Show my playlist')
        else:
            self.dockWidget.setVisible(True)
            self.actionMy_playlist.setText('Hide my playlist')

    def play_item_clicked_in_playlist(self):
        """Plays the track the user has clicked in the playlist"""

        self.current_source_index = self.listWidget.currentRow()
        print(self.current_source_index)
        self.mediaObject.setCurrentSource(self.media_sources[self.current_source_index])
        self.mediaObject.play()

    def play_or_pause(self):
        """Apart from the obvious, it toggles the icon of play/pause button and its tooltip"""

        icon_1 = QIcon()
        icon_1.addPixmap(QPixmap(':/icons/pause.png'))
        icon_2 = QIcon()
        icon_2.addPixmap(QPixmap(':/icons/play.png'))
        if self.mediaObject.state() == Phonon.PlayingState:
            self.mediaObject.pause()
            self.toolButton_play_pause.setIcon(icon_2)
            self.toolButton_play_pause.setToolTip('Play')
        elif self.mediaObject.state() == Phonon.PausedState or self.mediaObject.state() == Phonon.StoppedState:
            self.mediaObject.play()
            self.toolButton_play_pause.setIcon(icon_1)
            self.toolButton_play_pause.setToolTip('Pause')

        self.stage = 'Media interrupted'
        self._enable_disable_buttons()

    def stop(self):
        """Completely halts the players and reset the seekslider to 0 position"""

        self.mediaObject.stop()
        self.stage = 'Media stopped'
        self._enable_disable_buttons()

        icon = QIcon()
        icon.addPixmap(QPixmap(':/icons/play.png'))
        self.toolButton_play_pause.setIcon(icon)
        self.toolButton_play_pause.setToolTip('Play')

    def next_track(self):
        """Cycles through all files in the playlist in the form of a loop
        (just like in VLC player)"""

        if self.current_source_index < len(self.media_sources)-1:
             self.current_source_index += 1
        else:
            self.current_source_index = 0 # start from the beginning of the list

        self.mediaObject.setCurrentSource(self.media_sources[self.current_source_index])
        self.mediaObject.play()
        self.listWidget.setCurrentRow(self.current_source_index)

    def previous_track(self):
        """Cycles through all files in the playlist in the form of a loop
        (just like in VLC player)"""

        if self.current_source_index > 0:
            self.current_source_index -= 1
        else:
            self.current_source_index = len(self.media_sources)-1  #start again from the end of the list

        self.mediaObject.setCurrentSource(self.media_sources[self.current_source_index])
        self.mediaObject.play()
        self.listWidget.setCurrentRow(self.current_source_index)

    def tick(self, tick_time):
        """Displays updated time every second in the track time label"""

        self.current_tick_time_str = self.convert_time_to_human_readable_format(tick_time)
        self.display_time = self.current_tick_time_str + ' | ' + self.total_video_time_str
        self.track_time.setText(self.display_time)

    def calculate_total_video_time(self):
        """Executes only at the beginning of each track. Calculates the total time of the media object"""

        self.total_video_time_ms = self.mediaObject.totalTime()
        print(self.total_video_time_ms)
        self.total_video_time_str = self.convert_time_to_human_readable_format(self.total_video_time_ms)
        print(self.total_video_time_str)

    def convert_time_to_human_readable_format(self, time_in_ms):
        """Time retrieved from media object is in ms. This function converts it into hh mm ss format"""

        time = time_in_ms/1000 # convert from milliseconds to seconds
        displayTime = QTime((time / 3600) % 60, (time / 60) % 60, (time / 1) % 60)
        if (self.total_video_time_ms/1000) > 3600:
            return displayTime.toString('hh:mm:ss')
        else:
            return displayTime.toString('mm:ss')

    def _enable_disable_buttons(self):
        """Activates or deactivates buttons depending on the scenario"""

        if self.stage == 'GUI just started':
            self.toolButton_play_pause.setDisabled(True)
            self.toolButton_stop.setDisabled(True)
            self.toolButton_next.setDisabled(True)
            self.toolButton_previous.setDisabled(True)
        elif self.stage == 'Track loaded and playing':
            self.toolButton_play_pause.setEnabled(True)
            self.toolButton_stop.setEnabled(True)
            self.toolButton_next.setEnabled(True)
            self.toolButton_previous.setEnabled(True)
        elif self.stage == 'Media stopped':
            self.toolButton_stop.setDisabled(True)
        elif self.stage == 'Media interrupted':
            self.toolButton_stop.setEnabled(True)

    def exit_gui(self):
        """Quits the GUI is Exit is selected from the File menu"""

        app.exit()


if __name__ == "__main__":
    app = QApplication([])
    my_gui = MyMainGui()
    my_gui.show()
    app.exit(app.exec_())