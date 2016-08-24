#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Aug 24 17:04:18 2016
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
from gnuradio.wxgui import forms
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
        self.sr_unmodulated = sr_unmodulated = 40e3
        self.sr_rtl_sdr = sr_rtl_sdr = 2e6
        self.sr_fm_pm = sr_fm_pm = 640e3
        self.slider = slider = 75e3
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        _slider_sizer = wx.BoxSizer(wx.VERTICAL)
        self._slider_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_slider_sizer,
        	value=self.slider,
        	callback=self.set_slider,
        	label='slider',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._slider_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_slider_sizer,
        	value=self.slider,
        	callback=self.set_slider,
        	minimum=0,
        	maximum=1000e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_slider_sizer)
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "scope")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "fft")
        self.Add(self.notebook_0)
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(0).GetWin(),
        	title="Scope Plot",
        	sample_rate=sr_fm_pm,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_0.GetPage(0).Add(self.wxgui_scopesink2_0_0.win)
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_f(
        	self.notebook_0.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=sr_fm_pm,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.notebook_0.GetPage(1).Add(self.wxgui_fftsink2_0_0.win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=16,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, sr_fm_pm, 20e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.iir_filter_xxx_1 = filter.iir_filter_ffd(([1,-0.95]), ([1]), True)
        self.iir_filter_xxx_0 = filter.iir_filter_ffd(([1/sr_unmodulated]), ([1,1]), True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, sr_fm_pm,True)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((sr_fm_pm, ))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_2 = analog.sig_source_c(sr_fm_pm, analog.GR_COS_WAVE, 100e3, 1, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(sr_unmodulated, analog.GR_COS_WAVE, 11e3, .5, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(sr_unmodulated, analog.GR_COS_WAVE, 1.1e3, .5, 0)
        self.analog_phase_modulator_fc_0 = analog.phase_modulator_fc(2*3.14*slider)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.2, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 1))    
        self.connect((self.analog_phase_modulator_fc_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_add_xx_0, 0), (self.iir_filter_xxx_1, 0))    
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_conjugate_cc_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_1, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_complex_to_arg_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_scopesink2_0_0, 0))    
        self.connect((self.iir_filter_xxx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.iir_filter_xxx_1, 0), (self.iir_filter_xxx_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_phase_modulator_fc_0, 0))    

    def get_sr_unmodulated(self):
        return self.sr_unmodulated

    def set_sr_unmodulated(self, sr_unmodulated):
        self.sr_unmodulated = sr_unmodulated
        self.analog_sig_source_x_0.set_sampling_freq(self.sr_unmodulated)
        self.analog_sig_source_x_1.set_sampling_freq(self.sr_unmodulated)
        self.iir_filter_xxx_0.set_taps(([1/self.sr_unmodulated]), ([1,1]))

    def get_sr_rtl_sdr(self):
        return self.sr_rtl_sdr

    def set_sr_rtl_sdr(self, sr_rtl_sdr):
        self.sr_rtl_sdr = sr_rtl_sdr

    def get_sr_fm_pm(self):
        return self.sr_fm_pm

    def set_sr_fm_pm(self, sr_fm_pm):
        self.sr_fm_pm = sr_fm_pm
        self.analog_sig_source_x_2.set_sampling_freq(self.sr_fm_pm)
        self.blocks_throttle_0.set_sample_rate(self.sr_fm_pm)
        self.wxgui_scopesink2_0_0.set_sample_rate(self.sr_fm_pm)
        self.wxgui_fftsink2_0_0.set_sample_rate(self.sr_fm_pm)
        self.blocks_multiply_const_vxx_0.set_k((self.sr_fm_pm, ))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.sr_fm_pm, 20e3, 4e3, firdes.WIN_HAMMING, 6.76))

    def get_slider(self):
        return self.slider

    def set_slider(self, slider):
        self.slider = slider
        self.analog_phase_modulator_fc_0.set_sensitivity(2*3.14*self.slider)
        self._slider_slider.set_value(self.slider)
        self._slider_text_box.set_value(self.slider)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
