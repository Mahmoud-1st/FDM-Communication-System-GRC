#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: xmahm
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
import math
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip
import threading



class Theory_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Theory_1")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.B = B = 20000
        self.AMstation = AMstation = 100000
        self.AM_BW = AM_BW = 2*B
        self.station = station = AMstation
        self.samp_rate = samp_rate = 441000
        self.frequency_offset = frequency_offset = 0
        self.Transition_Width_Low_freq = Transition_Width_Low_freq = 1000
        self.Transition_Width = Transition_Width = 1800
        self.Max_Deviation = Max_Deviation = 5000
        self.IF = IF = 25000
        self.FMstation = FMstation = 150000
        self.FM_BW = FM_BW = 2*B
        self.BW = BW = AM_BW
        self.Acarrier = Acarrier = 1

        ##################################################
        # Blocks
        ##################################################

        self._frequency_offset_range = qtgui.Range(0, 1000, 100, 0, 200)
        self._frequency_offset_win = qtgui.RangeWidget(self._frequency_offset_range, self.set_frequency_offset, "'frequency_offset'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._frequency_offset_win)
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=10,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=10,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=10,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
            44100, #size
            samp_rate, #samp_rate
            "m(t)", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(.1)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amp', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_f(
            32768, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "m(f)", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.1)
        self.qtgui_freq_sink_x_0_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_1.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_win)
        self.qtgui_freq_sink_x_0_0_0_1_0_1 = qtgui.freq_sink_f(
            32768, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "LPF → AM out", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0_0_1_0_1.set_update_time(0.1)
        self.qtgui_freq_sink_x_0_0_0_1_0_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0_0_1_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_1_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_1_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0_1_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0_1_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_1_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_1_0_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0_0_1_0_1.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0_0_1_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_1_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_1_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_1_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_1_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_1_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_1_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_1_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_1_0_1_win)
        self.qtgui_freq_sink_x_0_0_0_1_0_0_0 = qtgui.freq_sink_f(
            32768, #size
            window.WIN_HAMMING, #wintype
            0, #fc
            samp_rate, #bw
            "FM out", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0_0_1_0_0_0.set_update_time(0.1)
        self.qtgui_freq_sink_x_0_0_0_1_0_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0_0_1_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_1_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0_1_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0_1_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_1_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_1_0_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0_0_1_0_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0_0_1_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_1_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_1_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_1_0_0_0_win)
        self.qtgui_freq_sink_x_0_0_0_1_0_0 = qtgui.freq_sink_f(
            32768, #size
            window.WIN_HANN, #wintype
            0, #fc
            samp_rate, #bw
            "AM out", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0_0_1_0_0.set_update_time(0.1)
        self.qtgui_freq_sink_x_0_0_0_1_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0_0_1_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_1_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0_1_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0_1_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_1_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_1_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0_0_1_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0_0_1_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_1_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_1_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_1_0_0_win)
        self.qtgui_freq_sink_x_0_0_0_1_0 = qtgui.freq_sink_f(
            32768, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "baseband detector → LPF", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0_0_1_0.set_update_time(0.1)
        self.qtgui_freq_sink_x_0_0_0_1_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0_0_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_1_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0_0_1_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0_0_1_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_1_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_1_0_win)
        self.qtgui_freq_sink_x_0_0_0_1 = qtgui.freq_sink_f(
            32768, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "IF → baseband detector", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0_0_1.set_update_time(0.1)
        self.qtgui_freq_sink_x_0_0_0_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0_0_1.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_1_win)
        self.qtgui_freq_sink_x_0_0_0_0 = qtgui.freq_sink_f(
            32768, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Mixer → IF", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0_0_0.set_update_time(0.1)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_0_win)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_f(
            32768, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "RF → Mixer", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.1)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_f(
            32768, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "FDM", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.1)
        self.qtgui_freq_sink_x_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                (.5*BW),
                Transition_Width_Low_freq,
                window.WIN_HAMMING,
                6.76))
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_fcf(1, firdes.low_pass(1, samp_rate, BW, Transition_Width), (IF+frequency_offset), samp_rate)
        self.blocks_wavfile_source_0_0 = blocks.wavfile_source('E:\\2T\\Communication Theory 1\\Project\\kamhunt-run-130bpm-190419.wav', True)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(2)
        self.blocks_freqshift_cc_0 = blocks.rotator_cc(2.0*math.pi*FMstation/samp_rate)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(Acarrier)
        self.band_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                (IF-.5*BW),
                (IF+.5*BW),
                Transition_Width_Low_freq,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                (station-.5*BW),
                (station+.5*BW),
                Transition_Width,
                window.WIN_HAMMING,
                6.76))
        self.audio_sink_2 = audio.sink(44100, '', True)
        self.analog_sig_source_x_1_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, (IF+frequency_offset), 1, 0, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, (station+IF), 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 100000, Acarrier, 0, 0)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=samp_rate,
        	quad_rate=samp_rate,
        	tau=(75e-6),
        	max_dev=Max_Deviation,
        	fh=(-1.0),
                )
        self.analog_fm_demod_cf_0 = analog.fm_demod_cf(
        	channel_rate=samp_rate,
        	audio_decim=1,
        	deviation=Max_Deviation,
        	audio_pass=BW,
        	audio_stop=(BW+Transition_Width),
        	gain=1.0,
        	tau=(75e-6),
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fm_demod_cf_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.analog_nbfm_tx_0, 0), (self.blocks_freqshift_cc_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.band_pass_filter_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.band_pass_filter_0_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_0_0_0_1, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_freqshift_cc_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_0_0_0_1_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.qtgui_freq_sink_x_0_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.qtgui_freq_sink_x_0_0_0_1_0, 0))
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.qtgui_freq_sink_x_0_1, 0))
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_fm_demod_cf_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_nbfm_tx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.audio_sink_2, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_freq_sink_x_0_0_0_1_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.qtgui_freq_sink_x_0_0_0_1_0_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Theory_1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B
        self.set_AM_BW(2*self.B)
        self.set_FM_BW(2*self.B)

    def get_AMstation(self):
        return self.AMstation

    def set_AMstation(self, AMstation):
        self.AMstation = AMstation
        self.set_station(self.AMstation)

    def get_AM_BW(self):
        return self.AM_BW

    def set_AM_BW(self, AM_BW):
        self.AM_BW = AM_BW
        self.set_BW(self.AM_BW)

    def get_station(self):
        return self.station

    def set_station(self, station):
        self.station = station
        self.analog_sig_source_x_1.set_frequency((self.station+self.IF))
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.station-.5*self.BW), (self.station+.5*self.BW), self.Transition_Width, window.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.station-.5*self.BW), (self.station+.5*self.BW), self.Transition_Width, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.IF-.5*self.BW), (self.IF+.5*self.BW), self.Transition_Width_Low_freq, window.WIN_HAMMING, 6.76))
        self.blocks_freqshift_cc_0.set_phase_inc(2.0*math.pi*self.FMstation/self.samp_rate)
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, self.Transition_Width))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, (.5*self.BW), self.Transition_Width_Low_freq, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_1_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_1_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_1_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)

    def get_frequency_offset(self):
        return self.frequency_offset

    def set_frequency_offset(self, frequency_offset):
        self.frequency_offset = frequency_offset
        self.analog_sig_source_x_1_0.set_frequency((self.IF+self.frequency_offset))
        self.freq_xlating_fir_filter_xxx_0.set_center_freq((self.IF+self.frequency_offset))

    def get_Transition_Width_Low_freq(self):
        return self.Transition_Width_Low_freq

    def set_Transition_Width_Low_freq(self, Transition_Width_Low_freq):
        self.Transition_Width_Low_freq = Transition_Width_Low_freq
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.IF-.5*self.BW), (self.IF+.5*self.BW), self.Transition_Width_Low_freq, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, (.5*self.BW), self.Transition_Width_Low_freq, window.WIN_HAMMING, 6.76))

    def get_Transition_Width(self):
        return self.Transition_Width

    def set_Transition_Width(self, Transition_Width):
        self.Transition_Width = Transition_Width
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.station-.5*self.BW), (self.station+.5*self.BW), self.Transition_Width, window.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, self.Transition_Width))

    def get_Max_Deviation(self):
        return self.Max_Deviation

    def set_Max_Deviation(self, Max_Deviation):
        self.Max_Deviation = Max_Deviation
        self.analog_nbfm_tx_0.set_max_deviation(self.Max_Deviation)

    def get_IF(self):
        return self.IF

    def set_IF(self, IF):
        self.IF = IF
        self.analog_sig_source_x_1.set_frequency((self.station+self.IF))
        self.analog_sig_source_x_1_0.set_frequency((self.IF+self.frequency_offset))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.IF-.5*self.BW), (self.IF+.5*self.BW), self.Transition_Width_Low_freq, window.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0.set_center_freq((self.IF+self.frequency_offset))

    def get_FMstation(self):
        return self.FMstation

    def set_FMstation(self, FMstation):
        self.FMstation = FMstation
        self.blocks_freqshift_cc_0.set_phase_inc(2.0*math.pi*self.FMstation/self.samp_rate)

    def get_FM_BW(self):
        return self.FM_BW

    def set_FM_BW(self, FM_BW):
        self.FM_BW = FM_BW

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.station-.5*self.BW), (self.station+.5*self.BW), self.Transition_Width, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.IF-.5*self.BW), (self.IF+.5*self.BW), self.Transition_Width_Low_freq, window.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, self.Transition_Width))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, (.5*self.BW), self.Transition_Width_Low_freq, window.WIN_HAMMING, 6.76))

    def get_Acarrier(self):
        return self.Acarrier

    def set_Acarrier(self, Acarrier):
        self.Acarrier = Acarrier
        self.analog_sig_source_x_0.set_amplitude(self.Acarrier)
        self.blocks_add_const_vxx_0.set_k(self.Acarrier)




def main(top_block_cls=Theory_1, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
