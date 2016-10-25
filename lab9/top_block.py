#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Oct  5 16:18:46 2016
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
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from math import pi
from math import sqrt
from optparse import OptionParser
import numpy
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 3
        self.nfilts = nfilts = 32
        self.ntaps = ntaps = 11*nfilts*sps
        self.excess_bw = excess_bw = 0.4
        self.tx_taps = tx_taps = firdes.root_raised_cosine(nfilts,nfilts,1.0,excess_bw,ntaps)
        self.timing_bw = timing_bw = 2*pi/100
        self.symb_samp_rate = symb_samp_rate = 20000
        self.samp_rate = samp_rate = 32000
        self.rx_taps = rx_taps = firdes.root_raised_cosine(nfilts, nfilts*sps, 1.0,excess_bw, ntaps)
        self.output_sps = output_sps = 1
        self.freq_bw = freq_bw = 2*pi/100
        self.const_points = const_points = 8
        self.b4 = b4 = .062
        self.b3 = b3 = -.125
        self.b2 = b2 = 0.25
        self.b1 = b1 = -.5

        ##################################################
        # Blocks
        ##################################################
        self.notebook_1 = self.notebook_1 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_1.AddPage(grc_wxgui.Panel(self.notebook_1), "time")
        self.notebook_1.AddPage(grc_wxgui.Panel(self.notebook_1), "fft")
        self.notebook_1.AddPage(grc_wxgui.Panel(self.notebook_1), "out")
        self.notebook_1.AddPage(grc_wxgui.Panel(self.notebook_1), "new")
        self.Add(self.notebook_1)
        _b4_sizer = wx.BoxSizer(wx.VERTICAL)
        self._b4_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_b4_sizer,
        	value=self.b4,
        	callback=self.set_b4,
        	label='b4',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._b4_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_b4_sizer,
        	value=self.b4,
        	callback=self.set_b4,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_b4_sizer)
        _b3_sizer = wx.BoxSizer(wx.VERTICAL)
        self._b3_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_b3_sizer,
        	value=self.b3,
        	callback=self.set_b3,
        	label='b3',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._b3_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_b3_sizer,
        	value=self.b3,
        	callback=self.set_b3,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_b3_sizer)
        _b2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._b2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_b2_sizer,
        	value=self.b2,
        	callback=self.set_b2,
        	label='b2',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._b2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_b2_sizer,
        	value=self.b2,
        	callback=self.set_b2,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_b2_sizer)
        _b1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._b1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_b1_sizer,
        	value=self.b1,
        	callback=self.set_b1,
        	label='b1',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._b1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_b1_sizer,
        	value=self.b1,
        	callback=self.set_b1,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_b1_sizer)
        self.wxgui_scopesink2_0_0_1_0 = scopesink2.scope_sink_f(
        	self.notebook_1.GetPage(3).GetWin(),
        	title="Scope Plot",
        	sample_rate=symb_samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_1.GetPage(3).Add(self.wxgui_scopesink2_0_0_1_0.win)
        self.wxgui_scopesink2_0_0_1 = scopesink2.scope_sink_c(
        	self.notebook_1.GetPage(2).GetWin(),
        	title="Scope Plot",
        	sample_rate=symb_samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_1.GetPage(2).Add(self.wxgui_scopesink2_0_0_1.win)
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_c(
        	self.notebook_1.GetPage(0).GetWin(),
        	title="Scope Plot",
        	sample_rate=symb_samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=True,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_1.GetPage(0).Add(self.wxgui_scopesink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.notebook_1.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=symb_samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.notebook_1.GetPage(1).Add(self.wxgui_fftsink2_0.win)
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "new")
        self.Add(self.notebook_0)
        self.iir_filter_xxx_1 = filter.iir_filter_ffd(([0.001]), ([1,0.98]), True)
        self.iir_filter_xxx_0 = filter.iir_filter_ccf(([1,b1,b2,b3,b4]), ([1]), True)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((((1+0j),(1+1j)/sqrt(2),(0+1j),(1-1j)/sqrt(2),(-1 + 0j),(-1-1j)/sqrt(2),(0-1j),(-1+1j)/sqrt(2))), 1)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, symb_samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, symb_samp_rate,True)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((0.5, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1, ))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-1, ))
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, const_points, 1000)), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.05, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 1))    
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.iir_filter_xxx_1, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.iir_filter_xxx_0, 0))    
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_scopesink2_0_0, 0))    
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_add_xx_1, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_throttle_0_0, 0))    
        self.connect((self.iir_filter_xxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.iir_filter_xxx_0, 0), (self.wxgui_scopesink2_0_0_1, 0))    
        self.connect((self.iir_filter_xxx_1, 0), (self.wxgui_scopesink2_0_0_1_0, 0))    

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_ntaps(11*self.nfilts*self.sps)
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0,self.excess_bw, self.ntaps))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_ntaps(11*self.nfilts*self.sps)
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0,self.excess_bw, self.ntaps))
        self.set_tx_taps(firdes.root_raised_cosine(self.nfilts,self.nfilts,1.0,self.excess_bw,self.ntaps))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0,self.excess_bw, self.ntaps))
        self.set_tx_taps(firdes.root_raised_cosine(self.nfilts,self.nfilts,1.0,self.excess_bw,self.ntaps))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0,self.excess_bw, self.ntaps))
        self.set_tx_taps(firdes.root_raised_cosine(self.nfilts,self.nfilts,1.0,self.excess_bw,self.ntaps))

    def get_tx_taps(self):
        return self.tx_taps

    def set_tx_taps(self, tx_taps):
        self.tx_taps = tx_taps

    def get_timing_bw(self):
        return self.timing_bw

    def set_timing_bw(self, timing_bw):
        self.timing_bw = timing_bw

    def get_symb_samp_rate(self):
        return self.symb_samp_rate

    def set_symb_samp_rate(self, symb_samp_rate):
        self.symb_samp_rate = symb_samp_rate
        self.blocks_throttle_0.set_sample_rate(self.symb_samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.symb_samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.symb_samp_rate)
        self.wxgui_scopesink2_0_0.set_sample_rate(self.symb_samp_rate)
        self.wxgui_scopesink2_0_0_1.set_sample_rate(self.symb_samp_rate)
        self.wxgui_scopesink2_0_0_1_0.set_sample_rate(self.symb_samp_rate)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rx_taps(self):
        return self.rx_taps

    def set_rx_taps(self, rx_taps):
        self.rx_taps = rx_taps

    def get_output_sps(self):
        return self.output_sps

    def set_output_sps(self, output_sps):
        self.output_sps = output_sps

    def get_freq_bw(self):
        return self.freq_bw

    def set_freq_bw(self, freq_bw):
        self.freq_bw = freq_bw

    def get_const_points(self):
        return self.const_points

    def set_const_points(self, const_points):
        self.const_points = const_points

    def get_b4(self):
        return self.b4

    def set_b4(self, b4):
        self.b4 = b4
        self.iir_filter_xxx_0.set_taps(([1,self.b1,self.b2,self.b3,self.b4]), ([1]))
        self._b4_slider.set_value(self.b4)
        self._b4_text_box.set_value(self.b4)

    def get_b3(self):
        return self.b3

    def set_b3(self, b3):
        self.b3 = b3
        self.iir_filter_xxx_0.set_taps(([1,self.b1,self.b2,self.b3,self.b4]), ([1]))
        self._b3_slider.set_value(self.b3)
        self._b3_text_box.set_value(self.b3)

    def get_b2(self):
        return self.b2

    def set_b2(self, b2):
        self.b2 = b2
        self.iir_filter_xxx_0.set_taps(([1,self.b1,self.b2,self.b3,self.b4]), ([1]))
        self._b2_slider.set_value(self.b2)
        self._b2_text_box.set_value(self.b2)

    def get_b1(self):
        return self.b1

    def set_b1(self, b1):
        self.b1 = b1
        self.iir_filter_xxx_0.set_taps(([1,self.b1,self.b2,self.b3,self.b4]), ([1]))
        self._b1_slider.set_value(self.b1)
        self._b1_text_box.set_value(self.b1)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
