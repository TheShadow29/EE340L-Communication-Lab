#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Oct 26 16:06:28 2016
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
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from math import pi
from math import sqrt
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
        self.sps = sps = 6
        self.samp_rate = samp_rate = 600000
        self.rx_taps = rx_taps = firdes.root_raised_cosine(32,32*6,1.0,0.35,1024)
        self.al = al = 0.333

        ##################################################
        # Blocks
        ##################################################
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab1")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab2")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab3")
        self.Add(self.notebook_0)
        _al_sizer = wx.BoxSizer(wx.VERTICAL)
        self._al_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_al_sizer,
        	value=self.al,
        	callback=self.set_al,
        	label='al',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._al_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_al_sizer,
        	value=self.al,
        	callback=self.set_al,
        	minimum=0,
        	maximum=0.7,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_al_sizer)
        self.wxgui_scopesink2_1 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(1).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate/sps,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_0.GetPage(1).Add(self.wxgui_scopesink2_1.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(0).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate/6,
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
        self.iir_filter_xxx_0 = filter.iir_filter_ccz(([1,0,0,-al,0,0,al*al]), ([1]), True)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(6, pi/50, (rx_taps), 32, 16, 1.5, 1)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(pi/25, 8, False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_magphase_to_complex_0 = blocks.magphase_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/arktheshadow/ARK-Linux/Programming/CommunicationLab/EE340L-Communication-Lab/Endsem/q1/File1.dat", True)
        self.analog_const_source_x_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, pi/8)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_magphase_to_complex_0, 0))    
        self.connect((self.analog_const_source_x_1, 0), (self.blocks_magphase_to_complex_0, 1))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_magphase_to_complex_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))    
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.wxgui_scopesink2_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.iir_filter_xxx_0, 0))    
        self.connect((self.digital_costas_loop_cc_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.iir_filter_xxx_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))    

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.wxgui_scopesink2_1.set_sample_rate(self.samp_rate/self.sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate/6)
        self.wxgui_scopesink2_1.set_sample_rate(self.samp_rate/self.sps)

    def get_rx_taps(self):
        return self.rx_taps

    def set_rx_taps(self, rx_taps):
        self.rx_taps = rx_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rx_taps))

    def get_al(self):
        return self.al

    def set_al(self, al):
        self.al = al
        self._al_slider.set_value(self.al)
        self._al_text_box.set_value(self.al)
        self.iir_filter_xxx_0.set_taps(([1,0,0,-self.al,0,0,self.al*self.al]), ([1]))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
