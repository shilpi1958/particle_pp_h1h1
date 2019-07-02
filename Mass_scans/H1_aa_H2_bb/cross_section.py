from __future__ import print_function
from ROOT import TCanvas, TGraph2D,gStyle, TGraph
from ROOT import gROOT
from math import sin
from array import array


gStyle.SetPalette(1)

def SetCanvas():

    # CMS inputs
    # -------------
    H_ref = 2000;
    W_ref = 3000;
    W = W_ref
    H  = H_ref

    T = 0.08*H_ref
    B = 0.21*H_ref
    L = 0.12*W_ref
    R = 0.08*W_ref
    # --------------

    c1 = TCanvas("c2","c2",2000,1500)
    c1.SetFillColor(0)
    c1.SetBorderMode(0)
    c1.SetFrameFillStyle(0)
    c1.SetFrameBorderMode(0)
    c1.SetLeftMargin( L/W )
    c1.SetRightMargin( R/W )
    c1.SetTopMargin( T/H )
    c1.SetBottomMargin( B/H )
    c1.SetTickx(0)
    c1.SetTicky(0)
    c1.SetTickx(1)
    c1.SetTicky(1)
    c1.SetGridy()
    c1.SetGridx()
    c1.SetLogy(1)
    return c1

c = SetCanvas()

gr1 = TGraph("H3_600GeV.dat")
gr1.SetTitle("Cross-Sections for H3 -> H1 (#gamma #gamma) H2 (b b~) ; M_{H2} [GeV] ; Cross-Sections [pb]" )
gr1.SetLineColor(2)
gr1.SetLineWidth(5)
gr2= TGraph("H3_800GeV.dat")
gr2.SetTitle("Cross-Sections for H3 -> H1 (#gamma #gamma) H2 (b b~) ; M_{H2} [GeV] ; Cross-Sections [pb]" )
gr2.SetLineColor(3)
gr2.SetLineWidth(4)
gr3= TGraph("H3_1000GeV.dat")
gr3.SetTitle("Cross-Sections for H3 -> H1 (#gamma #gamma) H2 (b b~) ; M_{H2} [GeV] ; Cross-Sections [pb]" )
gr3.SetLineColor(3)
gr3.SetLineWidth(4)
gr1.Draw("AC*")
gr2.Draw("CP*")
gr3.Draw("CP*")


c.SaveAs("Cross_Sections_H1_aa_H2_bb.png" )
c.SaveAs("Cross_Sections_H1_aa_H2_bb.root")
