#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Oct 26 16:42:08 2016
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
from gnuradio.wxgui import scopesink2
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
        self.samp_rate = samp_rate = 500000

        ##################################################
        # Blocks
        ##################################################
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab1")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab2")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab3")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab4")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab5")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab6")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab7")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab8")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab9")
        self.Add(self.notebook_0)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(6).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_0.GetPage(6).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_1_0 = fftsink2.fft_sink_c(
        	self.notebook_0.GetPage(8).GetWin(),
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
        	win=window.flattop,
        )
        self.notebook_0.GetPage(8).Add(self.wxgui_fftsink2_1_0.win)
        self.wxgui_fftsink2_1 = fftsink2.fft_sink_f(
        	self.notebook_0.GetPage(7).GetWin(),
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
        self.notebook_0.GetPage(7).Add(self.wxgui_fftsink2_1.win)
        self.wxgui_fftsink2_0_0_1_0 = fftsink2.fft_sink_c(
        	self.notebook_0.GetPage(3).GetWin(),
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
        self.notebook_0.GetPage(3).Add(self.wxgui_fftsink2_0_0_1_0.win)
        self.wxgui_fftsink2_0_0_1 = fftsink2.fft_sink_c(
        	self.notebook_0.GetPage(2).GetWin(),
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
        self.notebook_0.GetPage(2).Add(self.wxgui_fftsink2_0_0_1.win)
        self.wxgui_fftsink2_0_0_0_0 = fftsink2.fft_sink_f(
        	self.notebook_0.GetPage(5).GetWin(),
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
        	win=window.flattop,
        )
        self.notebook_0.GetPage(5).Add(self.wxgui_fftsink2_0_0_0_0.win)
        self.wxgui_fftsink2_0_0_0 = fftsink2.fft_sink_f(
        	self.notebook_0.GetPage(4).GetWin(),
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
        	win=window.flattop,
        )
        self.notebook_0.GetPage(4).Add(self.wxgui_fftsink2_0_0_0.win)
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
        	self.notebook_0.GetPage(1).GetWin(),
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
        self.notebook_0.GetPage(1).Add(self.wxgui_fftsink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
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
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 25e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 25e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.iir_filter_xxx_0_0 = filter.iir_filter_ffd(([0.002]), ([1,0.9999]), True)
        self.iir_filter_xxx_0 = filter.iir_filter_ffd(([0.002]), ([1,0.9999]), True)
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate, 10e6, 1)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_gr_complex*1, "127.0.0.1", 1234, 1472, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, "127.0.0.1", 1234, 1472, True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_conjugate_cc_2 = blocks.multiply_conjugate_cc(1)
        self.blocks_multiply_conjugate_cc_1 = blocks.multiply_conjugate_cc(1)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/arktheshadow/ARK-Linux/Programming/CommunicationLab/EE340L-Communication-Lab/140070011_endsem_communication_lab_ee340l/q2/File2.dat", True)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 10)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.band_pass_filter_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	1, samp_rate, 100e3, 150e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 125e3, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_conjugate_cc_1, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_1_0, 1))    
        self.connect((self.band_pass_filter_0, 0), (self.wxgui_fftsink2_0_0_1, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.iir_filter_xxx_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.iir_filter_xxx_0_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_conjugate_cc_2, 1))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_conjugate_cc_2, 0))    
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))    
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.wxgui_fftsink2_0_0, 0))    
        self.connect((self.blocks_multiply_conjugate_cc_1, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.blocks_multiply_conjugate_cc_2, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.wxgui_fftsink2_0_0_1_0, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_vco_c_0, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.wxgui_fftsink2_1, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_conjugate_cc_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_udp_sink_0, 0))    
        self.connect((self.blocks_vco_c_0, 0), (self.wxgui_fftsink2_1_0, 0))    
        self.connect((self.iir_filter_xxx_0, 0), (self.blocks_sub_xx_0, 0))    
        self.connect((self.iir_filter_xxx_0, 0), (self.wxgui_fftsink2_0_0_0, 0))    
        self.connect((self.iir_filter_xxx_0_0, 0), (self.blocks_sub_xx_0, 1))    
        self.connect((self.iir_filter_xxx_0_0, 0), (self.wxgui_fftsink2_0_0_0_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_multiply_xx_1_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 100e3, 150e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 25e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 25e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0_1.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0_1_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_1.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_1_0.set_sample_rate(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
