#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Sep 13 20:03:22 2016
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
        self.samp_rate = samp_rate = 2e6
        self.message_f = message_f = 10e3
        self.carrier_f = carrier_f = 100e3

        ##################################################
        # Blocks
        ##################################################
        self.notebook_1 = self.notebook_1 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_1.AddPage(grc_wxgui.Panel(self.notebook_1), "fft1")
        self.notebook_1.AddPage(grc_wxgui.Panel(self.notebook_1), "fft2")
        self.notebook_1.AddPage(grc_wxgui.Panel(self.notebook_1), "fft3")
        self.Add(self.notebook_1)
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "scope1")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "scope2")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "scope3")
        self.Add(self.notebook_0)
        self.wxgui_scopesink2_0_0_1 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(1).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=True,
        	xy_mode=False,
        	num_inputs=2,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_0.GetPage(1).Add(self.wxgui_scopesink2_0_0_1.win)
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(2).GetWin(),
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
        self.notebook_0.GetPage(2).Add(self.wxgui_scopesink2_0_0.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(0).GetWin(),
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
        self.notebook_0.GetPage(0).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_0_0_0 = fftsink2.fft_sink_f(
        	self.notebook_1.GetPage(2).GetWin(),
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
        self.notebook_1.GetPage(2).Add(self.wxgui_fftsink2_0_0_0.win)
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_f(
        	self.notebook_1.GetPage(1).GetWin(),
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
        self.notebook_1.GetPage(1).Add(self.wxgui_fftsink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.notebook_1.GetPage(0).GetWin(),
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
        self.notebook_1.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((-1, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((-2, ))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_2 = blocks.add_const_vff((1, ))
        self.blocks_add_const_vxx_1_0 = blocks.add_const_vff((5, ))
        self.blocks_add_const_vxx_1 = blocks.add_const_vff((5, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((1.3, ))
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, 100000, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, message_f, 0.4, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 0.01, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_sub_xx_0, 0))    
        self.connect((self.blocks_add_const_vxx_1, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.blocks_add_const_vxx_1, 0), (self.wxgui_scopesink2_0_0_1, 0))    
        self.connect((self.blocks_add_const_vxx_1_0, 0), (self.blocks_sub_xx_0, 1))    
        self.connect((self.blocks_add_const_vxx_1_0, 0), (self.wxgui_fftsink2_0_0, 0))    
        self.connect((self.blocks_add_const_vxx_1_0, 0), (self.wxgui_scopesink2_0_0_1, 1))    
        self.connect((self.blocks_add_const_vxx_2, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_const_vxx_2, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_const_vxx_1, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_const_vxx_1_0, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.wxgui_fftsink2_0_0_0, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.wxgui_scopesink2_0_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0_0_1.set_sample_rate(self.samp_rate)

    def get_message_f(self):
        return self.message_f

    def set_message_f(self, message_f):
        self.message_f = message_f
        self.analog_sig_source_x_0.set_frequency(self.message_f)

    def get_carrier_f(self):
        return self.carrier_f

    def set_carrier_f(self, carrier_f):
        self.carrier_f = carrier_f


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
