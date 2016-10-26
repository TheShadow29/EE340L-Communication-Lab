#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Sep 14 15:45:49 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 1
        self.tuner = tuner = -18.3e3
        self.samp_rate = samp_rate = 960e3
        self.carrier_f = carrier_f = 150e3

        ##################################################
        # Blocks
        ##################################################
        _volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	label='volume',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	minimum=0,
        	maximum=2,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_volume_sizer)
        _tuner_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tuner_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tuner_sizer,
        	value=self.tuner,
        	callback=self.set_tuner,
        	label='tuner',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tuner_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tuner_sizer,
        	value=self.tuner,
        	callback=self.set_tuner,
        	minimum=-30e3,
        	maximum=-15e3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tuner_sizer)
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab1")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab2")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab3")
        self.Add(self.notebook_0)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.notebook_0.GetPage(0).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.notebook_0.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=30,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 30e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/arktheshadow/ARK-Linux/Programming/CommunicationLab/EE340L-Communication-Lab/Midsem/Q1/data.bin", True)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.audio_sink_0 = audio.sink(32000, "", True)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, carrier_f + tuner, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))
        self._volume_slider.set_value(self.volume)
        self._volume_text_box.set_value(self.volume)

    def get_tuner(self):
        return self.tuner

    def set_tuner(self, tuner):
        self.tuner = tuner
        self.analog_sig_source_x_0.set_frequency(self.carrier_f + self.tuner)
        self._tuner_slider.set_value(self.tuner)
        self._tuner_text_box.set_value(self.tuner)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 30e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_carrier_f(self):
        return self.carrier_f

    def set_carrier_f(self, carrier_f):
        self.carrier_f = carrier_f
        self.analog_sig_source_x_0.set_frequency(self.carrier_f + self.tuner)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
