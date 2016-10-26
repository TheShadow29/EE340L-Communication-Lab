#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Sep 14 15:50:43 2016
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
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
        self.samp_rate = samp_rate = 100e3

        ##################################################
        # Blocks
        ##################################################
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab1")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab2")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab3")
        self.Add(self.notebook_0)
        self.wxgui_fftsink2_0_0_0 = fftsink2.fft_sink_c(
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
        self.notebook_0.GetPage(0).Add(self.wxgui_fftsink2_0_0_0.win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 20e3, 10, firdes.WIN_HAMMING, 6.76))
        self.hilbert_fc_0 = filter.hilbert_fc(6500, firdes.WIN_HAMMING, 6.76)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 20000, 2, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 10000, 0.05, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_add_xx_1, 1))    
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_throttle_0_0_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.hilbert_fc_0, 0))    
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_add_xx_1, 0))    
        self.connect((self.blocks_throttle_0_0_0, 0), (self.wxgui_fftsink2_0_0_0, 0))    
        self.connect((self.hilbert_fc_0, 0), (self.blocks_conjugate_cc_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_float_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0_0_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 20e3, 10, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
